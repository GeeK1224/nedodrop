from setuptools import find_packages, setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup (
    name='nedodrop',
    version='0.1.0',
    description="Linux file transfering app",
    package_dir={"": "nedodrop"},
    packages=find_packages(where='nedodrop'),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    author="nedogeek",
    author_email="urunbaev.timur@gmail.com",
    license="",
    classifiers=[
        "License :: OSI Approved :: ",
        "Programming Language :: Python :: 3.12",
        "Operating System :: Linux"
    ],
    install_requires=[""],
    extras_require={

    },
    python_requires=">=3.10",
)