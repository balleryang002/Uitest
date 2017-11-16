#coding="utf-8"

import xlrd
import os

path=os.path.split(os.path.realpath(__file__))[0]+"\\..\\config\\study-old-data.xlsx"

class IOexcel():

    def readExcle(self):
        data=xlrd.open_workbook(path)
        table=data.sheet_by_index(0)
        rows=table.nrows
        list=[]
        for i in range(1,rows):
            value=table.row_values(i)
            if value :
                list.append(value)


        return list

    def toStr(self,value):
        return value.encode("utf-8")




