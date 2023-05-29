# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys 

sys.path.insert(0, "..")

project = 'Vistacare communications plugin docs'
copyright = '2023, Jhon Galindo'
author = 'Jhon Galindo'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

root_doc = 'index'

extensions = [
    'sphinx.ext.githubpages',
    'sphinx.ext.todo',
    'sphinxcontrib.images',
    'sphinx.ext.viewcode',
    'sphinx.ext.autodoc',
     'myst_parser'
]

templates_path = ['_templates']
exclude_patterns = []

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    'display_version': 'true',
    'sticky_navigation': 'true'
}

# -- Extension configuration -------------------------------------------------
import sys,os
sys.path.insert(0, os.path.abspath(".."))

images_config = {
    'override_image_directive': True,
    'default_image_width': '100%',
    'show_caption': True,
    'download': True
    }

gettext_compact = False
gettext_enables = ['index']
gettext_ignore_index = False

