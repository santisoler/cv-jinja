#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import yaml
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

DESCRIPTION = """
Renders the CV using Jinja2 templates
"""


def get_argparser():
    """
    Create the arguments parser object
    """
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(
        "--yml",
        metavar="cv.yml",
        required=True,
        type=argparse.FileType("r"),
        help="YAML file containing the data of the CV",
    )
    parser.add_argument(
        "--template",
        required=True,
        type=argparse.FileType("r"),
        help="Jinja2 template file for building the CV",
    )
    parser.add_argument(
        "--output",
        required=True,
        type=argparse.FileType("w"),
        help="Jinja2 template file for building the CV",
    )
    return parser


if __name__ == "__main__":

    # Create the arguments parser
    parser = get_argparser()
    arguments = parser.parse_args()

    # Read cv.yml file
    cv_data = yaml.load(arguments.yml, Loader=yaml.FullLoader)

    # Read Markdown template
    template_file = Path(str(arguments.template.name))
    loader = FileSystemLoader(str(template_file.parent))
    environment = Environment(loader=loader)
    template = environment.get_template(str(template_file.name))

    # Render the CV
    arguments.output.write(template.render(**cv_data))
