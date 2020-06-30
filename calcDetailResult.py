import openpyxl
from Model import PriceItem

def calcSummaryResult(price_file):
    wb = openpyxl.load_workbook(price_file)
    sheet = wb['检测对账总明细表']
    result = list()
    return result
