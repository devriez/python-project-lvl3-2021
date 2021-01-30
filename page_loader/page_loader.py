import os
import requests
from urllib.parse import urlparse
import re


def download(page_address, output_dir):
#     if is_dir_exist(output_dir):
#         file_path = make_file_path(page_address, output_dir)
#         file_html = read_page(page_address)
#
#         # with open(file_path, 'w+') as file:
#         #     file.write(read_page(page_address))
#
         return file_path


# тест написан
def make_page_file_name(page_address):
    netloc = urlparse(page_address).netloc
    path = urlparse(page_address).path
    splitted_netloc = netloc.split('.')
    netloc_kebab_case = '-'.join(splitted_netloc)
    splitted_address = (netloc_kebab_case + path).split('/')
    page_file_name = '-'.join(splitted_address) + '.html'
    return page_file_name


def make_path(name, root_dir):
    path = os.path.join(root_dir, name)
    return path


# тест написан
def make_name_dir_with_images(page_file_name):
    path_without_ext, _ = os.path.splitext(page_file_name)
    return path_without_ext + '_files'


# тест написан
def is_dir_exist(output_dir):
    return os.path.exists(output_dir) and os.path.isdir(output_dir)


# тест написан
def make_kebab_case_name(name):
    if name[0] == '/':
        name = name[1:]
    splitted_name = re.split(r'[./]', name)
    kebab_case_name = '-'.join(splitted_name)
    return kebab_case_name


def make_domain_kebab_case_name(url):
    domain_name = urlparse(url).netloc
    return make_kebab_case_name(domain_name)


def read_page(url):
    page = requests.get(url)
    return page.text


# test written
def make_image_file_name(page_address, image_path):
    domain_kebab_case = make_domain_kebab_case_name(page_address)
    image_path_without_ext, extension = os.path.splitext(image_path)
    image_path_kebab_case = make_kebab_case_name(image_path_without_ext)
    image_name = domain_kebab_case + '-' + image_path_kebab_case + extension
    return image_name


# test written
def make_image_url_absolut(page_url, image_url_relative):
    domain_with_scheme = urlparse(page_url).scheme + '://' + urlparse(page_url).netloc
    return (domain_with_scheme + image_url_relative)
