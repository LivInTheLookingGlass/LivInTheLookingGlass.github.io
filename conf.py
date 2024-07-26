from textwrap import dedent
from sphinxnotes.any import Schema, Field
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Portfolio'
copyright = '2024, Olivia Appleton'
author = 'Olivia Appleton'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinxnote_any',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']


project = Schema('project',
    name=Field(referenceable=True, form=Field.Form.LINES),
    attrs={
        'id': Field(unique=True, referenceable=True, required=True),
        'title': Field(referenceable=True, required=True),
        'start': Field(referenceable=True, required=True),
        'end': Field(referenceable=True),
        'description': Field(),
        'link': Field(),
        'tags': Field(referenceable=True, required=True, form=Field.Form.WORDS),
    },
    description_template=dedent("""
        :id: {{ id }}
        :title: {{ title }}
        :start: {{ start }}
        :end: {{ end }}
        :description: {{ description }}
        :link: {{ title }}
        :tags: {{ tags }}

        {{ content }}""")
)
