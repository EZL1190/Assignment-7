import sys
import webget 
import csv_data_conversion as cdc
import tasks

url = 'http://wfs-kbhkort.kk.dk/k101/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=k101:p_pladser&outputFormat=csv&SRSNAME=EPSG:4326'
url2 = 'https://data.kk.dk/dataset/e734af29-4e40-4754-9cce-789a7513dd8a/resource/bd5b19ee-cedd-4b69-9272-532a1bce1eee/download/indkomstbruttohustypev.csv'

file_name = webget.download(url)
data = cdc.get_data_set(file_name)
file_name2 = webget.download(url2)
data2 = cdc.get_data_set2(file_name2)

# print(tasks.task1(data))
# #---
# print(tasks.task2(data))
# #---
# tasks.task3(data)

#tasks.task4(data, data2)

tasks.taskt5(data, data2)


