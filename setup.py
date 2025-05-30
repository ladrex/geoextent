import setuptools
from geoextent import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="geoextent",
    version=__version__,
    author="o2r-project",
    author_email="o2r.team@uni-muenster.de",
    description="A package to extract geospatial extent from files and directories",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/o2r-project/geoextent",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pyproj',
        'geojson>=2.4.1',
        'pygeoj',
        'pyshp',
        'gdal',
        'patool',
        'python-dateutil',
        'pandas',
        'requests',
        'numpy',
        'traitlets',
        'wheel'
    ],
    entry_points={
        "console_scripts": [
            "geoextent = geoextent.__main__:main",
        ]
    },
)
