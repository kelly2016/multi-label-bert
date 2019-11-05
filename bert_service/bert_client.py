# -*- coding: utf-8 -*-
# @Time    : 2019-04-24 11:49
# @Author  : Kelly
# @Email   : 289786098@qq.com
# @File    : bert_client.py
# @Description:

from bert_serving.client import BertClient
bc = BertClient(ip='192.168.100.19',check_version=False,check_length=False)#, port=5555
vec = bc.encode(['机器人说：你好'])
print(vec)