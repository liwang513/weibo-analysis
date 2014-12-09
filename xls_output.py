#encoding=utf-8
import codecs
import re
import math
import os.path
import xlrd
from os import walk

workbook = xlrd.open_workbook('/Users/liwang/Desktop/热门蓝V分类.xls')
worksheet = workbook.sheet_by_name(u'sheet1 - \u8868\u683c 1')

num_rows = worksheet.nrows - 1
num_cols = worksheet.ncols - 1


for i in range(1,num_cols+1):
    category = worksheet.cell_value(0,i)
    file = codecs.open('/Users/liwang/Desktop/ctgr_vector/%s.txt'%category, 'w+','utf-8')
    for j in range(1,num_rows+1):
        name = worksheet.cell_value(j,i)
        file.write(name+'\n')