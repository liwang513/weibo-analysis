#encoding=utf-8
import codecs
import re
import math
import os.path
import xlrd
from os import walk

def read_ctgr(name):
    file = codecs.open('/Users/liwang/Desktop/weibo/ctgr_vector/%s.txt'%name, 'r','utf-8')
    content_list = [line.strip().split(':') for line in file]
    return content_list
    
def read_file(name):
    file = codecs.open('/Users/liwang/Desktop/weibo/vector/%s.txt'%name, 'r','utf-8')
    content_list = [line.strip().split(':') for line in file]
    return content_list

def read_ctgr_names(name):
    file = codecs.open('/Users/liwang/Desktop/weibo/ctgr_name/%s.txt'%name, 'r','utf-8')
    content_list = [line.strip() for line in file]
    return content_list
    
    
workbook = xlrd.open_workbook('/Users/liwang/Desktop/weibo/热门蓝V分类.xls')

worksheet = workbook.sheet_by_name(u'sheet1 - \u8868\u683c 1 - \u8868\u683c 1')

num_rows = worksheet.nrows - 1
num_cols = worksheet.ncols - 1


def count_distance(file_name):
    
    result_box = []
    
    store = read_file(file_name)
    point_location = [float(i[1]) for i in store]
    
    for i in range(1, num_cols + 1):
        category = worksheet.cell_value(0,i)
        content_list = read_ctgr(category)
        ctgr_location = [float(i[1]) for i in content_list]
        
        sum_square = 0
        for i in range(5000):
            sum_square = sum_square + math.pow(point_location[i] - ctgr_location[i],2) 
        distance = math.sqrt(sum_square)
        
        result_box.append([category,distance])
        
    return sorted(result_box, key=lambda item: float(item[1]))

def app_distance(vector):
    
    result_box = []
    
    point_location = [float(i[1]) for i in vector]
    
    for i in range(1,num_cols + 1):
        category = worksheet.cell_value(0,i)
        content_list = read_ctgr(category)
        ctgr_location = [float(i[1]) for i in content_list]
        
        sum_square = 0
        for i in range(5000):
            sum_square = sum_square + math.pow(point_location[i] - ctgr_location[i],2) 
        distance = math.sqrt(sum_square)
        
        result_box.append([category,distance])
        
    return sorted(result_box, key=lambda item: float(item[1]))

def main():
    count_num = 0
    good_num = 0

    for i in range(1, 2):
        count_num_ctgr = 0
        good_num_ctgr = 0
        category = worksheet.cell_value(0,i)
        print category
        name_list = read_ctgr_names(category)
        for name in name_list:
            if os.path.isfile("/Users/liwang/Desktop/weibo/vector/%s.txt"%name):
                count_num_ctgr = count_num_ctgr + 1
                count_num = count_num + 1
                result = count_distance(name)[0][0]
                print name,result
                if (result == category):
                    good_num_ctgr = good_num_ctgr + 1
                    good_num = good_num + 1
        print good_num_ctgr, count_num_ctgr, round(float(good_num_ctgr)/count_num_ctgr, 2)
    
        print good_num, count_num, round(float(good_num)/count_num, 2)
        
#main()
for i in count_distance('最体育'):
    print i[0],i[1]
                
    