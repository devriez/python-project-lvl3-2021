import re
import os


# def download(page_address, output_dir):
#     return

def make_file_path(page_address, output_dir):
    address_without_schema = page_address.split('//')[1]
    print('address_without_schema', address_without_schema)
    splited_words_in_address = re.split(r'[^a-zA-Z0-9]', address_without_schema)
    file_name = '-'.join(splited_words_in_address) + '.html'
    print('file_name', file_name)
    file_path = os.path.join(output_dir, file_name)
    return file_path
