from page_loader.page_loader import make_file_path

FILE_NAME_CORRECT = '/var/tmp/ru-hexlet-io-courses.html'


def test_make_file_path():
    file_name = make_file_path('https://ru.hexlet.io/courses', '/var/tmp')
    assert FILE_NAME_CORRECT == file_name
