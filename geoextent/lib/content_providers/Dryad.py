from requests import HTTPError
import urllib.parse
import zipfile
from .providers import DoiProvider
from ..extent import *


class Dryad(DoiProvider):
    def __init__(self):
        super().__init__()
        self.log = logging.getLogger("geoextent")
        self.host = {"hostname": ["https://datadryad.org/dataset/", "http://datadryad.org/dataset/"],
                     "api": "https://datadryad.org/api/v2/datasets/"
                     }
        self.reference = None
        self.record_id = None
        self.record_id_html = None
        self.name = "Dryad"

    def validate_provider(self, reference):
        self.reference = reference
        url = self.get_url
        if any([url.startswith(p) for p in self.host["hostname"]]):
            self.record_id = url.rsplit("/")[-2] + "/" + url.rsplit("/")[-1]
            self.record_id_html = urllib.parse.quote(self.record_id, safe="")
            return True
        else:
            return False

    def _get_metadata(self):

        if self.validate_provider:
            try:
                resp = self._request(
                    "{}{}".format(self.host["api"], self.record_id_html), headers={"accept": "application/json"}
                )
                resp.raise_for_status()
                self.record = resp.json()
                return self.record
            except:
                m = "The Dryad dataset : " + self.get_url + " does not exist"
                self.log.warning(m)
                raise HTTPError(m)
        else:
            raise ValueError('Invalid content provider')

    @property
    def _get_file_links(self):
        """
        try:
            self._get_metadata()
            record = self.record
        except ValueError as e:
            raise Exception(e)

        try:
            files = record['files']
        except:
            m = "This record does not have Open Access files. Verify the Access rights of the record."
            self.log.warning(m)
            raise ValueError(m)

        file_list = []
        for j in files:
            file_list.append(j['links']['self'])
        return file_list
        """
        # very simple method for download only, instead of 2+ API queries, but without metadata capabilities
        file_list = []
        file_list.append(self.host["api"] + self.record_id_html + "/download")
        return file_list


    def download(self, folder):
        self.log.debug("Downloading Dryad dataset id: {} ".format(self.record_id))
        try:
            download_links = self._get_file_links
            counter = 1
            for file_link in download_links:
                resp = self.session.get(file_link, stream=True)
                filename = "files.zip"
                filepath = os.path.join(folder, filename)
                try:
                    with open(filepath, "wb") as dst:
                        for chunk in resp.iter_content(chunk_size=None):
                            dst.write(chunk)
                    with zipfile.ZipFile(filepath, 'r') as zip_ref:
                        zip_ref.extractall(os.path.join(folder, "extracted"))
                except:
                    m = "The Dryad dataset : " + self.get_url + " does not exist"
                    self.log.warning(m)
                    raise HTTPError(m)
                self.log.debug("{} out of {} files downloaded.".format(counter, len(download_links)))
                counter += 1
        except ValueError as e:
            raise Exception(e)
