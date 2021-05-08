# coding=utf-8
from selenium import webdriver
import unittest
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from public.login import Mylogin

class Gouwuche(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://101.133.169.100/yuns/index.php")
        self.driver.maximize_window()
        time.sleep(5)

    def tearDown(self):
        filedir = "D:/test/screenshot/"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('D:/', 'test', 'screenshot'))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()


    # def testGouwu01_01(self):
    #     '''购物车为空时文案显示是否正常'''
    #     Mylogin(self.driver).login()
    #     self.driver.find_element_by_xpath("//div[@class='small_cart_name']/span").click()
    #     time.sleep(3)
    #     emptyGouwuText = self.driver.find_element_by_xpath("//div[@class='r']/span")
    #     print(emptyGouwuText.text)
    #     self.assertEqual("购物车内暂时没有商品",emptyGouwuText.text)

    def testGouwu01_02(self):
        '''点击秒杀商品添加到购物车，是否弹出提示框'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_link_text("秒杀").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[3]/div[3]/div[2]/a").click()
        self.driver.find_element_by_css_xpath(".yyue").click()
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div[2]/div[3]/dl[1]/dd/a/em").click()
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div[2]/div[3]/dl[2]/dd/a/em").click()
        self.driver.find_element_by_css_xpath(".yyue").click()
        self.assertEqualTrue(self.driver.find_element_by_link_text(".buy_tip_name>p")).is_displayed()

    # def testGouwu01_03(self):
    #     '''查看商品下面是否有库存显示'''
    #     Mylogin(self.driver).login()

if __name__ == "__main__":
    unittest.main()


