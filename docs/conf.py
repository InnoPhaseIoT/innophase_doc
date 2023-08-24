import os
import sys

sys.path.insert(0, os.path.abspath('..'))
project = 'InnoPhase'
copyright = '2023, InnoPhase'
author = 'InnoPhase'
release = '1.0.1'

extensions = [
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
]

intersphinx_mapping = {
    "rtd": ("https://docs.readthedocs.io/en/stable/", None),
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]
epub_show_urls = "footnote"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]


def get_versions():
    return {
        'Version': 'latest',
        '1.0.0': 'https://innophase-iot-innophase-doc.readthedocs-hosted.com/en/v1.0/',
    }


def get_modules():
    return {
        "Module": "#",
        'Talaria-TWO': 'https://innophase.com/docs/v1.0',
    }


html_context = {
    'get_modules': get_modules,
    "get_versions": get_versions,
}
