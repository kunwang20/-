import os


class Config:
    # 项目地址
    url = "https://www.520dl.com/#"

    # 项目根目录
    root_dir = os.path.split(os.path.split(__file__)[0])[0]
    test_cases_dir = root_dir + os.path.sep + "TestCases"
    test_files_dir = root_dir + os.path.sep + "TestFiles"
    test_datas_dir = root_dir + os.path.sep + "TestDatas"
    test_report_dir = root_dir + os.path.sep + "TestReport" + os.path.sep + "AllureReport"
    test_result_dir = root_dir + os.path.sep + "TestReport" + os.path.sep + "AllureResult"
    test_screenshot_dir = root_dir + os.path.sep + "TestReport" + os.path.sep + "Screenshot"
    logs = root_dir + os.path.sep + "Logs"

    # 权限认证目录
    auth_dir = root_dir + os.path.sep + "Auth"

    #浏览器
    browser = "chrome"

if __name__ == '__main__':
    print(Config.root_dir)
    print(Config.test_cases_dir)