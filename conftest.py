from pytest import fixture
from pages.index_page import IndexPage


@fixture()
def index_page(page):
    page.goto('https://toghrulmirzayev.github.io/ui-simulator/index.html')
    yield IndexPage(page)