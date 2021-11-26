from openpyxl import load_workbook


def get_job_sheet(file_name):
    excel = load_workbook(r'..\\' + file_name)
    sheet = excel['脚本编排']
    return sheet
