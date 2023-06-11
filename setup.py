from ensurepip import version
import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Chicken-Disease-Image-classification"
AUTHOR_USER_NAME = "Gourav"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "gourav052003@gmail.com"

setuptools.setup(

    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_mail = AUTHOR_EMAIL,
    description = "A small python package for cnn app",
    long_description = long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",

    project_urls = {
        "Bug tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },

    package_dir = {"":"src"},
    packages = setuptools.find_packages(where = "src")
)     
