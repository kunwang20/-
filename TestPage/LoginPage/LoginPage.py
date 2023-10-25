import allure
from common.BasePage import BasePage


class LoginPage(BasePage):
    # 元素定位器
    __username = "//body/div[@id='app']/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]"
    __password = "//body/div[@id='app']/div[1]/form[1]/div[2]/div[1]/div[1]/input[1]"
    __verify_code = "//body/div[@id='app']/div[1]/form[1]/label[1]/span[1]/span[1]"
    __button_login = "//span[contains(text(),'登 录')]"
    contions_pg = "//h1[contains(text(),'电恋生活管理系统')]"

    def del_auth(self):
        self._del_auth()

    @allure.step("打开登录页面")
    def goto_login(self, url):
        self._goto_url(url)

    @allure.step("输入账号")
    def fill_username(self, value):
        self._fill(self.__username, value)

    @allure.step("输入密码")
    def fill_password(self, value):
        self._fill(self.__password, value)

    @allure.step("记住密码")
    def click_verify_code(self, value):
        self._fill(self.__verify_code, value)

    @allure.step("点击登录按钮")
    def click_login_button(self):
        self._click(self.__button_login)

    @allure.step("断言登录成功")
    def login_to_be_visible(self, locator):
        return self._ele_to_be_visible(locator)

    def browser_operation(self, reload=True, forward=False, back=False):
        self._browser_operation(reload=reload, forward=forward, back=back)
