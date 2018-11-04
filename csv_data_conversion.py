import csv
import ast
import os
import shutil

def get_data_set(file_name):
    '''We have to convert it into a "understandable format. So we have to clean it up, beucase alot of the tiles is not unicode based right.'''
    with open(file_name, encoding="utf8", errors='ignore') as f:
        reader = csv.reader(f)
        next(reader) # skip header
        data_set = []
        for row in reader:
                try:
                    # We create a single object for each row, that takes the important informations and put them into an array.
                    row_object = {}
                    # Had to decode some characters into a suitable format the computer understands, so we chose to use latin. We also put the information into suitable formats, for better performance and correct indication
                    row_object['fid'] = row[0:1][0]
                    row_object['vejkode'] = row[1:2][0]
                    row_object['vejnavn'] = row[2:3][0]
                    row_object['antal_pladser'] = int(row[3:4][0])
                    row_object['restriktion'] = row[4:5][0]
                    row_object['vejstatus'] = row[5:6][0]
                    row_object['vejside'] = row[6:7][0]
                    row_object['bydel'] = row[7:8][0]
                    row_object['p_ordning'] = row[8:9][0]
                    row_object['p_type'] = row[9:10][0]
                    row_object['rettelsedato'] = row[10:11][0]
                    row_object['oprettelsesdato'] = row[11:12][0]
                    row_object['bemaerkning'] = row[12:13][0]
                    row_object['id'] = row[13:14][0]
                    row_object['taelle_id'] = row[14:15][0]
                    row_object['startdato_midlertidigt_nedlagt'] = row[15:16][0]
                    row_object['slutdato_midlertidigt_nedlagt'] = row[16:17][0]
                    row_object['wkb_geometry'] = row[17:18][0]

                    data_set.append(row_object)
                except:
                    pass
    shutil.rmtree(os.getcwd() + '\\__pycache__')
    return data_set

def get_data_set2(file_name):
    '''We have to convert it into a "understandable format. So we have to clean it up, beucase alot of the tiles is not unicode based right.'''
    with open(file_name, encoding="utf8", errors='ignore') as f:
        reader = csv.reader(f)
        next(reader) # skip header
        data_set = []
        for row in reader:
                try:
                    # We create a single object for each row, that takes the important informations and put them into an array.
                    row_object = {}
                    # Had to decode some characters into a suitable format the computer understands, so we chose to use latin. We also put the information into suitable formats, for better performance and correct indication
                    row_object['aar'] = row[0:1][0]
                    row_object['bydel'] = row[1:2][0]
                    row_object['distriktsnavn'] = row[2:3][0].split('. ')[1]
                    row_object['hustyp'] = row[3:4][0]
                    row_object['familiegruppe'] = row[4:5][0]
                    row_object['familietype'] = row[5:6][0]
                    row_object['bruttoindkom'] = row[6:7][0]
                    row_object['indkomstkategori'] = row[7:8][0]
                    row_object['hustande'] = row[8:9][0]

                    data_set.append(row_object)
                except:
                    pass
    #shutil.rmtree(os.getcwd() + '\\__pycache__')
    return data_set