#!/usr/bin/env python3
import os

from setuptools import setup

setup(
    name="dc_design_system",
    version="0.0.1",
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
