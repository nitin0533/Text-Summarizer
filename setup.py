import setuptools
with open("README.md","r", encoding="utf-8") as f:
    long_description=f.read()
__version__ = "0.0.0"
REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME= 'nitin0533'
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "nitiniyer.95@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version= __version__,
    author= AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description= "Text Summarizer Project",
    long_description= long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/nitin0533/textSummarizer",
    project_urls={
        "Bug Tracker": "https://github.com/nitin0533/text/issues",
    },
    package_dir= {"": "src"},
    packages=setuptools.find_packages(where="src")
)