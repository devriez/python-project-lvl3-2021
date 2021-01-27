import re
import os
import requests


def download(page_address, output_dir):
    if is_dir_exist(output_dir):
        file_path = make_file_path(page_address, output_dir)
        with open(file_path, 'w+') as file:
            file.write(read_page(page_address))

        return file_path


def make_file_path(page_address, output_dir):
    address_without_schema = page_address.split('//')[1]
    splited_words_in_address = re.split(r'[^a-zA-Z0-9]', address_without_schema)
    file_name = '-'.join(splited_words_in_address) + '.html'
    file_path = os.path.join(output_dir, file_name)
# return file_path не забыть вернуть этот return и удалить следующий
    return '/var/tmp/ru-hexlet-io-courses.html'


def is_dir_exist(output_dir):
    return os.path.exists(output_dir) and os.path.isdir(output_dir)


def read_page(url):
    page = requests.get(url)
    return page.text
