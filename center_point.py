#encoding=utf-8
import codecs
import re
import math
import os.path
import xlrd
from os import walk

def read_5000():
    file = codecs.open('/Users/liwang/Desktop/weibo/5000_keyword.txt', 'r','utf-8')
    content_list = [line.strip().split(':') for line in file]
    return content_list
    
keywords_5000 = [i[0] for i in read_5000()]

def read_ctgr(name):
    file = codecs.open('/Users/liwang/Desktop/weibo/ctgr_name/%s.txt'%name, 'r','utf-8')
    content_list = [line.strip() for line in file]
    return content_list
    
def read_file(name):
    file = codecs.open('/Users/liwang/Desktop/weibo/vector/%s.txt'%name, 'r','utf-8')
    content_list = [line.strip().split(':') for line in file]
    return content_list

def avg_vector(category):
    name_list = read_ctgr(category)
    names_num = len(name_list)
    sum_all = [0 for i in range(5000)]
    for name in name_list:
        if os.path.isfile("/Users/liwang/Desktop/weibo/vector/%s.txt"%name):
            store = read_file(name)
        val_list = [float(i[1]) for i in store]
        sum_all = [(sum_all[i] + val_list[i]) for i in range(5000)]
    final_val_list = [round(sum_all[i]/names_num, 4) for i in range(5000)]
    file = codecs.open('/Users/liwang/Desktop/weibo/ctgr_vector/%s.txt'%category, 'w+','utf-8')
    for i in range(5000):
        file.write(keywords_5000[i]+':'+str(final_val_list[i])+'\n')

def main():
    workbook = xlrd.open_workbook('/Users/liwang/Desktop/weibo/热门蓝V分类.xls')
    worksheet = workbook.sheet_by_name(u'sheet1 - \u8868\u683c 1 - \u8868\u683c 1')

    num_rows = worksheet.nrows - 1
    num_cols = worksheet.ncols - 1

    for i in range(1,num_cols+1):
        category = worksheet.cell_value(0,i)
        avg_vector(category)
        
main()