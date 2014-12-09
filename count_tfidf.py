#encoding=utf-8
import codecs
import re
import math
import os.path
from os import walk

def read_tf():
    file = codecs.open('/Users/liwang/Desktop/copy.txt', 'r','utf-8')
    content_list = [line.strip().split(':') for line in file]
    return content_list
    
def read_idf():
    file = codecs.open('/Users/liwang/Desktop/count_df.txt', 'r','utf-8')
    content_list = [line.strip().split(':') for line in file]
    return content_list

total_term_num = 6574975
total_weibo_num = 425579

tf_items = read_tf()
idf_items = read_idf()
 
def tf_idf(n):
    tf_item = tf_items[n]
    idf_item = idf_items[n]
    
    keyword_1 = tf_item[0]
    keyword_2 = idf_item[0]
    tf_num = int(tf_item[1])
    idf_num = int(idf_item[1])
    
    tf = float(tf_num)/total_term_num
    idf = math.log(float(1 + total_weibo_num)/(1 + idf_num))
    tf_idf = tf * idf
    return tf_idf
    
def sort_data(store):
    return sorted(store, key=lambda item: -item[1])

def main():
    file = codecs.open('/Users/liwang/Desktop/record_tfidf.txt', 'w+','utf-8')
    store = []
    
    for i in range(0,len(tf_items)):
        keyword = tf_items[i][0]
        tfidf = tf_idf(i)
        store.append([keyword,tfidf])
    
    sort_items = sort_data(store)
    for i in sort_items:
        file.write(i[0]+':'+str(i[1])+'\n')
    
    