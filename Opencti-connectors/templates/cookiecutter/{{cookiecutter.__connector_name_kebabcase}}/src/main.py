import traceback

from {{cookiecutter.__connector_type_snakecase}}_connector import Connector{{cookiecutter.__connector_name_camelcase}}

if __name__ == "__main__":
    """
    Entry point of the script

    - traceback.print_exc(): This function prints the traceback of the exception to the standard error (stderr).
    The traceback includes information about the point in the program where the exception occurred,
    which is very useful for debugging purposes.
    - exit(1): effective way to terminate a Python program when an error is encountered.
    It signals to the operating system and any calling processes that the program did not complete successfully.
    """
    try:
        connector = Connector{{cookiecutter.__connector_name_camelcase}}()
        connector.run()
    except Exception:
        traceback.print_exc()
        exit(1)
