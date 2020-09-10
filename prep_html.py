import json
import shutil
import os
from os import path
from inspect import getsourcefile



PATH_TO_SOURCE_SITE = path.dirname(path.abspath(getsourcefile(lambda:0))) + '\\source\\'
PATH_TO_PUBLIC = path.dirname(path.abspath(getsourcefile(lambda:0))) + '\\public'
IGNORE_DIRS = ['public\\css', 'public\\js']




def load_config():
    pass

def remake_dir_public():
    try:
        shutil.rmtree('public')
        shutil.copytree(PATH_TO_SOURCE_SITE, PATH_TO_PUBLIC)
        shutil.rmtree('public/html_blocks')
    except:
        pass

def get_content_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def set_content_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)




if __name__ == "__main__":

    load_config()

    remake_dir_public()

    blocks = os.listdir('source/html_blocks')

    for branch in os.walk('public'):
        if branch[0] in IGNORE_DIRS: continue

        for file_name in branch[2]:
            file_path = branch[0] + '\\' + file_name

            content_file = get_content_from_file(file_path)

            for block in blocks:
                content_file = content_file.replace('%%' + block, get_content_from_file('source/html_blocks/' + block))

            set_content_to_file(file_path, content_file)