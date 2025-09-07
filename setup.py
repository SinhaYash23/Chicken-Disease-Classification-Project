import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

__version__ = "0.0.1"

REPO_NAME = "Chicken-Disease-Classification-Project"
AUTHOR_USER_NAME = "YourGitHubUsername"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "sinha.yash3917@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for Chicken Disease Classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "tensorflow",
        "pandas",
        "dvc",
        "notebook",
        "matplotlib",
        "seaborn",
        "python-box==6.0.2",
        "pyYAML==6.0",
        "tqdm==4.64.1",
        "ensure==1.0.2",
        "joblib==1.2.0",
        "types-pyYAML==6.0.12",
        "scipy==1.10.1",
        "Flask==2.2.3",
        "Flask-Cors==3.0.10",
    ],
    entry_points={
        "console_scripts": [
            "cnnClassifier=cnnClassifier.__main__:main"
        ]
    },
)
