#!/usr/bin/env python
import argparse
import yaml
from jinja2 import Environment

DESCRIPTION = """
Renders the CV using Jinja2 templates
"""
JINJA2_KEYS = ["info", "page_layout", "sections"]


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

    # Fill the cv_data with missing jinja2 keys
    for key in JINJA2_KEYS:
        if key not in cv_data:
            cv_data[key] = None

    # Read Markdown template
    template = arguments.template.read()
    environment = Environment().from_string(template)

    # Render the CV
    arguments.output.write(environment.render(**cv_data))
