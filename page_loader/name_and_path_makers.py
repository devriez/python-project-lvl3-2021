import os
import re
from urllib.parse import urlparse


def make_page_file_name(url):
    '''
    Make file name from url
    :param url:
    :return: file name
    '''
    netloc = urlparse(url).netloc
    path = urlparse(url).path
    splitted_netloc = netloc.split('.')
    netloc_kebab_case = '-'.join(splitted_netloc)
    splitted_address = (netloc_kebab_case + path).split('/')
    page_file_name = '-'.join(splitted_address) + '.html'
    return page_file_name


def make_path(name, root_dir):
    path = os.path.join(root_dir, name)
    return path


def make_dir_with_files_name(page_address):
    '''
    Make name of directory. where to save sources from page
    :param
        page_address: url of page with links to sources
    :return: directory name
    '''
    netloc = urlparse(page_address).netloc
    path = urlparse(page_address).path
    splitted_netloc = netloc.split('.')
    netloc_kebab_case = '-'.join(splitted_netloc)
    splitted_address = (netloc_kebab_case + path).split('/')
    dir_name = '-'.join(splitted_address) + '_files'
    return dir_name


def make_kebab_case_name(name):
    '''
    Replace '.' and '/' by '-'
    :param name
    :return: modified name
    '''
    if name[0] == '/':
        name = name[1:]
    splitted_name = re.split(r'[./]', name)
    kebab_case_name = '-'.join(splitted_name)
    return kebab_case_name


def make_domain_kebab_case_name(url):
    domain_name = urlparse(url).netloc
    return make_kebab_case_name(domain_name)


def make_file_name(page_url, image_path):
    domain_kebab_case = make_domain_kebab_case_name(page_url)
    source_path_without_ext, extension = os.path.splitext(image_path)
    source_path_kebab_case = make_kebab_case_name(source_path_without_ext)
    if not extension:
        extension = '.html'
    source_name = domain_kebab_case + '-' + source_path_kebab_case + extension
    return source_name


def make_url(page_url, link):
    '''
    Make absolut source's url
    :param page_url: page which contains link to source
    :param link: link to source: url or path
    :return: source absolute url
    '''
    domain_with_scheme = (
            urlparse(page_url).scheme + '://' + urlparse(page_url).netloc)
    return domain_with_scheme + urlparse(link).path
