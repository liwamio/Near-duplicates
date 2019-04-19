
# coding: utf-8

# In[ ]:


from nltk.tokenize import RegexpTokenizer
import pandas as pd
import json

file_dir = 'DMT4Bas/hw_1/part_2/dataset/261K_lyrics_from_MetroLyrics.csv'

df = pd.read_csv(file_dir)
lyrics = df['lyrics'].tolist()

vocabulary_set = dict() 
tokenizer = RegexpTokenizer(r'\w+')

number_of_shingles = 3
shingled_lyric = dict()
counter = 0

#Shingle

for l in range(len(lyrics)):
    token_lyrics = tokenizer.tokenize(ly[l])
    voc = []    
    for i in range(len(token_lyrics)): 
        temp = ' '.join([token_lyrics[j] for j in range(i, i + number_of_shingles) if j < len(token_lyrics)])
        vocabulary_set[temp] = i
        voc.append(temp)           

    shingled_lyric[l] = voc

#index 
shingled_dic = dict()

for i in shingled_lyric: 
    for v in shingled_lyric[i]:         
        try: 
            shingled_dic[i].append(vocabulary_set[v])
        except: 
            shingled_dic[i] = [vocabulary_set[v]]

pd.DataFrame.from_dict(shingled_dic, columns = ['Id', 'Element Id'], orient= 'index').to_csv('dmt4bas/hw_1/part_2/input_1.tsv', index = False, sep = '\t')

