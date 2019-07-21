import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shockmarket_diveone",
    version="0.0.1",
    author="K Hudson",
    author_email="dev@divethree.com",
    description="A stock market game simulator.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/diveone/shockmarket",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3",
        "Operating System :: OS Independent",
    ],
)
