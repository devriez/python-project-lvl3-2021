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
    splitted_address = re.split(r'[^a-zA-Z0-9]', address_without_schema)
    page_name = '-'.join(splitted_address) + '.html'
    file_path = os.path.join(output_dir, page_name)
    return file_path
#    return '/var/tmp/ru-hexlet-io-courses.html'


def is_dir_exist(output_dir):
    return os.path.exists(output_dir) and os.path.isdir(output_dir)


def read_page(url):
    page = requests.get(url)
    return page.text


def make_path_to_dir_with_images(file_path):
    path_without_ext, _ = os.path.splitext(file_path)
    return path_without_ext + '_files'


def make_path_to_image(page_address, image_path):
    address_without_schema = page_address.split('//')[1]
    domain = address_without_schema.split('/')[0]
    splitted_domain = re.split(r'[^a-zA-Z0-9]', domain)
    image_path_without_ext, extension = os.path.splitext(image_path)
    print('image_path_without_ext', image_path_without_ext)
    splitted_image_path = re.split(r'[^a-zA-Z0-9]', image_path_without_ext)
    print('splitted_image_path', splitted_image_path)
    path_to_image = ('-'.join(splitted_domain) + '-'.join(splitted_image_path) + extension)
    return path_to_image
