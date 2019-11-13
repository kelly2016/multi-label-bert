# -*- coding: utf-8 -*-
# @Time    : 2019-11-07 12:05
# @Author  : Kelly
# @Email   : 289786098@qq.com
# @File    : createFinalResult.py
# @Description:将多分类的文件生成最终用户需要的结果数据

import os
import pandas as pd
import tensorflow as tf
import json
def deal(src_file,output_file):
    num_written_lines = 0
    with tf.gfile.GFile(output_file, "w") as writer:
        src_df = pd.read_csv(src_file, encoding='utf-8',header=None,sep = '\t')
        orLabels = ['location_traffic_convenience', 'location_distance_from_business_district', 'location_easy_to_find',
                    'service_wait_time', 'service_waiters_attitude', 'service_parking_convenience',
                    'service_serving_speed', 'price_level', 'price_cost_effective', 'price_discount',
                    'environment_decoration', 'environment_noise', 'environment_space', 'environment_cleaness',
                    'dish_portion', 'dish_taste', 'dish_look', 'dish_recommendation', 'others_overall_experience',
                    'others_willing_to_consume_again']

        title_line = "id\t" + "content\t" + "\t".join(label for label in orLabels) + "\n"
        writer.write(title_line)
        for j, values in enumerate(src_df.values):
            newValues = []
            for index  in range(2,len(values),4):
                maxValue = values[index]
                maxIndex = index
                for (i, value) in enumerate(values[index:index+4]):
                    v = float(value)
                    if v >= maxValue:
                        maxValue = v
                        maxIndex = i
                if maxIndex == 0:
                    newValues.append('1')
                elif maxIndex ==1:
                    newValues.append('0')
                elif maxIndex == 2:
                    newValues.append('-1')
                elif maxIndex ==3:
                    newValues.append('-2')
            if j >= 630:
                s = str(values[1])
                #print(s)
                #print('----------')
                #s1 = s.replace('\n','').replace('\r',' ')
                #print(s1)
                bug = 0
            output_line = str(values[0])+"\t"+str(values[1]).replace('\n','').replace('\r',' ')+"\t"+"\t".join(newValue for newValue in newValues) + "\n"
            writer.write(output_line)
            num_written_lines += 1
    print('total num_written_lines =',num_written_lines)


def create_bulletsjson(src_file,output_file):
    """
    生成展示的数据文件
    [
      {"title":"location_traffic_convenience","subtitle":"% ","ranges":[150,225,300],"measures":[220,270],"markers":[250]},
      {"title":"location_distance_from_business_district","subtitle":"%","ranges":[20,25,30],"measures":[21,23],"markers":[26]},
      {"title":"location_easy_to_find","subtitle":"%", average","ranges":[350,500,600],"measures":[100,320],"markers":[550]},
         。。。
    ]
    :param src_file:
    :param output_file:
    :return:
    """
    labels = ['location_traffic_convenience', 'location_distance_from_business_district', 'location_easy_to_find',
                'service_wait_time', 'service_waiters_attitude', 'service_parking_convenience', 'service_serving_speed',
                'price_level', 'price_cost_effective', 'price_discount', 'environment_decoration', 'environment_noise',
                'environment_space', 'environment_cleaness', 'dish_portion', 'dish_taste', 'dish_look',
                'dish_recommendation', 'others_overall_experience', 'others_willing_to_consume_again']
    labelsCounter = []
    for  label in labels:
        dict = {}
        dict['title'] = label
        dict['Positive'] = 0
        dict['Neutral'] = 0
        dict['Negative'] = 0
        dict['NotMentioned'] = 0
        dict['totalCount'] = 0
        labelsCounter.append(dict)
    src_df = pd.read_csv(src_file, encoding='utf-8',header=None,sep = '\t',error_bad_lines=False)
    totalcount = len(src_df.values)
    for i, values in enumerate(src_df.values):
        if i== 0:
            continue
        bug = 0
        for j in range(2,len(values)):
            dict= labelsCounter[j - 2]

            if values[j] == '1':  # Positive
                dict['Positive'] = dict['Positive']+1
                # 总数+！
                dict['totalCount'] = dict['totalCount'] + 1
            elif values[j] == '0':  # Neutral
                dict['Neutral'] = dict['Neutral'] + 1
                # 总数+！
                dict['totalCount'] = dict['totalCount'] + 1
            elif values[j] == '-1':  # Negative
                dict['Negative'] = dict['Negative'] + 1
                # 总数+！
                dict['totalCount'] = dict['totalCount'] + 1
            elif values[j] == '-2':#NotMentioned
                dict['NotMentioned'] = dict['NotMentioned'] + 1
    bulletsValue = []
    v = ['Positive','Neutral','Negative','NotMentioned']
    v2 = ['1', '0', '-1', '-2']
    for couter  in labelsCounter:
        for  i, iv in enumerate(v):
          dict = {}
          dict['title']  =couter['title']+v2[i]
          dict['subtitle'] = '%'
          dict['ranges'] = [couter['totalCount'],totalcount]#这个大类别的总数和总评论数
          dict['measures'] = [couter[iv]]
          dict['markers'] = [couter['totalCount']]
          bulletsValue.append(dict)
    string = json.dumps(bulletsValue)
    with open(output_file,'w')as f:
          f.write(string)


if __name__ == "__main__":
    src_file ='/Users/henry/Documents/application/multi-label-bert/data/output/test_results.tsv'
    output_file = '/Users/henry/Documents/application/multi-label-bert/data/output/sentiment_analysis_test_results.tsv'
    deal(src_file, output_file)
    output_file1 = '/Users/henry/Documents/application/multi-label-bert/data/output/bullets.json'
    create_bulletsjson(output_file,output_file1)