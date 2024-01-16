from pytest import mark


def test_successful_login(index_page):
    index_page.login('correct_username', 'correct_password')
    index_page.verify_url()


# def test_password_incorrect(index_page):
#     index_page.login('correct_username', '123')
#     index_page.verify_error_message('Password or username is incorrect')
#
#
# def test_username_incorrect(index_page):
#     index_page.login('123', 'correct_password')
#     index_page.verify_error_message('Password or username is incorrect')
#
#
# def test_empty_password(index_page):
#     index_page.login('correct_username', '')
#     index_page.verify_error_message('Password field cannot be empty')
#
#
# def test_empty_username(index_page):
#     index_page.login('', 'correct_password')
#     index_page.verify_error_message('Username field cannot be empty')


password_incorrect = ['correct_username', 'password', 'Password or username is incorrect']
username_incorrect = ['user', 'correct_password', 'Password or username is incorrect']
empty_password = ['correct_username', '', 'Password field cannot be empty']
empty_username = ['', 'correct_password', 'Username field cannot be empty']


@mark.parametrize('username, password, error_message', (password_incorrect, username_incorrect, empty_password, empty_username),
                  ids=['password_incorrect', 'username_incorrect', 'empty_password', 'empty_username'])
def test_unsuccessful_login(index_page, username, password, error_message):
    index_page.login(username=username, password=password)
    index_page.verify_error_message(error_message)


"""
1. сделать через параметризацию - done
2. опубликовать в github - done
3. добавить в гитигнор файлы которые считаешь нужными  - done
"""