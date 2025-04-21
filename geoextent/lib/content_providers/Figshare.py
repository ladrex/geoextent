from requests import HTTPError
from .providers import DoiProvider
from ..extent import *


class Figshare(DoiProvider):
    def __init__(self):
        super().__init__()
        self.log = logging.getLogger("geoextent")
        self.host = {"hostname": ["https://figshare.com/articles/", "http://figshare.com/articles/"],
                     "api": "https://api.figshare.com/v2/articles/"
                    }
        self.reference = None
        self.record_id = None
        self.name = "Figshare"

    def validate_provider(self, reference):
        self.reference = reference
        url = self.get_url
        if any([url.startswith(p) for p in self.host["hostname"]]):
            self.record_id = url.rsplit("/", maxsplit=1)[1]
            return True
        else:
            return False

    def _get_metadata(self):

        if self.validate_provider:
            try:
                resp = self._request(
                    "{}{}".format(self.host["api"], self.record_id), headers={"accept": "application/json"}
                )
                resp.raise_for_status()
                self.record = resp.json()
                return self.record
            except:
                m = "The Figshare item : https://figshare.com/articles/" + self.record_id + " does not exist"
                self.log.warning(m)
                raise HTTPError(m)
        else:
            raise ValueError('Invalid content provider')

    @property
    def _get_file_links(self):

        try:
            self._get_metadata()
            record = self.record
        except ValueError as e:
            raise Exception(e)

        try:
            files = record['files']
        except:
            m = "This item does not have Open Access files. Verify the Access rights of the item."
            self.log.warning(m)
            raise ValueError(m)

        file_list = []
        for j in files:
            file_list.append(j['download_url'])
            # TODO files can be empty
        return file_list

    def download(self, folder):
        self.log.debug("Downloading Figshare item id: {} ".format(self.record_id))
        try:
            download_links = self._get_file_links
            counter = 1
            for file_link in download_links:
                resp = self.session.get(file_link, stream=True)
                filename = file_link.split('/')[-2]
                filepath = os.path.join(folder, filename)
                with open(filepath, "wb") as dst:
                    for chunk in resp.iter_content(chunk_size=None):
                        dst.write(chunk)
                self.log.debug("{} out of {} files downloaded.".format(counter, len(download_links)))
                counter += 1
        except ValueError as e:
            raise Exception(e)
