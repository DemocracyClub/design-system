#!/usr/bin/env python3
import os
import json

from setuptools import setup

def get_version():
    package_json = json.load(open("package.json"))
    return package_json["version"]

setup(
    name="dc_design_system",
    version=get_version(),
    description="SCSS and images for the DC design system",
    author="Sym Roe",
    author_email="sym.roe@democracyclub.org.uk",
    packages=[
        "dc_design_system",
        "dc_design_system/system",
    ],
    package_dir={
        "dc_design_system": "python-package",
        "dc_design_system/system": "system",
    },
    package_data={
        "dc_design_system/system": [
            "*",
            "**/*",
        ]
    },
    setup_requires=["wheel"],
)
