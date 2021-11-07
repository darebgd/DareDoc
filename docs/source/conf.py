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
release = '03'
import sphinx_rtd_theme
# -- General configuration ---------------------------------------------------
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx_rtd_theme']
#, 'sphinxemoji.sphinxemoji','sphinx_tabs.tabs','sphinx_copybutton']

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.


#html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme = "sphinx_rtd_theme"
html_theme_path = ['.']

html_theme_options = {
    'prev_next_buttons_location': 'none',    
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 5,
    
}

html_style = 'css/RTD_custom.css'
file_insertion_enabled = True
# html_show_sourcelink = False
# html_js_files = ['js/expand_tabs.js']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
#numfig = True
#numfig_secnum_depth = 1
numfig_format = {'figure': '',
                 'table': '',
                 'code-block': '',
                }
html_show_sphinx = False
html_show_sourcelink = False




rst_epilog = """

.. |Intel| replace:: Intel\ :sup:`®`

.. |Celeron| replace:: Celeron\ :sup:`®`

.. |Arm| replace:: Arm\ :sup:`®`

.. |Cortex| replace:: Cortex\ :sup:`®`

.. |Core| replace:: Core™

.. |br| raw:: html 

   <br>

.. _cstore: https://chipsee.com/

.. |cstore| replace:: **Chipsee Store**

.. _mguide: https://chipsee.com/mount-ipc-guide/

.. |mguide| replace:: **Mount IPC Guide**

.. _email: service@chipsee.com

.. |email| replace:: **service@chipsee.com**

.. |cd| replace:: cd/m\ :sup:`2`

.. |r| replace:: :sup:`®`

"""

html_last_updated_fmt = '%b %d, %Y'
#html_context = {
#"display_github": True, # Add 'Edit on Github' link instead of 'View page source'
#"commit": False,
#}

tablecaption = 'below'