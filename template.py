import os  # Importing the OS module for interacting with the operating system
from pathlib import Path  # Importing Path from pathlib for handling file paths
import logging  # Importing logging module for logging messages

# Configuring logging to display messages with timestamp
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Defining the project name
project_name = "cnnClassifier"

# List of files and directories to be created
list_of_files = [
    ".github/workflows/.gitkeep",  # GitHub workflows directory
    f"src/{project_name}/__init__.py",  # Package initializer
    f"src/{project_name}/components/__init__.py",  # Components module
    f"src/{project_name}/utils/__init__.py",  # Utils module
    f"src/{project_name}/utils/common.py",  # Common utility functions
    f"src/{project_name}/config/__init__.py",  # Config module
    f"src/{project_name}/config/configuration.py",  # Configuration settings
    f"src/{project_name}/pipeline/__init__.py",  # Pipeline module
    f"src/{project_name}/entity/__init__.py",  # Entity module
    f"src/{project_name}/entity/config_entity.py",  # Config entity definitions
    f"src/{project_name}/constants/__init__.py",  # Constants module
    "config/config.yaml",  # Configuration file
    "params.yaml",  # Parameters file
    "main.py",  # Main application script
    "app.py",  # Application entry point
    "requirements.txt",  # Dependencies file
    "setup.py",  # Setup script for packaging
    "research/trials.ipynb",  # Jupyter Notebook for research
    "templates/index.html",  # HTML template file
]

# Iterating through each file path in the list
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert string path to Path object
    filedir, filename = os.path.split(filepath)  # Separate directory and filename

    # If directory path is not empty, create the directory if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Create the file if it does not exist or if it is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:  # Create an empty file
            pass
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")  # Log message if file exists
