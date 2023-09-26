import os.path

import openpyxl
import pytest


# install openpyxl package


def load_excel_file(excel_path):
    global workbook
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    workbook = openpyxl.load_workbook(path + excel_path)
    print("Work Book loaded")
    return workbook


def get_data(sheet_name, testcase_name):
    sheet = workbook[sheet_name]
    row = sheet.max_row
    col = sheet.max_column
    current_testcase = ""
    data_list = []
    for r in range(1, row + 1):
        testcase = sheet.cell(r, 1).value
        if testcase == testcase_name:
            current_testcase = sheet.cell(r, 1).value  # Get the name of the new test case
        elif current_testcase and testcase == "***":
            break
        elif current_testcase and testcase is not None:
            row_list = []
            for c in range(1, col + 1):
                value = sheet.cell(r + 1, c).value
                if value is None or value == "***":
                    break
                row_list.append(value)
            if row_list:
                data_list.append(row_list)
    return data_list



