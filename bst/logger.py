import sys
import os
import time
from loguru import logger as log


def setup_logger(log_option: int = 0,
                 console_log_level: str = "INFO",
                 file_log_level: str = "DEBUG",
                 colorize: bool = True) -> None:
    """
    Adds necessary handlers in root logger
    :param log_option:
        0: No logging
        1: On screen logs
        2: 1 + File logging to logs/latest.log
        3: 2 + File logging to logs/<timestamp>.log
    :param console_log_level: The lowest severity level to be logged to console-logs
    :param file_log_level: The lowest severity level to be logged to file-logs
    :param colorize: Bool
    :return: None
    """
    log.remove()  # Remove any existing handlers

    console_format = "<level>{level: <8} {message}</level>"
    file_format = "{time:MMM-DD HH:mm:ss} {level:<8} {name}:{function}():{line} {message}"

    if log_option >= 1:
        log.add(sys.stdout, format=console_format, colorize=colorize, level=console_log_level, diagnose=False)

    repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # Repository path
    log_dir = os.path.join(repo_dir, 'logs')
    os.makedirs(log_dir, exist_ok=True)

    if log_option >= 2:
        log_file = os.path.join(log_dir, "latest.log")  # Latest log file for easy access
        log.add(log_file, format=file_format, level=file_log_level, diagnose=False)
        log.debug('Dumping logs to file: {:s}'.format(log_file))

    if log_option >= 3:
        timestamp = time.strftime('%Y.%m.%d_%H.%M.%S')
        log_file = os.path.join(log_dir, timestamp + ".log")  # Storing logs for archival purposes
        log.add(log_file, format=file_format, level=file_log_level, diagnose=False)
        log.debug('Dumping logs to file: {:s}'.format(log_file))

    return


def get_logger():
    """
    Returns logger instance
    :return:
    """
    return log



