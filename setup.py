import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="linked list",
    version="0.0.1",
    author="M T",
    author_email="marcin.tyman@gmail.com",
    description="An example of implementation of LinkedList",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sirtyman/linked_list",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
