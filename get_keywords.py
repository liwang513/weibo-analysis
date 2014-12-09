#encoding=utf-8
import jieba
import codecs
import os.path

############################################
#Input:file     Output:text
############################################

def get_input(filepath):
    file = codecs.open(filepath, "r","utf-8")
    return file.read()

############################################
#Input:text     Output:term frequency(TF)
############################################

def get_tokens(sentence):
    tokens = list(jieba.cut(sentence))
    #strip space
    new_tokens = map(lambda x: x.strip(), tokens)
    return new_tokens
    
def tokens_num(tokens):
    total_tokens = float(sum(1 for i in tokens))
    return total_tokens

def get_token_set(tokens):
    return set(tokens)
    
def count_each_token(tokens):
    token_set = get_token_set(tokens)
    store = []
    for element in token_set:
        count = tokens.count(element)
        store.append([element, count])
    return store

############################################
#Input:text     Output:corpus
############################################
    

    
def sort_data(store):
    return sorted(store, key=lambda item: -item[1])
    
def remove_stop_words(store,stopwords):
    new_store = []
    
    def should_stop(word,stopwords):
        for ele in stopwords:
            if (word == ele or word == u''):
                return True
        return False
    
    for item in store:
        if not should_stop(item[0],stopwords):
            new_store.append(item)
    return new_store    
            

############################################
#Input:text     Output:top n keywords
############################################

def top_n_keywords(store,num):
    new_store = []
    count = 0
    while (count < num):
        new_store.append(store[count])
        count = count + 1
    return new_store    
    
############################################
#Main Function
############################################

def main(name):
    
    #Initial stopwords
    stopword_file = codecs.open("/Users/liwang/Desktop/weibo/stopwords.txt", "r","utf-8")
    stopwords = [line.strip() for line in stopword_file]

    #Initial input_file content
    text = get_input("/Users/liwang/Desktop/weibo_set/%s.txt"%name)
    
    #Get corpus
    tokens = get_tokens(text)
    #print tokens_num(tokens)
    token_set = get_token_set(tokens)
    store = count_each_token(tokens)
    check_stop = remove_stop_words(store,stopwords)
    sorted_store = sort_data(check_stop)
        
    #select top-n keywords
    keywords = top_n_keywords(sorted_store,5)
    return sorted_store

def record_keywords():
    names_file = codecs.open('/Users/liwang/Desktop/names.txt', 'r','utf-8')
    names = [line.strip() for line in names_file]

    for name in names:
        if os.path.isfile("/Users/liwang/Desktop/weibo_set/%s.txt"%name):
            file = codecs.open('/Users/liwang/Desktop/keyword_set/%s.txt'%name, 'w+','utf-8')
            keywords = main(name)
            for i in keywords:
                file.write(i[0]+':'+str(i[1])+'\n')