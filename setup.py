import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="conektango",
    version="0.0.1",
    author="Alex Dzul",
    author_email="alex@kiub.tech",
    description="The easiest way to integrate Conekta.io with Django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kiubtech/conektango",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
