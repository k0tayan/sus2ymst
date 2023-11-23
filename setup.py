import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sus2ymst",  # Replace with your own username
    version="0.0.3",
    install_requires=[
        "sus-io",
    ],
    entry_points={
        "console_scripts": [
            "sus2ymst=sus2ymst.cli:main",
        ],
    },
    author="k0tayan",
    author_email="kotayan0415@outlook.jp",
    description="Convert Ched SUS to YMST(world dai star) txt chart format.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/k0tayan/sus2ymst",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.9",
)
