import sys
import webget 
import csv_data_conversion as cdc
import tasks

url = 'http://wfs-kbhkort.kk.dk/k101/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=k101:p_pladser&outputFormat=csv&SRSNAME=EPSG:4326';


file_name = webget.download(url)
data = cdc.get_data_set(file_name)

task1 = tasks.task1(data)
#print(task1)

task2 = tasks.task2(data)
#print(task2)


task3 = tasks.task3(data)