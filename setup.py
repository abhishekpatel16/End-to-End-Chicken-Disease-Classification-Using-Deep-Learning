# Import the setuptools package for packaging the Python project
import setuptools

# Read the contents of the README.md file to use as the long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Define the package version
__version__ = "0.0.0"

# Define metadata for the project
REPO_NAME = "End-to-End-Chicken-Disease-Classification-Using-Deep-Learning"
AUTHOR_USER_NAME = "abhishekpatel16"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "abhishekpatel0771@gmail.com"

# Configure the setup for the Python package
setuptools.setup(
    name=SRC_REPO,  # Package name
    version=__version__,  # Package version
    author=AUTHOR_USER_NAME,  # Author's name
    author_email=AUTHOR_EMAIL,  # Author's email
    description="A small python package for CNN app",  # Short description of the package
    long_description=long_description,  # Long description from README.md
    long_description_content="text/markdown",  # Format of the long description
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # URL of the project repository
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",  # Link to the issue tracker
    },
    package_dir={"": "src"},  # Location of the source code
    packages=setuptools.find_packages(where="src")  # Automatically find packages inside the 'src' directory
)
