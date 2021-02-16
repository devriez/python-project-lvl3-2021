import os
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

from page_loader.logger import get_logger
from page_loader.name_and_path_makers import make_dir_with_files_name, \
    make_path, make_url, make_file_name

from progress.bar import Bar

logger = get_logger(__name__)


def is_dir_exist(output_dir):
    '''
    Check is directory exist
    :param
        output_dir: directory path
    :return: True of False
    '''
    return os.path.exists(output_dir) and os.path.isdir(output_dir)


def save_file(destination_path, content):
    '''
    Saving source content to file
    :param
        destination_path: file path
        content: source content
    :return:
        None
    '''
    try:
        with open(destination_path, "wb") as f:
            f.write(content)
    except OSError as error:
        logger.critical(error)
        raise OSError()


def save_page(page_file_path, content):
    '''
    Saving page content to file
    :param
        destination_path: file path
        content: page content (html)
    :return:
        None
    '''
    try:
        with open(page_file_path, "w") as f:
            f.write(content)
    except OSError as error:
        logger.critical(error)
        raise OSError()


def read_page(url):
    '''
    Read page
    :param
        url: page url
    :return:
        page.text - page text(html)
    '''
    try:
        page = requests.get(url)
        page.raise_for_status()
    except requests.exceptions.RequestException as error:
        logger.critical(error)
        raise requests.exceptions.RequestException()
    return page.text


def read_source(source_url):
    '''
    Read page with source
    :param
        source_url: url with source
    :return: p.content - source content
    '''
    try:
        p = requests.get(source_url)
        p.raise_for_status()
    except requests.exceptions.RequestException as error:
        logger.critical(error)
        raise requests.exceptions.RequestException()
    return p.content


def change_links_and_save(html_doc, page_url, output_dir):
    '''
    Change source links in tags in html. links - saved locally source files
    :param html_doc: page html text
    :param page_url: page url
    :param output_dir: directory to save page html with new sources links
    :return: html with local links
    '''
    logger.info('making soup')
    soup = BeautifulSoup(html_doc, 'html.parser')
    logger.info('making dir with files name and path')
    dir_with_files_name = make_dir_with_files_name(page_url)
    dir_with_files_path = make_path(dir_with_files_name, output_dir)
    logger.warning(f'{dir_with_files_name} and {dir_with_files_path}')

    logger.info('starts loop in tags')
    tag_list = soup.find_all(['link', 'script', 'img'])

    bar = Bar('Processing', max=len(tag_list))

    for source_tag in tag_list:
        logger.debug(f'source_tag {source_tag}')
        src_or_href = choose_src_or_href_attribute(source_tag)
        if not src_or_href:
            bar.next()
            continue

        source_link = source_tag.get(src_or_href)
        logger.debug(f'source_link {source_link}')
        if (
                not urlparse(source_link).netloc
                or
                urlparse(source_link).netloc == urlparse(page_url).netloc
        ):
            source_url = make_url(page_url, urlparse(source_link).path)
            logger.debug(f'done source_url {source_url}')
            source_file_name = make_file_name(page_url,
                                              urlparse(source_link).path)
            logger.debug(f'done source_file_name {source_file_name}')

            source_path = make_path(source_file_name, dir_with_files_path)
            logger.debug(f'done source_path {source_path}')
            logger.info('read source')

            source_content = read_source(source_url)
            logger.debug('saving source in file')
            save_file(source_path, source_content)

            logger.debug('saving source_tag')
            source_tag[src_or_href] = make_path(source_file_name,
                                                dir_with_files_name)
            logger.debug(f'source_tag: {source_tag}')
        bar.next()
    bar.finish()

    logger.info('making html_with_local_links from soup')
    html_with_local_links = soup.prettify(formatter="html5")
    logger.info('html_with_local_links')
    return html_with_local_links


def choose_src_or_href_attribute(tag):
    if tag.get('src'):
        return 'src'
    if tag.get('href'):
        return 'href'
    else:
        return False
