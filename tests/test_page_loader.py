import os
from page_loader.name_and_path_makers import make_page_file_name, make_dir_with_files_name, make_kebab_case_name, \
    make_file_name, make_url, make_path
from page_loader.file_interactors import is_dir_exist, change_links_and_save, read_source, save_file
# from page_loader.page_loader import download
# save_image
import tempfile
import requests_mock
from bs4 import BeautifulSoup
import filecmp
import logging

logging.basicConfig(
    level=logging.DEBUG
)


def test_make_page_file_name():
    PAGE_FILE_NAME_CORRECT = 'ru-hexlet-io-courses.html'
    page_file_name = make_page_file_name('https://ru.hexlet.io/courses')
    assert PAGE_FILE_NAME_CORRECT == page_file_name


def test_make_dir_with_files_name():
    CORRECT_NAME_DIR_WITH_IMAGES = 'ru-hexlet-io-courses_files'
    file_name = 'https://ru.hexlet.io/courses'
    assert CORRECT_NAME_DIR_WITH_IMAGES == make_dir_with_files_name(file_name)


def test_is_dir_exist():
    assert is_dir_exist(os.getcwd()) is True


# def test_download(requests_mock):
#     with tempfile.TemporaryDirectory() as tmpdir_for_test:
#         requests_mock.get('https://ru.hexlet.io/courses', text='data')
#         file_path = download('https://ru.hexlet.io/courses', tmpdir_for_test)
#         with open(file_path) as file:
#             assert 'data' == file.read()


def test_make_kebab_case_name():
    NAME = '/assets/professions/nodejs.pop'
    CORRECT_KEBAB_CASE_NAME = 'assets-professions-nodejs-pop'
    assert CORRECT_KEBAB_CASE_NAME == make_kebab_case_name(NAME)


def test_make_file_name():
    path_to_image = make_file_name(
        'https://ru.hexlet.io/courses', '/assets/professions/nodejs.png'
    )
    correct_path_to_image = 'ru-hexlet-io-assets-professions-nodejs.png'
    assert path_to_image == correct_path_to_image


def test_make_image_url_absolut():
    CORRECT_IMAGE_URL_ABSOLUTE = 'https://ru.hexlet.io/assets/professions/nodejs.png'
    PAGE_URL = 'https://ru.hexlet.io/courses'
    IMAGE_PATH = '/assets/professions/nodejs.png'
    img_url_absolut = make_url(PAGE_URL, IMAGE_PATH)
    assert CORRECT_IMAGE_URL_ABSOLUTE == img_url_absolut


def test_save_image():
    img_url = (
        f'https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Elizabeth_Raffald_%28cropped%29.jpg/'
        f'800px-Elizabeth_Raffald_%28cropped%29.jpg'
    )

    with tempfile.TemporaryDirectory() as tmpdir_for_test:
        img_doc = read_source(img_url)
        image_file_path = os.path.join(tmpdir_for_test, 'test.jpeg')
        save_file(image_file_path, img_doc)

        assert os.path.isfile(image_file_path)
        assert filecmp.cmp(image_file_path, 'tests/fixtures/test_file2.jpg', shallow=True)
        assert filecmp.cmp(image_file_path, 'tests/fixtures/test_file2.jpg', shallow=False)


def test_change_links_and_save():
    page_url = 'https://cdn2.hexlet.io/packs'
    with open('tests/fixtures/page.html') as test_page:
        test_html = test_page.read()
    with tempfile.TemporaryDirectory() as tmpdir:
        dir_with_files_name = make_dir_with_files_name(page_url)
        dir_with_files_path = make_path(dir_with_files_name, tmpdir)
        os.mkdir(dir_with_files_path)
        result_html = change_links_and_save(test_html, page_url, tmpdir)
    with open('tests/fixtures/page_with_new_img_paths.html') as test_page:
        correct_html = test_page.read()
    assert correct_html == result_html
