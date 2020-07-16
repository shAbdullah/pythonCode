import setuptools
with open("README.md", "r") as fh:
long_description = fh.read()


setuptools.setup(
    name="example-pkg-kh", 
    version="0.0.1",
    author="Abdullah",
    author_email="aiaas2010@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/knowledgehut-aws/python-101",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",],
    python_requires='>=3.6',
    )
