import json
import datetime
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def load_config(config_file_path='config.json'):
    """
    Loads configuration settings from a JSON file.

    Args:
        config_file_path (str, optional): Path to the configuration file.
                                          Defaults to 'config.json'.

    Returns:
        dict: A dictionary containing the configuration settings.
              Returns an empty dictionary if the file is not found or invalid.
    """
    try:
        with open(config_file_path, 'r') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        logging.error(f"Configuration file not found at: {config_file_path}")
        return {}
    except json.JSONDecodeError:
        logging.error(f"Invalid JSON format in configuration file: {config_file_path}")
        return {}
    except Exception as e:
        logging.exception(f"An unexpected error occurred while loading config: {e}")
        return {}


def format_date(date_string, input_format='%Y-%m-%d', output_format='%m/%d/%Y'):
    """
    Formats a date string from one format to another.

    Args:
        date_string (str): The date string to format.
        input_format (str, optional): The format of the input date string.
                                       Defaults to '%Y-%m-%d'.
        output_format (str, optional): The desired output format.
                                        Defaults to '%m/%d/%Y'.

    Returns:
        str: The formatted date string. Returns None if the input is invalid.
    """
    try:
        date_object = datetime.datetime.strptime(date_string, input_format)
        return date_object.strftime(output_format)
    except ValueError:
        logging.warning(f"Invalid date format. Expected: {input_format}, Received: {date_string}")
        return None
    except TypeError:
        logging.warning("Input must be a string.")
        return None
    except Exception as e:
        logging.exception(f"An unexpected error occurred while formatting date: {e}")
        return None


def create_directory_if_not_exists(directory_path):
    """
    Creates a directory if it does not already exist.

    Args:
        directory_path (str): The path to the directory to create.

    Returns:
        bool: True if the directory was created or already exists, False otherwise.
    """
    try:
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            logging.info(f"Directory created: {directory_path}")
        return True
    except OSError as e:
        logging.error(f"Error creating directory {directory_path}: {e}")
        return False


def validate_email(email):
    """
    Simple email validation.  Not comprehensive, but catches common errors.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email appears valid, False otherwise.
    """
    if not isinstance(email, str):
        return False

    if "@" not in email:
        return False

    if "." not in email.split("@")[-1]:
        return False

    return True