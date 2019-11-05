# -*- coding: utf-8 -*-
# @Time    : 2019-04-15 17:03
# @Author  : Kelly
# @Email   : 289786098@qq.com
# @File    : callPreprocession.py
# @Description:

import pandas as pd
import os

def  create_csvFile(data_dir):






   '''
   file_path = os.path.join(data_dir, 'train.csv')
    train_df = pd.read_csv(file_path, encoding='utf-8')
    train_df['C'] = train_df['A'] + train_df['B']
    
    
    #train_df = pd.read_csv('data.csv', usecols=[0, 1, 2, 3])
    train_data = []
    for index, train in enumerate(train_df.values):
        guid = 'train-%d' % index
        text_a = tokenization.convert_to_unicode(str(train[0]))
        text_b = tokenization.convert_to_unicode(str(train[1]))
        label = str(train[2])
        train_data.append(InputExample(guid=guid, text_a=text_a, text_b=text_b, label=label))

parent_teacher_data['address'] = parent_teacher_data['country']+parent_teacher_data['province']+parent_teacher_data['city']+parent_teacher_data['county']


#将DataFrame存储为csv,index表示是否显示行名，default=True
train_df.to_csv("test.csv",index=False,sep=',')
import csv

#python2可以用file替代open
with open("test.csv","w") as csvfile:
    writer = csv.writer(csvfile)

    #先写入columns_name
    writer.writerow(["index","a_name","b_name"])
    #写入多行用writerows
    writer.writerows([[0,1,3],[1,2,3],[2,3,4]])
    
    
'''

if __name__ == "__main__":
    d = ''