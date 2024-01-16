from pytest import mark
import random

rand_numbers = [1, 2]


@mark.ui
def test_fake_page1():
    assert 1 == random.choice(rand_numbers)


@mark.api
def test_ui_fake_page2():
    pass


@mark.ui
@mark.smoke
def test_fake_page3():
    pass

