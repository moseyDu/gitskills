# unittet是Python自带的一个单元测试的模块


# --引入unittest模块
# --让所有执行测试的类都继承于TestCase类,可以讲TestCase看成是对特定类进行测试的方法的集合
# --在SetUp()方法中进行测试前的初始化工作,并在tearDown()中执行测试后的清除工作,它会在每一个测试方法执行之后被执行
# --定义测试用例，名字以test开头
# --调用unittest.main()启动测试


# 例：编写一个在python.org站点上搜索的测试用例：
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=
                          'D:\pycharm\pycharm-professional-2017\pycharm-professional-2017.3.4\chromedriver.exe')

    def test_search_python_org(self):
        driver = self.driver
        driver.get("https://www.python.org/")
        self.assertIn("Python", driver.title)       # 判断页面标题是否包含"Python"
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)     # 按下键盘enter键
        assert "No results found." not in driver.page_source       # 判断结果是否成功返回

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()






























