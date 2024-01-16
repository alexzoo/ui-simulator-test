import time


def test_successful_login(index_page):
    index_page.login('correct_username', 'correct_password')
    index_page.verify_url()


def test_password_incorrect(index_page):
    index_page.login('correct_username', '123')
    index_page.verify_error_message('Password or username is incorrect')


def test_username_incorrect(index_page):
    index_page.login('123', 'correct_password')
    index_page.verify_error_message('Password or username is incorrect')


def test_empty_password(index_page):
    index_page.login('correct_username', '')
    index_page.verify_error_message('Password field cannot be empty')


def test_empty_username(index_page):
    index_page.login('', 'correct_password')
    index_page.verify_error_message('Username field cannot be empty')


"""
1. сделать через параметризацию
2. опубликовать в github
3. добавить в гитигнор файлы которые считаешь нужными 
"""