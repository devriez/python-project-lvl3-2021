import os
from page_loader.page_loader import make_page_file_name
from page_loader.page_loader import is_dir_exist
# from page_loader.page_loader import download
from page_loader.page_loader import make_file_name
from page_loader.page_loader import make_dir_with_files_name
from page_loader.page_loader import make_kebab_case_name
from page_loader.page_loader import make_url
from page_loader.page_loader import save_image
from page_loader.page_loader import change_links_and_save
import tempfile
import requests_mock
from bs4 import BeautifulSoup
import filecmp


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
        image_file_path = os.path.join(tmpdir_for_test, 'test.jpeg')
        save_image(img_url, image_file_path)
        save_image(img_url, 'tests/fixtures/test_file_downloaded.jpeg')
        assert os.path.isfile(image_file_path)
        assert filecmp.cmp(image_file_path, 'tests/fixtures/test_file2.jpg', shallow=True)
        assert filecmp.cmp(image_file_path, 'tests/fixtures/test_file2.jpg', shallow=False)


def test_change_links_and_save():
    page_url = 'https://en.wikipedia.org/wiki/Main_Page'
    with open('tests/fixtures/page.html') as test_page:
        test_html = test_page.read()
    soup = BeautifulSoup(test_html, 'html.parser')
    with tempfile.TemporaryDirectory() as tmpdir_for_test:
        soup = change_links_and_save(soup, page_url, tmpdir_for_test)
    with open('tests/fixtures/page_with_new_img_paths.html') as test_page:
        correct_html = test_page.read()
    assert correct_html == soup.prettify(formatter="html5")
