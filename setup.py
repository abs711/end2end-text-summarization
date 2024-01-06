import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    description = f.read()

    __version__ = "0.0.0"

    REPO_NAME = "e2e-text-summarization"
    AUTHOR_USER_NAME = "abs711"
    SRC_REPO = "e2e_text_summarization"
    AUTHOR_EMAIL = "as711@uw.edu"


    setuptools.setup(
        name=SRC_REPO,
        version= __version__,
        author=AUTHOR_USER_NAME,
        author_email=AUTHOR_EMAIL,
        description="text summarization using transformers",
        long_description=description,
        long_description_content="text/markdown",
        url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
        project_urls={"Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",},
        package_dir={"": "src"},
        packages=setuptools.find_packages(where="src")
    )