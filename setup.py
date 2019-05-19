import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cli-app",
    version="0.1.0",
    author="Joseph Paul",
    author_email="joseph@sehrgute.software",
    description="Framework for creating CLI apps using Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jsphpl/python-cli-app",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
