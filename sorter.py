import os
import shutil
import time
import argparse
from concurrent.futures import ThreadPoolExecutor


def files_to_dir(file_name: str):
    data_seconds = os.path.getmtime(f'1/{file_name}')
    data = f'{time.ctime(data_seconds)[4:11]}' \
               f'{time.ctime(data_seconds)[-4:]}'
    try:
        os.mkdir(f'1/{data}')
        shutil.move(f'1/{file_name}', f'1/{data}/')
    except FileExistsError:
        shutil.move(f'1/{file_name}', f'1/{data}/')


def sorter():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--extension", type=str, help="write a file extension")
    args = parser.parse_args()
    for file in os.listdir('1/'):
        if file.find(args.extension) != -1:
            with ThreadPoolExecutor() as executor:
                executor.submit(files_to_dir, file)


sorter()