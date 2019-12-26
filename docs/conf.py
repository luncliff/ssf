# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

from os import getcwd
from os.path import join

import guzzle_sphinx_theme

# -- Project information -----------------------------------------------------

project = 'ssf'
copyright = '2019, github.com/luncliff'
author = 'github.com/luncliff'

release = '1.0'

# -- General configuration ---------------------------------------------------

extensions = ['breathe', 'guzzle_sphinx_theme']
templates_path = ['_templates']

language = 'kr'

exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme_path = guzzle_sphinx_theme.html_theme_path()
html_theme = 'guzzle_sphinx_theme'
# html_static_path = ['_static']

# -- Options for Breadthe -------------------------------------------------

# https://breathe.readthedocs.io/en/latest/quickstart.html

breathe_projects = {"ssf": join(getcwd(), 'doxygen', 'xml')}
breathe_default_project = 'ssf'
