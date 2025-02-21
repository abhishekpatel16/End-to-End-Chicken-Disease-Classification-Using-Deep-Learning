import os  # Importing the OS module for interacting with the operating system
from box.exceptions import BoxValueError  # Importing BoxValueError for handling errors related to Box
import yaml  # Importing YAML for reading and writing YAML files
from cnnClassifier import logger  # Importing logger from cnnClassifier for logging
import json  # Importing JSON for reading and writing JSON files
import joblib  # Importing joblib for saving and loading binary files
from ensure import ensure_annotations  # Importing ensure_annotations for enforcing function annotations
from box import ConfigBox  # Importing ConfigBox to manage dictionary-like objects
from pathlib import Path  # Importing Path from pathlib for handling file paths
from typing import Any  # Importing Any from typing for type hinting
import base64  # Importing base64 for encoding and decoding binary data


@ensure_annotations  # Ensuring annotations are followed
# Function to read a YAML file and return its contents as a ConfigBox

def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its content as a ConfigBox.
    
    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: Any other exceptions encountered during reading.

    Returns:
        ConfigBox: Contains the YAML file data.
    """
    try:
        with open(path_to_yaml) as yaml_file:  # Opening the YAML file
            content = yaml.safe_load(yaml_file)  # Loading the contents using yaml
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")  # Logging successful load
            return ConfigBox(content)  # Returning the content as a ConfigBox
    except BoxValueError:  # Handling empty file error
        raise ValueError("YAML file is empty")
    except Exception as e:  # Handling any other exceptions
        raise e  
    

@ensure_annotations  # Ensuring annotations are followed
# Function to create directories from the provided list of paths

def create_directories(path_to_directories: list, verbose=True):
    """Creates directories from the provided list of paths.

    Args:
        path_to_directories (list): List of directory paths to be created.
        verbose (bool, optional): If True, logs directory creation. Defaults to True.
    """
    for path in path_to_directories:  # Iterating over each directory path
        os.makedirs(path, exist_ok=True)  # Creating directories (if they don't exist)
        if verbose:  # If verbose is enabled, log the creation
            logger.info(f"Created directory at: {path}")


@ensure_annotations  # Ensuring annotations are followed
# Function to save a dictionary as a JSON file

def save_json(path: Path, data: dict):
    """Saves dictionary data into a JSON file.

    Args:
        path (Path): Path where JSON file should be saved.
        data (dict): Data to be stored in JSON format.
    """
    with open(path, "w") as f:  # Opening the file in write mode
        json.dump(data, f, indent=4)  # Dumping dictionary data into the JSON file
    
    logger.info(f"JSON file saved at: {path}")  # Logging successful save


@ensure_annotations  # Ensuring annotations are followed
# Function to load data from a JSON file and return it as a ConfigBox

def load_json(path: Path) -> ConfigBox:
    """Loads data from a JSON file and returns it as a ConfigBox.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: Data stored as class attributes instead of a dictionary.
    """
    with open(path) as f:  # Opening the JSON file in read mode
        content = json.load(f)  # Loading the content
    
    logger.info(f"JSON file loaded successfully from: {path}")  # Logging successful load
    return ConfigBox(content)  # Returning the content as a ConfigBox


@ensure_annotations  # Ensuring annotations are followed
# Function to save data as a binary file using joblib

def save_bin(data: Any, path: Path):
    """Saves data as a binary file using joblib.

    Args:
        data (Any): Data to be saved in binary format.
        path (Path): Path to the binary file.
    """
    joblib.dump(value=data, filename=path)  # Saving the data as a binary file
    logger.info(f"Binary file saved at: {path}")  # Logging successful save


@ensure_annotations  # Ensuring annotations are followed
# Function to load binary data from a file using joblib

def load_bin(path: Path) -> Any:
    """Loads binary data from a file using joblib.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: The loaded object from the file.
    """
    data = joblib.load(path)  # Loading the binary file
    logger.info(f"Binary file loaded from: {path}")  # Logging successful load
    return data  # Returning the loaded data


@ensure_annotations  # Ensuring annotations are followed
# Function to return the size of a file in KB

def get_size(path: Path) -> str:
    """Returns the size of a file in KB.

    Args:
        path (Path): Path of the file.

    Returns:
        str: Size of the file in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)  # Getting the file size in KB
    return f"~ {size_in_kb} KB"  # Returning the formatted size


# Function to decode a base64 encoded image and save it as a file
def decodeImage(imgstring, fileName):
    """Decodes a base64 encoded image and saves it as a file.
    
    Args:
        imgstring (str): Base64 encoded image string.
        fileName (str): Name of the output image file.
    """
    imgdata = base64.b64decode(imgstring)  # Decoding base64 string
    with open(fileName, 'wb') as f:  # Opening file in write-binary mode
        f.write(imgdata)  # Writing decoded data to file


# Function to encode an image file into a base64 string
def encodeImageIntoBase64(croppedImagePath):
    """Encodes an image file into a base64 string.
    
    Args:
        croppedImagePath (str): Path to the image file.
    
    Returns:
        str: Base64 encoded string of the image.
    """
    with open(croppedImagePath, "rb") as f:  # Opening file in read-binary mode
        return base64.b64encode(f.read())  # Encoding file content as base64
