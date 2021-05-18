# encoding: utf-8

import xlrd

class readExcel(object):
    def __init__(self, path):
        self.path = path

    # @property
    def getSheet(self,sheet_index):
        # 获取索引
        xl = xlrd.open_workbook(self.path)
        sheet = xl.sheet_by_index(sheet_index)
        return sheet

    # @property
    def getRows(self,sheet_index):
        # 获取行数
        rows = self.getSheet(sheet_index).nrows
        return rows

    # @property
    def getCol(self,sheet_index):
        # 获取列数
        col = self.getSheet(sheet_index).ncols
        return col

    # 以下是分别获取每一列的数值
    def getName(self, column_index,sheet_index):

        if column_index <= self.getCol(sheet_index):
            ColumnName = []
            for i in range(1, self.getRows(sheet_index)):
                ColumnName.append(self.getSheet(sheet_index).cell_value(i, column_index))
            return ColumnName
        else:
            print("输入的column不合法！")

    def getRowList(self, row_index,sheet_index):
        if row_index <= self.getRows(sheet_index):
            RowName = []
            RowName.append(self.getSheet(sheet_index).row_values(row_index))
            return RowName
        else:
            print("输入的row不合法！")

    def excel_table(self,sheet_index):
        u"""装载list"""
        # 获取行数
        Trows = self.getRows(sheet_index)
        # 获取列数
        Tcols = self.getCol(sheet_index)
        # print('行数：',Trows)
        # print('列数：',Tcols)

        # 获取第一行
        Tcolnames = self.getRowList(0,sheet_index)
        header=[]
        for rownum in range(0, Tcols):
            row_data=Tcolnames[0][rownum]
            header.append(row_data)

        all_data = []
        for rownumber in range(1,Trows):
            row_data = self.getRowList(rownumber,sheet_index)
            # print(row_data)
            for i in range(0, Tcols):
                all_data.append(row_data[0][i])
        # print('all_data:',all_data)

        listener=[]
        j = 0
        for i in range(1, Trows):
            app={}
            for x in range(0, Tcols):
                app[header[x]]=all_data[j]
                j=j+1
            listener.append(app)
        # print(listener)
        return listener

if __name__ == '__main__':
    file_path = "TestCase.xlsx"
    excel_data = readExcel(file_path).excel_table(0)
    print(excel_data)