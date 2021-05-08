import os
import unittest
import time
from public.loginApp import Mylogin
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class ShouyeTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['noReset'] = 'True'
        desired_caps['app'] = PATH('F:/BaiduNetdiskDownload/appium/zuiyou518.apk')
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'
        desired_caps['appActivity'] = '.ui.base.SplashActivity'
        desired_caps['automationName'] = 'Uiautomator2'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        filedir = "F:/test/screenshot/"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join("F:/","test","screenshot"))
        screen_name = filedir + time.strftime('%Y-%m-%H-%M-%S',time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()

    def testshouye01_01(self):
        '''验证首页导航栏文案显示是否正常'''
        time.sleep(8)
        try:
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        except:
            pass
        time.sleep(6)
        navText = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/title")
        self.assertEqual(navText[0].text,"关注")
        self.assertEqual(navText[1].text, "推荐")
        self.assertEqual(navText[2].text, "视频")
        self.assertEqual(navText[3].text, "图文")


    def testshouye01_02(self):
        '''验证帖子列表内容跳转'''
        time.sleep(8)
        aa = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/expand_content_view")
        bb = aa.text
        aa.click()
        time.sleep(3)
        forumDetailText = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvTitle")
        cc = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvPostContent")
        self.assertEqual(forumDetailText.text,"帖子详情")
        self.assertEqual(bb,cc.text)


    def testshouye01_03(self):
        '''验证评论帖子功能'''
        # try:
        #     self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        # except:
        #     pass
        # Mylogin(self.driver).login()
        # time.sleep(3)
        # self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/iconTabItem").click()
        time.sleep(3)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/middle_view").click()
        time.sleep(6)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/etInput").click()
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/etInput").send_keys("cc")
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/send").click()
        # sendContent = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/expandTextView")
        # sendContentRawList = []
        # for i in range(0, len(sendContent)):
        #     sendContentRawList.append(sendContent[i].text)
        # sendContentList = "".join(sendContentRawList)
        # self.assertIn("huhui", sendContentList)
        time.sleep(2)
        sendContent = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/expandTextView")
        sendContentRawList = []
        for i in range(0, len(sendContent)):
            sendContentRawList.append(sendContent[i].text)
        sendContentList = "".join(sendContentRawList)
        self.assertIn('cc', sendContentList)

    def testshouye01_04(self):
        '''点击刷新按钮查看页面是否出现提示语'''
        time.sleep(6)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_refresh_view").click()
        toast_loc = ("xpath",'.//*[contains(@text,"为你选出14条好贴")]')
        #el = WebDriverWait(self.driver,20,0.1).until(EC.presence_of_element_located(toast_loc))
        el = WebDriverWait(self.driver, 20, 0.1).until(EC.presence_of_element_located(toast_loc))
        self.assertEqual(el.text,'为你选出14条好贴')
        time.sleep(2)
        self.driver.keyevent(4)


    def testshouye01_05(self):
        '''点击刷新按钮查看页面内容是否变化'''
        time.sleep(6)
        el = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/simple_member_tv_name")
        aa = el.text
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_refresh_view").click()
        bb = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/simple_member_tv_name")
        self.assertEqual(aa,bb.text )


    def testshouye01_06(self):
        '''搜索输入框能否输入内容'''
        time.sleep(6)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b").click()
        time.sleep(3)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/search_input").click()
        el = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/search_input").send_keys("哦豁")
        self.assertEqual(el.text,'哦豁')




    def testshouye01_07(self):
        '''搜索输入框中是否有提示语'''
        time.sleep(6)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b").click()
        time.sleep(3)
        el = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/search_input")
        self.assertEqual(el.text, '搜索话题 / 帖子 / 用户')

    def testshouye01_08(self):
        '''搜索是否支持模糊查询'''
        time.sleep(6)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b").click()
        time.sleep(3)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/search_input").click()
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/search_input").send_keys("love")
        sendContent = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/title")
        sendContentRawList = []
        for i in range(0, len(sendContent)):
            sendContentRawList.append(sendContent[i].text)
        sendContentList = "".join(sendContentRawList)
        self.assertIn("love", sendContentList)



    def testshouye01_09(self):
        '''搜索内容前置空格'''
        time.sleep(6)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b").click()
        time.sleep(3)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/search_input").click()
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/search_input").send_keys("  love")
        self.assertEqualTrue(self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/title").is_displayed())


    def testshouye01_10(self):
        '''搜索输入的内容查询不到时是否有提示语'''
        time.sleep(6)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b").click()
        time.sleep(3)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/search_input").click()
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/search_input").send_keys("咔咔咔咔咔咔扩")
        self.assertEqualTrue(self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvTip").is_displayed())


    def testshouye01_11(self):
        '''搜索后是否有搜索记录'''
        time.sleep(6)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b").click()
        time.sleep(3)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/search_input").click()
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/search_input").send_keys("love")
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/title").click()
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ivBack").click()
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/search_input_clear").click()
        self.assertEqualTrue(self.driver.find_element_by_xpath("//FrameLayout[@resource-id='android.widget.FrameLayout']/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.TextView").is_displayed())
        self.assertEqualTrue(self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/title").is_displayed())


    def testshouye01_12(self):
        '''输入内容时输入框中提示语是否被覆盖'''
        time.sleep(6)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b").click()
        time.sleep(3)
        el = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/search_input").click()
        aa =el.text
        el01 = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/search_input").send_keys('love')
        self.assertNotEqual(el01.text, aa)

    def testshouye01_13(self):
        '''页面长按是否弹出分享框'''
        time.sleep(6)
        heigth = self.driver.get_window_size()['height']
        width = self.driver.get_window_size()['width']
        self.driver.swipe(width*0.5,heigth*0.5,width*0.5,heigth*0.5,3000)
        self.assertEqualTrue(self.driver.find_element_by_xpath("//*[@text='QQ空间']").is_displayed())

    def testshouye01_14(self):
        '''页面下拉刷新'''
        time.sleep(6)
        heigth = self.driver.get_window_size()['height']
        width = self.driver.get_window_size()['width']
        self.driver.swipe(width*0.5,heigth*0.1,width*0.5,heigth*0.6,1000)
        toast_loc = ("xpath", './/*[contains(@text,"为你选出14条好贴")]')
        el = WebDriverWait(self.driver, 20, 0.1).until(EC.presence_of_element_located(toast_loc))
        self.assertEqual(el.text, '为你选出14条好贴')
        time.sleep(2)
        self.driver.keyevent(4)

    def testshouye01_15(self):
        '''点击我的是否跳转到个人页面'''
        time.sleep(6)
        self.driver.find_element_by_xpath("//android.view.ViewGroup[@resource-id='cn.xiaochuankeji.tieba:id/me_item']/android.widget.TextView[2]/").click()
        self.assertEqualTrue(self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/member_name").is_displayed())





if __name__ == "__main__":
    unittest.main()