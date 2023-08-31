#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from recommonmark.parser import CommonMarkParser

import os
import sys

sys.path.insert(0, os.path.abspath('.'))

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

templates_path = ['_templates']

master_doc = 'index'

# General information about the project.
project = 'InnoPhase'
copyright = '2023, InnoPhase IoT, Inc'
author = 'InnoPhase'
release = '1.0.0'

language = 'en'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'
highlight_language = 'python'

todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'


def setup(app):
    app.add_css_file('css/custom.css')
    # app.add_js_file("js/custom.js")


source_parsers = {'.md': CommonMarkParser}

source_suffix = ['.rst', '.md']
html_static_path = ['_static']

html_sidebars = {
    '**': [
        'about.html',
    ]
}

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'InnoPhase IoT'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [(master_doc, 'InnoPhase IoT')]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, 'InnoPhase IoT', [author], 1)]

texinfo_documents = [(master_doc, 'InnoPhase IoT', 'InnoPhase IoT Programming Guide', author)]


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