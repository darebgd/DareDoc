# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Chipsee Documentation Drafts'
copyright = '2021, Chipsee'
author = 'Darko'
version = '1.0'

# The full version, including alpha/beta/rc tags
release = '02'

# -- General configuration ---------------------------------------------------
import os
import sys
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx_rtd_theme']
#, 'sphinxemoji.sphinxemoji','sphinx_tabs.tabs','sphinx_copybutton']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
import sphinx_rtd_theme

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'prev_next_buttons_location': 'None',    
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 5,
    'includehidden': True,
    'titles_only': False
}

html_style = 'css/my_theme.css' 

html_show_sourcelink = False
#html_js_files = ['js/expand_tabs.js']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_show_sphinx = False

rst_epilog = """

.. |Intel| replace:: Intel\ :sup:`®`

.. |Celeron| replace:: Celeron\ :sup:`®`

.. |Arm| replace:: Arm\ :sup:`®`

.. |Cortex| replace:: Cortex\ :sup:`®`

.. role:: underline
    :class: underline

"""

html_last_updated_fmt = '%b %d, %Y'
html_context = {
"display_github": False, # Add 'Edit on Github' link instead of 'View page source'
"commit": False,
}

