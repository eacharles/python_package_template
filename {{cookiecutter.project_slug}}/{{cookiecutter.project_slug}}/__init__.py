# -*- coding: utf-8 -*-
"""Top-level package for {{ cookiecutter.project_name }}."""
from pkg_resources import get_distribution, DistributionNotFound

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = '{{ cookiecutter.email }}'

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass
