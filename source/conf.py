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

html_theme = 'pydata_sphinx_theme'

html_context = {
    "github_url": "https://github.com", 
    "github_user": "fadhil-riyanto",
    "github_repo": "www.fadev.org",
    "github_version": "master",
    "doc_path": "source",
}


html_theme_options = {
        "navbar_end": ["navbar-icon-links"],
        "use_edit_page_button": True,
        "footer_center": ["aboutme", "contact"],
}



extensions = [
        'sphinx.ext.duration',
        'sphinx_design',
        'myst_parser',
        'sphinx_copybutton'
]
