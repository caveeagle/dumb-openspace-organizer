
def read_names_from_file(filename: str) -> list:
    """
    Read names from a text file, one name per line.

    Args:
        filename (str): Path to the input file.

    Returns:
        list of str: List of names read from the file. Empty lines are ignored.

    Notes:
        - Strips leading/trailing whitespace from each line.
        - Handles common file errors:
            * FileNotFoundError: prints a message if the file does not exist.
            * PermissionError: prints a message if access is denied.
            * OSError: prints a message for other OS-related file errors.
    """

    lines = []

    try:

        with open(filename, 'r') as my_file:

            lines = [line.strip() for line in my_file
                     if line.strip()]  # Exclude empty strings

    except FileNotFoundError:
        print("File not found:", filename)
    except PermissionError:
        print("Permission error:", filename)
    except OSError as e:
        print("General OS file error:", e)
    return lines

