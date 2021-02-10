#!/usr/env python
import yaml
from jinja2 import Environment


if __name__ == "__main__":

    # Read cv.yml file
    with open("cv.yml", "r") as f:
        cv_data = yaml.load(f, Loader=yaml.FullLoader)

    # Read Markdown template
    with open("cv_template.md", "r") as f:
        md_template = f.read()
    md_environment = Environment().from_string(md_template)

    with open("out.md", "w") as f:
        f.write(
            md_environment.render(
                info=cv_data["info"],
                sections=cv_data["sections"],
            )
        )
