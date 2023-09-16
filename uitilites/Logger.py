import inspect
import logging
import os.path


def setup_logging(file_path):
    global file
    file = logging.FileHandler(file_path)
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    file.setFormatter(formatter)


def get_logger(testcase_name):
    log = logging.getLogger(testcase_name)
    log.addHandler(file)
    log.setLevel(logging.INFO)
    return log


# def custom_logger():
#     log_name = inspect.stack()[1][3]
#     logger = logging.getLogger(log_name)
#     logger.setLevel(logging.DEBUG)
#     file_handler = logging.FileHandler(
#         os.path.normpath(os.getcwd() + os.sep).rstrip("/uitilites/") + "/Report/test_reports.log", mode='a')
#     print(file_handler)
#     file_handler.setLevel(logging.DEBUG)
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s',
#                                   datefmt='%d/%m/%y %I:%M:%S %p %A')
#     file_handler.setFormatter(formatter)
#     logger.addHandler(file_handler)
#     return logger
