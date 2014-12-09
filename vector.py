#encoding=utf-8
import codecs
import re
import math
import os.path
from os import walk

def read_file(name):
    file = codecs.open('/Users/liwang/Desktop/keyword_set/%s.txt'%name, 'r','utf-8')
    content_list = [line.strip().split(':') for line in file]
    return content_list
    
def read_5000():
    file = codecs.open('/Users/liwang/Desktop/weibo/5000_keyword.txt', 'r','utf-8')
    content_list = [line.strip().split(':') for line in file]
    return content_list
    
def weibo_num(filename):
    file = codecs.open('/Users/liwang/Desktop/weibo_set/%s.txt'%filename, 'r','utf-8')
    file = file.read()
    content_list = file.split(', u')
    return len(content_list)

keywords_5000 = [i[0] for i in read_5000()]

def create_vector(name):
    store = read_file(name)
    count_weibo_num = weibo_num(name)
    vector = []
    for keyword in keywords_5000:
        match = False
        for item in store:
            if (keyword == item[0]):
                vector.append([keyword,float(int(item[1]))/count_weibo_num])
                match = True
                break
        if (match == False):
            vector.append([keyword,0])
    return vector

def main():
    
    f = []
    for (dirpath, dirnames, filenames) in walk('/Users/liwang/Desktop/weibo_set'):
        f.extend(filenames)
        
    names = []
    for i in range(1,len(f)):
        names.append(f[i].decode('utf-8').rstrip('.txt'))
    

    for name in names:
        file = codecs.open('/Users/liwang/Desktop/vector/%s.txt'%name, 'w+','utf-8')
        vector = create_vector(name)
        for item in vector:
            file.write(item[0]+':'+str(item[1])+'\n')

                
def app_vector(store, weibo_num):
    vector = []
    for keyword in keywords_5000:
        match = False
        for item in store:
            if (keyword == item[0]):
                vector.append([keyword,float(int(item[1]))/weibo_num])
                match = True
                break
        if (match == False):
            vector.append([keyword,0])
    return vector