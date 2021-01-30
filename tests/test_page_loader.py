import os
from page_loader.page_loader import make_page_file_name
from page_loader.page_loader import is_dir_exist
#from page_loader.page_loader import download
from page_loader.page_loader import make_image_file_name
from page_loader.page_loader import make_name_dir_with_images
from page_loader.page_loader import make_kebab_case_name
from page_loader.page_loader import make_image_url_absolut
from page_loader.page_loader import save_image
import tempfile
import requests_mock


def test_make_page_file_name():
    PAGE_FILE_NAME_CORRECT = 'ru-hexlet-io-courses.html'
    page_file_name = make_page_file_name('https://ru.hexlet.io/courses')
    assert PAGE_FILE_NAME_CORRECT == page_file_name


def test_make_name_dir_with_images():
    CORRECT_NAME_DIR_WITH_IMAGES = 'ru-hexlet-io-courses_files'
    file_name = 'ru-hexlet-io-courses.html'
    assert CORRECT_NAME_DIR_WITH_IMAGES == make_name_dir_with_images(file_name)


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


def test_make_image_file_name():
    path_to_image = make_image_file_name(
        'https://ru.hexlet.io/courses', '/assets/professions/nodejs.png'
    )
    correct_path_to_image = 'ru-hexlet-io-assets-professions-nodejs.png'
    assert path_to_image == correct_path_to_image


def test_make_image_url_absolut():
    CORRECT_IMAGE_URL_ABSOLUTE = 'https://ru.hexlet.io/assets/professions/nodejs.png'
    PAGE_URL = 'https://ru.hexlet.io/courses'
    IMAGE_PATH = '/assets/professions/nodejs.png'
    img_url_absolut = make_image_url_absolut(PAGE_URL, IMAGE_PATH)
    assert CORRECT_IMAGE_URL_ABSOLUTE == img_url_absolut


def test_save_image():
    img_url = 'https://en.wikipedia.org/wiki/Main_Page#/media/File:RE_Kaja_Kallas.jpg'
    with tempfile.TemporaryDirectory() as tmpdir_for_test:
        image_file_path = os.path.join(tmpdir_for_test, 'test.jpeg')
        save_image(img_url, image_file_path)
        assert os.path.isfile(image_file_path)
