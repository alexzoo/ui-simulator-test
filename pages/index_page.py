from playwright.sync_api import expect, Page


class IndexPage:

    USERNAME_FIELD = "#username"
    PASSWORD_FIELD = "#password"
    LOGIN_BTN = ".login-button"
    ERROR_MESSAGE = ".error-message"

    def __init__(self, page: Page) -> None:
        self.page = page

    def login(self, username: str, password: str) -> None:
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_btn()

    def enter_username(self, username: str) -> None:
        self.page.locator(self.USERNAME_FIELD).fill(username)

    def enter_password(self, password: str) -> None:
        self.page.locator(self.PASSWORD_FIELD).fill(password)

    def click_login_btn(self) -> None:
        self.page.locator(self.LOGIN_BTN).click()

    def verify_url(self) -> None:
        expect(self.page).to_have_url('https://toghrulmirzayev.github.io/ui-simulator/hover_and_select.html')

    def verify_error_message(self, error_message: str) -> None:
        expect(self.page.locator(self.ERROR_MESSAGE)).to_have_text(error_message)

