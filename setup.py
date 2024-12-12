import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "example_repo"
AUTHOR_USER_NAME = "Mahavir Rajpurohit"
SRC_REPO = "mrajpurohit1912@gmail.com"
AUTHOR_EMAIL = "example_repo"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="a small python package",
    long_description=long_description,
    #long_description_content_type="text/markdown",
    long_description_content="text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    projects_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)