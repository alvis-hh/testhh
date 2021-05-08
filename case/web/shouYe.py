# coding=utf-8
from selenium import webdriver
from public.login import Mylogin
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import os
import time

class TestShouye(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://101.133.169.100/yuns/index.php")
        self.driver.maximize_window()
        time.sleep(5)
        print("starttime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        # print(self.driver.window_handles)
        # print(self.driver.current_window_handle)
    def tearDown(self):
        filedir = "D:/test/screenshot/"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('D:/', 'test', 'screenshot'))
        print("endTime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()


    def testShouye01_01(self):
        '''测试首页导航文案显示是否正常'''
        Mylogin(self.driver).login()
        firstPageNavi = self.driver.find_element_by_xpath("//div[@class='top']/span")
        loginText = self.driver.find_element_by_css_selector("div.login>a:nth-child(1)")
        regisText = self.driver.find_element_by_css_selector("div.login>a:nth-child(3)")

        self.assertEqual("亲，欢迎您来到云商系统商城！",firstPageNavi.text)
        self.assertEqual("123", loginText.text)
        self.assertEqual("退出", regisText.text)

        # self.assertNotEqual("dd", regisText.text)
        #
        # self.assertIn("云商系统商城",firstPageNavi.text)
        #
        # self.assertTrue(self.driver.find_element_by_xpath("//div[@class='top']/span").is_displayed())
        # self.assertFalse(firstPageNavi.is_displayed())
        #
        # if loginText.text == "177****0979":
        #     print("等于")
        # else:
        #     print("不等于")
        #     self.driver.find_element_by_xpath("王麻子")



    def testShouye01_02(self):
        '''验证搜索内容无时，提示语是否正常'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_xpath("/html/body/div/div/div/div/form/input[1]").send_keys("王麻子")
        self.driver.find_element_by_xpath("/html/body/div/div/div/div/form/input[2]").click()
        time.sleep(2)
        searchText = self.driver.find_element_by_xpath("//div[@class='nomsg']")
        self.assertEqual(searchText.text, "抱歉，没有找到相关的商品")

    def testShouye01_03(self):
        '''点击关键字、热字是否跳转页面'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_css_selector("div.schhot>a:nth-child(3)").click()
        time.sleep(2)
        searchText = self.driver.find_element_by_css_selector("div.nomsg")
        self.assertEqual(searchText.text,"抱歉，没有找到相关的商品")

    def testShouye01_04(self):
        '''含有空格搜索物品，查看搜索结果'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_name("key").send_keys("  女装")
        self.driver.find_element_by_css_selector(".but2").click()
        time.sleep(2)
        searchText = self.driver.find_element_by_css_selector("div.nomsg")
        self.assertNotEqual(searchText.text, "抱歉，没有找到相关的商品")


    def testShouye01_05(self):
        '''是否支持模糊查询'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_name("key").send_keys("女")
        self.driver.find_element_by_css_selector(".but2").click()
        time.sleep(2)
        searchText = self.driver.find_element_by_link_text("女装 优质长绒棉A字型条纹连衣裙(七分袖) 412932 优衣库UNIQLO")
        self.assertEqual(searchText.text, "女装 优质长绒棉A字型条纹连衣裙(七分袖) 412932 优衣库UNIQLO")

    def testShouye01_06(self):
        '''页面下滑，搜索框是否置顶'''
        # Mylogin(self.driver).login()
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        time.sleep(5)
        # self.driver.find_element_by_xpath("/html/body/div[8]/div/form/div/input[2]").click()
        # ele = self.driver.find_element_by_xpath("/html/body/div[8]/div/form/div/input[2]").send_keys("白长衫")
        # time.sleep(6)
        # self.assertEqual(ele.text, "白长衫")
        self.assertTrue(self.driver.find_element_by_xpath("//*[@id='ssx_submit']").is_enabled())


    def testShouye01_07(self):
        '''搜索输入框中输入信息，输入框中提示语是否消失'''
        Mylogin(self.driver).login()
        searchText = self.driver.find_element_by_name("key")
        self.driver.find_element_by_name("key").send_keys("奢华黑袍")
        self.assertNotEqual(searchText.text, "奢华黑袍")

    def testShouye01_08(self):
        '''鼠标移动到精选商城下面名称，右侧是否出现二级子标题'''
        Mylogin(self.driver).login()
        ele = self.driver.find_element_by_link_text("男装女装")
        time.sleep(2)
        ActionChains(self.driver).move_to_element(ele).perform()
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/dl[1]/div/div[1]/div/a").is_enabled())
        # self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/dl[1]/div/div[1]/div/a").click()
        # ele = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div[1]/span")


    def testShouye01_09(self):
        '''点击动态消息，是否能够跳转相应页面'''
        # Mylogin(self.driver).login()
        self.driver.find_element_by_link_text("阿里推出88VIP卡").click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        dongtaiText = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[1]/h1")
        self.assertEqual(dongtaiText.text,"阿里推出88VIP卡")
        print(self.driver.window_handles)

    def testShouye01_10(self):
        '''用户在没有登录的情况下点击优惠劵，是否弹出登录界面'''
        time.sleep(3)
        self.driver.find_element_by_link_text("优惠券").click()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div[3]/a").click()
        # self.assertEqualTrue(self.driver.find_element_by_xpath("/html/div[2]/div/div/div[1]/span").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/div[2]/div/div/div[1]/span").is_displayed())


    def testShouye01_11(self):
        '''用户在没有登录的情况下点击优惠劵，是否弹出登录界面'''
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()


