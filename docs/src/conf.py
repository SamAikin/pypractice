# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import tomllib
from importlib.metadata import version as get_version

github_username = 'SamAikin'
github_repository = 'pypractice'

with open('../../pyproject.toml', 'rb') as toml_file:
    pyproject = tomllib.load(toml_file)

project = pyproject['project']['name']
copyright = "2025, Sam Aikin"
author = '; '.join([auth['name'] for auth in pyproject['project']['authors']])
release = get_version('pypractice')
version = release

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx_toolbox.shields",
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ["_static"]
