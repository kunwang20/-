import os.path, allure, pytest, functools
from common.Config import Config


class PrettyAllure(object):
    """
    allure方法抽离 截图方法实现
    """
    @classmethod
    def PrettyAllureCase(cls, page, CaseData):
        allure.dynamic.feature(CaseData.get("模块"))
        allure.dynamic.story(CaseData.get("功能"))
        allure.dynamic.severity(CaseData.get("优先级"))
        allure.dynamic.title(f'{CaseData.get("用例编号")}_{CaseData.get("用例标题")}')
        if CaseData.get("是否执行") != "Y":
            allure.dynamic.description("用例指定跳过")
            pytest.skip("用例指定跳过")

    @classmethod
    def PrettyAllureScreenShot(cls, page, CaseData):
        filename = os.path.join(Config.test_screenshot_dir, f"{CaseData.get('用例标题')}.png")
        page.screenshot(path=filename)
        allure.attach.file(source=filename, name=CaseData.get('用例标题'), attachment_type=allure.attachment_type.PNG)

    @classmethod
    def PrettyAllureWarpper(cls, func):
        """装饰器函数"""

        @functools.wraps(func)
        def inner(*args, **kwargs):
            # 添加用例信息
            cls.PrettyAllureCase(page=kwargs.get("page"), CaseData=kwargs.get("CaseData"))  # 如何获取case_data?
            r = func(*args, **kwargs)  # 运行用例
            # 添加截图
            cls.PrettyAllureScreenShot(page=kwargs.get("page"), CaseData=kwargs.get("CaseData"))
            return r

        return inner

if __name__ == '__main__':
    pass