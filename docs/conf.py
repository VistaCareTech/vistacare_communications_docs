# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys 

sys.path.insert(0, "..")

project = 'VistaCare Communications plugin docs'
copyright = '2025, Jhon Galindo'
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
    'sphinx_copybutton',
    'myst_parser'
]

'''myst_enable_extensions = ["deflist",
                          "colon_fence"]'''

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
html_css_files = ["custom.css",
                  "fancybox.css"]

html_js_files = [
    'fancybox.umd.js', 
    'custom_lightbox_init.js',
]

html_theme_options = {
    'display_version': 'true',
    'sticky_navigation': 'true',
    'style_nav_header_background': '#a9c6e9'
}

html_logo = '_static/VistaCare_Logo.png'

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