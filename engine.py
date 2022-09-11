import datetime
import math
import os
from datetime import *
import re
from pathlib import Path
import time

# loop through the path
path = 'C:\\Users\\otayo\\PycharmProjects\\pythonProject\\Serial_Search_Engine\\My_Big_Directory'
my_pattern = r'[N]+[\w{3}]+[-]+[\d{5}]'
today = date.today()
numbers_found = []
files_found = []

start = time.time()


def find_number(file, pattern):
    this_file = open(file, 'r')
    text = this_file.read()

    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        return ''


def create_list():
    for folder, subfolder, file in os.walk(path):
        for a in file:

            result = find_number(Path(folder, a), my_pattern)
            if result != '':
                numbers_found.append(result.group())
                files_found.append(a.title())


def show_all():
    index = 0
    print('-' * 50)
    print(f'Date of Search: {today}')
    print('\n')
    print('FILE\t\t\tSERIAL NUMBER')
    print('----\t\t\t-------------')

    for a in files_found:
        print(f'{a}\t{numbers_found[index]}')
        index += 1
    print('\n')
    print(f'Numbers found: {len(numbers_found)}')
    end = time.time()
    duration = end - start
    print(f'Duration of the search: {math.ceil(duration)}')
    print('-' * 50)


create_list()
show_all()
