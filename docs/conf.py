# -*- coding: utf-8 -*-

import sys
import os
import shlex

sys.path.insert(0, os.path.abspath('..')) # path to `exhale`
import exhale

# TODO: figure out what's going on with viewcode
# from exhale import configs
# from exhale import deploy
# from exhale import graph
# from exhale import parse
# from exhale import utils
# viewcode_import = True

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.0'

# General information about the project.
project = u'Exhale'
copyright = u'2018, Stephen McDowell'
author = u'Stephen McDowell'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.graphviz',
    'sphinx.ext.intersphinx',
    # NOTE: viewcode isn't working, probably because of how my docs are setup
    #       and the lack of __all__ definitions?
    'sphinx.ext.viewcode'
]

intersphinx_mapping = {
    'python': ('http://docs.python.org/', None),
    'sphinx': ('http://sphinx.pocoo.org', None),
    'pytest': ('https://docs.pytest.org/en/latest/', None),
    # See _intersphinx/README.md
    'bs4':    ('https://www.crummy.com/software/BeautifulSoup/bs4/doc', "_intersphinx/bs4_objects.inv")
}

# make linkcheck does not support GitHub README.md anchors (they are synthetic anchors)
linkcheck_ignore = [
    r'https://github.com/jonmiles/bootstrap-treeview#.*'
]

# show :autoclass: member definitions as defined in exhale.py
autodoc_member_order = 'bysource'

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst']

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = exhale.__version__
# The full version, including alpha/beta/rc tags.
release = exhale.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
todo_link_only     = True

# -- Options for HTML output ----------------------------------------------

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    # TODO: figure out how to compile SASS so you can fix this
    #       https://github.com/rtfd/sphinx_rtd_theme/issues/457
    # "navigation_depth": 5,
    # "collapse_navigation": False
    #
    # Then change testing/tests.rst section headings to what you wanted
    # <h1>All Tests</h1>
    # .. automodule:: testing.tests
    # <h2>Exhale Core Tests</h2>
    # ...
    # <h2>Project Tests</h2>
    # ...
}

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'Exhale: Automatic C++ Library API Generation'

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = 'Exhale'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'ExhaleDoc'

# convenience replacements for writing e.g. |containmentFolder| and linking to the
# member of exhale.configs.Config.containmentFolder
import itertools
from exhale.configs import Config

configs_Config_repl_list = [
    'containmentFolder'
    # TODO: after migration, just use this
    # pack[0] for pack in itertools.chain(Config.REQUIRED_KV, Config.OPTIONAL_KV)
]
configs_Config_replacements = '\n'.join(
    '.. |{config}| replace:: :data:`~exhale.configs.Config.{config}`'.format(config=config)
    for config in configs_Config_repl_list
)
configs_DoxygenConfig_repl_list = [
    'stripFromPath'
]
configs_DoxygenConfig_replacements = '\n'.join(
    '.. |{config}| replace:: :data:`~exhale.configs.DoxygenConfig.{config}`'.format(config=config)
    for config in configs_DoxygenConfig_repl_list
)
rst_epilog = '\n'.join([
    configs_Config_replacements,
    configs_DoxygenConfig_replacements
])


def setup(app):
    import os
    import sys
    # make sure you can import by modifying sys.path
    extensions_dir = os.path.join(
       os.path.abspath(os.path.dirname(__file__)),
       '_extensions'
    )
    sys.path.insert(0, extensions_dir)
    ####################################################################################
    # Add directive: .. testproject::                                                  #
    ####################################################################################
    from testproject import testproject, visit_testproject_node, depart_testproject_node, TestProjectDirective
    app.add_node(testproject, html=(visit_testproject_node, depart_testproject_node))
    app.add_directive('testproject', TestProjectDirective)
    ####################################################################################
    # Add directives: .. member:: and .. param::                                       #
    ####################################################################################
    # import and add the new directives
    from attr_param import AttrDirective, ParamDirective
    app.add_directive('attr', AttrDirective)
    app.add_directive('param', ParamDirective)
    ####################################################################################
    # Multiline string documentation                                                   #
    ####################################################################################
    import textwrap

    from exhale.configs import DEFAULT_DOXYGEN_STDIN_BASE
    default_parts = DEFAULT_DOXYGEN_STDIN_BASE.strip().splitlines()
    multiline_var = "\n   ".join(p for p in default_parts)
    with open("DEFAULT_DOXYGEN_STDIN_BASE_value.rst", "w") as dcv:
        dcv.write(textwrap.dedent('''
            The value of this variable is a multiline string with contents:

            .. code-block:: py

        '''))
        dcv.write("   {multiline_var}".format(multiline_var=multiline_var))
        dcv.write(textwrap.dedent('''
            .. note::

               The above value is presented for readability, when using this variable take
               note of any leading or trailing ``\\n`` characters.
        '''))
