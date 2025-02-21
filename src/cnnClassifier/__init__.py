import os  # Importing the os module to interact with the operating system
import sys  # Importing the sys module to handle system-specific parameters and functions
import logging  # Importing the logging module to enable logging

# Defining the logging format to include timestamp, log level, module name, and message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Defining the directory where log files will be stored
log_dir = "logs"

# Creating the full path for the log file
log_filepath = os.path.join(log_dir, "running_logs.log")

# Ensuring that the log directory exists; if not, it will be created
os.makedirs(log_dir, exist_ok=True)

# Configuring the logging settings
logging.basicConfig(
    level=logging.INFO,  # Setting the logging level to INFO
    format=logging_str,  # Specifying the log format
    handlers=[
        logging.FileHandler(log_filepath),  # Logging to a file
        logging.StreamHandler(sys.stdout)   # Logging to the console (standard output)
    ]
)

# Creating a logger instance with a specific name
logger = logging.getLogger("cnnClassifierLogger")
