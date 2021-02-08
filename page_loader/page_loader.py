import os
import requests
from urllib.parse import urlparse
import re
from bs4 import BeautifulSoup


def download(page_url, output_dir):
    if is_dir_exist(output_dir):
        html_doc = read_page(page_url)

        page_file_name = make_page_file_name(page_url)
        page_file_path = make_path(page_file_name, output_dir)

        soup = BeautifulSoup(html_doc, 'html.parser')
        soup = change_img_links_and_save(soup, page_url, output_dir)

        with open(page_file_path, "w") as f:
            f.write(soup.prettify(formatter="html5"))

        return page_file_path


# test written
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


# test written
def make_dir_with_files_name(page_address):
    netloc = urlparse(page_address).netloc
    path = urlparse(page_address).path
    splitted_netloc = netloc.split('.')
    netloc_kebab_case = '-'.join(splitted_netloc)
    splitted_address = (netloc_kebab_case + path).split('/')
    dir_name = '-'.join(splitted_address) + '_files'
    return dir_name


# test written
def is_dir_exist(output_dir):
    return os.path.exists(output_dir) and os.path.isdir(output_dir)


# test written
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
    domain_with_scheme = (
            urlparse(page_url).scheme + '://' + urlparse(page_url).netloc
    )
    return domain_with_scheme + image_url_relative


# test written
def save_image(img_url, img_path):
    p = requests.get(img_url)
    with open(img_path, "wb") as out:
        out.write(p.content)


# test written
def change_img_links_and_save(soup, page_url, output_dir):
    dir_with_files_name = make_dir_with_files_name(page_url)
    dir_with_files_path = make_path(dir_with_files_name, output_dir)
    os.mkdir(dir_with_files_path)
    for image_tag in soup.find_all('img'):
        image_url_relative = image_tag.get('src')
        if len(urlparse(image_url_relative).netloc) == 0:
            img_url = make_image_url_absolut(page_url, image_url_relative)
            img_file_name = make_image_file_name(page_url, image_url_relative)
            img_path = make_path(img_file_name, dir_with_files_path)
            save_image(img_url, img_path)
            image_tag['src'] = make_path(img_file_name, dir_with_files_name)
    return soup
