import os
from page_loader.logger import get_logger
from page_loader.file_interactors import \
    is_dir_exist, save_page, read_page, change_links_and_save
from page_loader.name_and_path_makers import \
    make_page_file_name, make_path, make_dir_with_files_name

logger = get_logger(__name__)


def download(page_url, output_dir):
    '''
    Save page locally. And save locally sources from this page
    :param page_url:
    :param output_dir: directory to save page and sources
    :return: path to page saved locally
    '''
    logger.info(f'start func with page_url:{page_url},output_dir:{output_dir}')

    if not is_dir_exist(output_dir):
        logger.worning("An output directory doesn't exist!")
        raise NameError('Missing directory')

    logger.info('reading page')
    html_doc = read_page(page_url)

    logger.info('making page_file_name and page_file_path')
    page_file_name = make_page_file_name(page_url)
    page_file_path = make_path(page_file_name, output_dir)
    logger.info(f'{page_file_name} and {page_file_path}')

    logger.info('making dir with files name and path')
    dir_with_files_name = make_dir_with_files_name(page_url)
    dir_with_files_path = make_path(dir_with_files_name, output_dir)
    logger.info(f'{dir_with_files_name} and {dir_with_files_path}')

    logger.info('making dir with files')
    try:
        os.mkdir(dir_with_files_path)
    except OSError as error:
        logger.critical(error)
        raise OSError()

    logger.info('changing links and saving')
    logger.info(f'page_url {page_url} and output_dir {output_dir}')
    html_with_local_links = change_links_and_save(html_doc, page_url,
                                                  output_dir)

    logger.ingo('saving html with local links')
    save_page(page_file_path, html_with_local_links)

    return page_file_path
