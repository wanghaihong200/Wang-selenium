# coding:utf-8
import xlrd

#获取第一张表中单个单元格数据
def getExcel(rowValue,colValue,file_name='D:\\test\\happyHiiso3\\data\\business_login.xlsx'):
    '''
    :param rowValue: 表格的行
    :param colValue: 表格的列
    :param file_name: excel文件
    :return:
    '''
    #创建book
    book = xlrd.open_workbook(file_name)
    #获取sheet对象,第一张表
    sheet = book.sheet_by_index(0)
    #获取sheet对象中的数据
    return sheet.cell_value(rowValue,colValue)

#获取第一张表所有单元格数据
def getDdtExcel(file_name="D:\\test\\happyHiiso3\\data\\business_login.xlsx"):
    rows = []
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_index(0)
    # print(sheet.ncols,sheet.nrows)
    for row in range(1,sheet.nrows):
        rows.append(list(sheet.row_values(row,start_colx=0,end_colx=sheet.ncols)))
    return rows

if __name__ == "__main__":
    #测试代码，获取0行1列的单元格数据
    print(getExcel(0,1))
    #测试代码，获取第1张表的所有数据
    print(getDdtExcel())