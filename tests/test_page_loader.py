import os
from page_loader.page_loader import make_file_path
from page_loader.page_loader import is_dir_exist
from page_loader.page_loader import download
from page_loader.page_loader import make_path_to_image
import tempfile
import requests_mock

FILE_NAME_CORRECT = '/var/tmp/ru-hexlet-io-courses.html'


def test_make_file_path():
    file_name = make_file_path('https://ru.hexlet.io/courses', '/var/tmp')
    assert FILE_NAME_CORRECT == file_name


def test_is_dir_exist():
    assert is_dir_exist(os.getcwd()) is True


def test_download(requests_mock):
    with tempfile.TemporaryDirectory() as tmpdir_for_test:
        requests_mock.get('https://ru.hexlet.io/courses', text='data')
        file_path = download('https://ru.hexlet.io/courses', tmpdir_for_test)
        with open(file_path) as file:
            assert 'data' == file.read()


def test_make_path_to_imahe():
    path_to_image = make_path_to_image(
        'https://ru.hexlet.io/courses', '/assets/professions/nodejs.png'
    )
    correct_path_to_image = 'ru-hexlet-io-assets-professions-nodejs.png'
    assert path_to_image == correct_path_to_image
