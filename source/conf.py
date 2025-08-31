# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


import os

project = 'Fadhil Journal'
copyright = '2025, Fadhil Riyanto'
author = 'Fadhil Riyanto'
html_short_title = project

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'piccolo_theme'
html_theme_path =  [os.path.abspath("../submodule/piccolo_theme")]

html_theme_options = {
        "banner_text": 'blog.fadev.org will be deprecated soon...',
        "show_theme_credit": True,
        "source_url": "https://github.com/fadhil-riyanto/www.fadev.org"
}

extensions = [
        'sphinx.ext.duration',
        'myst_parser'
]
