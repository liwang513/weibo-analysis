#encoding=utf-8
import codecs
import re
import os.path
from os import walk

names_file = codecs.open('/Users/liwang/Desktop/merge_names.txt', 'r','utf-8')
names = [line.strip() for line in names_file]

def read_file(filename):
    file = codecs.open('/Users/liwang/Desktop/merge_8/%s.txt'%filename, 'r','utf-8')
    content_list = [line.strip().split(':') for line in file]
    return content_list

def merge(a,b):
    list_a = read_file(a)
    list_b = read_file(b)
    print len(list_a),len(list_b)
    list_a_copy = list_a
    list_b_copy = list_b
    file = codecs.open('/Users/liwang/Desktop/merge_9/%s.txt'%a, 'w+','utf-8')
    for item_a in list_a_copy:
        for item_b in list_b_copy:
            if (item_a[0] == item_b[0]):
                file.write(item_a[0]+':'+str(int(item_a[1])+int(item_b[1]))+'\n')
                list_a.remove(item_a)
                list_b.remove(item_b)
                break
    print len(list_a),len(list_b)
    for item in list_a:
        file.write(item[0]+':'+str(item[1])+'\n')
    for item in list_b:
        file.write(item[0]+':'+str(item[1])+'\n')

def cut_less_4(a):
    list_a = read_file(a)
    print len(list_a)
    list_a_copy = list_a
    file = codecs.open('/Users/liwang/Desktop/cut_less_4/%s.txt'%a, 'w+','utf-8')
    for item_a in list_a_copy:
        if (int(item_a[1]) > 3):
            file.write(item_a[0]+':'+str((item_a[1]))+'\n')

def main():
    for i in range(0,len(names),2):
        merge(names[i],names[i+1])




            
                