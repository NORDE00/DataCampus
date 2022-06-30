'''
언어 구사능력이 높을수록, functional word에 강조를 주지 않는 경향이 있다.
강조 할 수록 그 단어를 길게 발음하므로, 이를 참고하여 세 Speaker의 fluency를 rank해보자. 
'''

import os #file_list 만들기 위해 import

# 파일 여는 함수
def fileopen(f):
    file = open(f,'r')
    global data # data변수를 함수 외부에서 사용하기 위해, global 선언
    data = file.read()

# word의 duration 도출 함수
def duration (word, data_list):
    for d in data_list:
        if d == '"'+word+'"':
            i = data_list.index(d)
            dur = float(data_list[i-3])-float(data_list[i-6])
    return dur

def file_lister(p):
    file_list = os.listdir(p) #현재 경로에서의 file list를 file_list에 저장
    file_list_textgrid = [file for file in file_list if file.endswith(".TextGrid")]
    file_list = file_list_textgrid
    return file_list

# file_list와 sentance 받아 출력하는 함수
def processPrint (file_list, sen):
    count = 1
    for filename in file_list:
        fileopen(filename)
        data_list = data.split()
        total = 0
        print('Speaker #', count)
        for word in sen.split():
            dur = duration(word, data_list)
            print("duration of word", word, round(dur,3))
            total = total + dur
        print("total= " , round(total,3), '\n')
        count = count + 1

sen = "push the button"
path = r'C:\Users\sangw\Desktop\DataCampus\Introduction_to_Language_Technology'

os.chdir(path)
file_list = file_lister(path)
processPrint(file_list, sen)