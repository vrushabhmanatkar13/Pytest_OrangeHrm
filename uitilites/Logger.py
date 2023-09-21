import inspect
import logging
import os.path

import allure


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


@allure.step
def Step(step):
    pass
