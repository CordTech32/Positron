import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Positron",
    version="1.0.",
    author="Stift007",
    author_email="stift007@stift007.de",
    description=" Deploy Flask Applications into Distributables ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cordtech32/positron",
    project_urls={
        "Bug Tracker": "https://github.com/cordtech32/positron/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires=["PyQt5","PyQtWebEngine"]
)