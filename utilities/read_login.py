from xlrd import *

data = []

def get_test_data():
    wb = open_workbook("test_data/login.xlsx")
    sheet = wb.sheet_by_name("Sheet1")

    for i in range(2, sheet.nrows):
        rows = sheet.row_values(i)  # rows=[5,'','']
        testcase = rows[0]
        username = rows[1]
        password = rows[2]
        data.append((testcase,username,password))
    return data





# data = [(2,'wrong_user',' '),(3,'wrong_user','wrong_pass'),(4,'','secret_sauce'),(5,'','')]








# ##################################################### reading only second row   ###############################


# fetching one row of valid credentials
def get_testcase1_data():
    wb = open_workbook("test_data/login.xlsx")
    sheet = wb.sheet_by_name("Sheet1")
    rows = sheet.row_values(1)  # [1,'standard_user','secret_sauce']
    test_case = rows[0]
    un = rows[1]
    pwd = rows[2]
    return test_case,un,pwd






#################################################################################
# reading second row with zipcode
def get_row2():
    wb = open_workbook("test_data/login.xlsx")
    sheet = wb.sheet_by_name("Sheet1")
    rows = sheet.row_values(1)    #rows=[1,'standard_user','secret_sauce','keerthana','S',560032]
    return rows






























