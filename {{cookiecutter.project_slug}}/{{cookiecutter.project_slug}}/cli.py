# -*- coding: utf-8 -*-

"""Console script for {{cookiecutter.project_slug}}."""
import sys
import argparse

def main(args=None):
    """Console script for {{cookiecutter.project_slug}}."""

    parser = argparse.ArgumentParser(description='Command line executable for {{cookiecutter.project_slug}}.')
    args = parser.parse_args()

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
