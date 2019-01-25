import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# Get dependencies
with open('minikube_cloud/requirements.txt') as requirements:
    required = requirements.read().splitlines()

# This call to setup() does all the work
setup(
    name="minikube-cloud",
    version="0.0.1",
    description="Run a minikube kuberentes cluster on cloud.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/cloudyuga/minikube-cloud",
    author="Vishal Ghule, Sumit Murari",
    author_email="vishal@cloudyuga.guru, sumit@cloudyuga.guru",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
    packages=["minikube_cloud", "minikube_cloud.provider"],
    include_package_data=True,
    install_requires=required,
    entry_points={
        "console_scripts": [
            "minikube-cloud=minikube_cloud.main:main",
        ]
    },
)
