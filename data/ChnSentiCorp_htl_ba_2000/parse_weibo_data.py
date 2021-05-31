# -*- coding: utf-8 -*-


import codecs
import re

filename = "NLPCC2014WeiboData.xml"
pos_list = ["happiness", "like", "surprise"]
neg_list = ["anger", "disgust", "sadness", "fear"]
pos_i = 1
neg_i = 1

file_content = codecs.open(filename, "r", encoding="utf8")
file_lines = file_content.readlines()

for line in file_lines:
    if "sentence" in line:
        line_split = re.split("[<>]", line)
        for pos_word in pos_list:
            if pos_word in line_split[1]:
                temp_file = codecs.open("pos\\pos."+str(pos_i)+".txt", "w", encoding="utf8")
                temp_file.writelines(line_split[2])
                pos_i += 1
                break
        for neg_word in neg_list:
            if neg_word in line_split[1]:
                temp_file = codecs.open("neg\\neg."+str(neg_i)+".txt", "w", encoding="utf8")
                temp_file.writelines(line_split[2])
                neg_i += 1
                break