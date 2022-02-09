import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SAPOFTO",
    version="0.0.6",
    author="Shane Allcroft",
    author_email="shaneallcroft@fedoraproject.org",
    description="Parse, compose, evaluate and execute org files and data in org-down notation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shaneallcroft/SAPOFTO",
    project_urls={
        "Bug Tracker": "https://github.com/shaneallcroft/SAPOFTO/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
