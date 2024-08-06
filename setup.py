import setuptools

setuptools.setup(
    name="topognn",
    version="0.1.0",
    author="-",
    author_email="-",
    description="-",
    long_description="-",
    long_description_content_type="-",
    url="-",
    project_urls={
        "Bug Tracker": "-",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "",
        "",
    ],
    package_dir={"": "topognn"},
    packages=setuptools.find_packages(where="topognn"),
    install_requires=["torch"],
    python_requires=">=3.7.1",
)
