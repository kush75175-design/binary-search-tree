# Standard library imports
import argparse
from pathlib import Path


# User defined imports
from bst.logger import setup_logger, get_logger
from bst.bst_simple import BinarySearchTree

log = get_logger()


def _parse_arguments() -> argparse.Namespace:
    """ Parses command line arguments """
    parser = argparse.ArgumentParser()
    parser.add_argument("-j", "--job", required=True, type=str,
                        help="Path to input .txt file containing the test job")

    args = parser.parse_args()
    return args


def main():
    """ Main entry point function of this repository """
    log.info(f"Starting the application...")

    args = _parse_arguments()  # Parse command line arguments
    path_job: Path = Path(args.job)  # Path to input .txt job file
    assert path_job.is_file(), f"Input job file does not exist: {path_job}"  # Sanity check

    # Read the items from the input job .txt file
    with open(path_job, "r") as f:
        lines = f.readlines()
        log.debug(f"Parsed {len(lines):,d} lines from input job file")

    tree = BinarySearchTree()  # Initialize a new tree class object

    # Loop over all lines in the job .txt file
    for line_idx, line in enumerate(lines):
        line = line.strip()  # Remove any leading/trailing whitespaces, just in case
        if line.startswith('#'):  # Ignore comments in the input job file
            continue

        log.info(f"Processing line {line_idx:2d}: {line}")

        # Parse the content of the line from the .txt file
        if line.startswith(("insert", "delete", "search")):
            action, value = line.split()
            value = int(value)  # Convert to integer type
        else:
            raise NotImplementedError(f"Strange line  {line_idx} in the input job file: {line}")

        # Perform action as asked by the line
        if action == "insert":
            tree.insert(value)
        elif action == "delete":
            tree.delete(value)
        elif action == "search":
            tree.search(value)
        else:
            raise NotImplementedError(f"Unsupported action: {action}")

        log.debug(tree)  # Optional: print the entire tree

    log.info(f"All done!")
    return


if __name__ == '__main__':
    setup_logger(log_option=1, console_log_level="DEBUG", colorize=True)  # Set up the logger. Do it only once.
    main()
