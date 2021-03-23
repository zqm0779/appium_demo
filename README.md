# appium_demo
appium
#常用方法
#中止会话
driver.quit()
#后退
driver.back()
#屏幕截图
screenshotBase64 = self.driver.get_screenshot_as_base64()

#屏幕截图
screenshotBase64 = self.driver.get_screenshot_as_base64()
#获得页面源码
source = self.driver.page_source
#设置超时
driver.set_page_load_timeout(5000)
#设置隐式等待超时时间

driver.implicitly_wait(5)
#设置脚本超时时间

driver.set_script_timeout(5000)
#获取显示方面，横屏竖屏
orientation = driver.orientation
#设置显示方向
driver.orientation = "LANDSCAPE"
#获得地理位置
location = driver.location()
#设置地理位置
driver.set_location(49, 123, 10)
#获得可用的日志类型
log_types = driver.log_types
#获得日志对象
logs = driver.get_log('driver');
#记录事件
driver.log_event('appium', 'funEvent')

#获取事件

driver.get_events()
driver.get_events(['event1', 'event2'])
#更新设备的设置项
driver.update_settings({"sample": "value"}))
#提取设备的设置项
driver.get_settings

#启动Activity
driver.start_activity("com.example", "ActivityName")
#获取当前的Activity名称
driver.current_activity
#获取当前的包名
driver.current_package
#安装应用

driver.install_app('/Users/johndoe/path/to/app.apk')
#检查设备上是否安装了指定的应用程序
driver.is_app_installed('com.example.AppName')
#启动应用
driver.launch_app()
#应用置后台
driver.background_app()
#关闭app
driver.close_app()
#重置应用
driver.reset()
#删除应用
driver.remove_app('com.example.AppName')
#获取剪贴板

self.driver.get_clipboard()
self.driver.get_clipboard_text()
#设置剪贴板
self.driver.set_clipboard('happy testing')
self.driver.set_clipboard_text('happy testing')

 31.推送文件
dest_path = '/data/local/tmp/test_push_file.txt'
data = bytes('This is the contents of the file to push to the device.', 'utf-8'
)
driver.push_file(dest_path, base64.b64encode(data).decode('utf-8'))
        32.拉取文件
driver.pull_file('/path/to/device/foo.bar')
        33.拉取文件夹
driver.pull_folder('/path/to/device/')
        34.摇一摇
driver.shake()
        35.锁定
driver.lock()
        36.解锁
driver.unlock()
        37.设备是否锁定
driver.is_locked()
        38.按键Code
driver.press_keycode(10)
        39.隐藏键盘
driver.hide_keyboard()
        40.是否显示键盘
driver.is_keyboard_shown()
        41.切换WiFi
driver.toggle_wifi()
        42.切换定位服务
driver.toggle_location_services()
        43.发送短信(只支持模拟器)
driver.send_sms('19904636190', 'Hey lol')
        44.拨打电话(只支持模拟器)
driver.make_gsm_call('5551234567', GsmCallActions.CALL)
        45.网络速度

driver.set_network_speed(NetSpeed.LTE)
        46.获取性能数据
返回支持读取的系统状态信息，例如cpu，内存，网络流量和电池信息
driver.get_performance_data('my.app.package', 'cpuinfo', 5)
        47.获取性能数据类型
driver.get_performance_data_types()
        48.开始屏幕录制
driver.start_recording_screen()
        49.打开通知(仅模拟器)
driver.open_notifications()

        50.获取系统栏
driver.get_system_bars()
        51.获取系统时间
time = driver.device_time
time = driver.get_device_time()
time = driver.get_device_time("YYYY-MM-DD")
        52.元素查找
driver.find_element_by_accessibility_id('SomeAccessibilityID')
        53.元素组查找
driver.find_elements_by_accessibility_id('SomeAccessibilityID')
        54.元素点击
el = driver.find_element_by_accessibility_id('leizi')
el.click();
        55.发送key
driver.find_element_by_accessibility_id('leizishuoceshi').send_keys('Hello world!')
        56.清理值
driver.find_element_by_accessibility_id('leizishuoceshi').clear()
        57.获取元素的文本
e1=driver.find_element_by_accessibility_id('leizishuoceshi')
text = el.text
        58.获取标签名
driver.find_element_by_accessibility_id('leizishuoceshi').tag_name
        59.获得元素属性
driver.find_element_by_accessibility_id('leizishuoceshi').get_attribute('content-desc')
        60.元素被选中
driver.find_element_by_accessibility_id('leizishuoceshi').is_selected()


 61.元素是否可操作性
driver.find_element_by_accessibility_id('leizishuoceshi').is_enabled()
            62.元素是否可见
driver.find_element_by_accessibility_id('leizishuoceshi').is_displayed()
            
            64.获得元素定位
driver.find_element_by_accessibility_id('leizishuoceshi').location
            65.获取元素大小
driver.find_element_by_accessibility_id('leizishuoceshi').size
        
         66.获取元素矩形
driver.find_element_by_accessibility_id('leizishuoceshi')
    
        67.获取CSS元素的值
driver.find_element_by_accessibility_id('leizishuoceshi').value_of_css_property("style")

        68.获取视图中的元素位置
    
element = self.driver.find_element_by_accessibility_id('leizishuoceshi')
element.location_in_view

        69.表单提交
el = self.driver.find_element_by_accessibility_id('leizishuoceshi')
el.submit()

        70.获取焦点元素

driver.switch_to.active_element
      
       71.获取当前Context
context = driver.current_context
       
       72.设置当前Context
webview = driver.contexts[1]
driver.switch_to.context(webview)
       
       73.移动到点
actions = ActionChains(driver)
actions.move_to(element, 10, 10)
actions.perform()
        
        74.Click单击
actions = ActionChains(driver)
actions.move_to_element(element)
actions.click()
actions.perform()

        75.双击 
actions = ActionChains(driver)
actions.move_to_element(element)
actions.double_click()
actions.perform()

        76.轻按屏幕启用设备

from appium.webdriver.common.touch_action import TouchAction
actions = TouchAction(driver)
actions.tap(element)
actions.perform()

        77.双击
from appium.webdriver.common.touch_action import TouchAction
actions = TouchAction(driver)
actions.double_tap(element)
actions.perform()

     78.手指在屏幕上移动
from appium.webdriver.common.touch_action import TouchAction
actions = TouchAction(driver)
actions.tap_and_hold(element)
actions.move_to(element, 50, 50)
actions.perform()
    
    79.手指长按触摸屏的事件 
from appium.webdriver.common.touch_action import TouchAction
actions = TouchAction(driver)
actions.long_press(element)
actions.perform()

    80.手指在触摸屏上滚动的运动事件
from appium.webdriver.common.touch_action import TouchAction
actions = TouchAction(driver)
actions.scroll_from_element(element, 10, 100)
actions.scroll(10, 100)
actions.perform()

    81.手指在触摸屏上滑动的动作事件
from appium.webdriver.common.touch_action import TouchAction
actions = TouchAction(driver)
actions.flick_element(element, 1, 10, 10)
actions.perform()

     82.执行多点触控动作序列
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
a1 = TouchAction()
a1.press(10, 20)
a1.move_to(10, 200)
a1.release()
a2 = TouchAction()
a2.press(10, 10)
a2.move_to(10, 100)
a2.release()
ma = MultiAction(self.driver)
ma.add(a1, a2)
ma.perform()

     83.执行触摸动作序列
from appium.webdriver.common.touch_action import TouchAction
actions = TouchAction(driver)
actions.tap_and_hold(20, 20)
actions.move_to(10, 100)
actions.release()
actions.perform()

     84.切换窗口
driver.switch_to.window("handle")

     85.关闭窗口
driver.close()
    
     86.获取窗口句柄
driver.current_window_handle()

     87.获取窗口所有的句柄
driver.window_handles()

     88.获取标题
driver.title

     89.获取窗口大小
driver.get_window_size()

    90.设置窗口大小
driver.set_window_size(10, 10)
  91.获取窗口位置
handle_one_position = self.driver.get_window_position()
handle_two_position = self.driver.get_window_position("handleName")
        
        92.设置窗口位置
driver.set_window_position(10, 10)
    
        93.最大化窗口
driver.maximize_window()
        
        94.回退
driver.back()
        
        95.前进
driver.forward()
    
        96.刷新
driver.refresh()
        
        97.获取所有 Cookies(仅是 Web context)
driver.get_cookies()
       98.设置 Cookie 
        (仅是 Web context)
driver.add_cookie({name: 'foo', value: 'bar'})

        99.删除 Cookie
driver.delete_cookie("cookie_name")
            
        100.删除所有 Cookies
driver.delete_all_cookies()
        
        101.切换Frame
driver.switch_to.frame(3)
    
        102.切换到父Frame
driver.switch_to.parent()

        103.执行异步脚本
driver.execute_async_script(‘document.title’）
    
        104.执行脚本
driver.execute_script(‘document.title’)
        
        

        补充常见的元素定位方式
driver.find_element_by_accessibility_id()
driver.find_element_by_android_uiautomator("new UiSelector().resourceId(\"com.oupeng.mini.android:id/search_engine_title")")
driver.find_element_by_class_name()#class属性是classname
driver.find_element_by_id()
driver.find_element_by_ios_class_chain()
driver.find_element_by_ios_predicate()#仅支持iOS10以上，可以多个属性同时定位
driver.find_element_by_ios_uiautomation()
driver.find_element_by_link_text()
driver.find_element_by_css_selector()
driver.find_element_by_xpath()
driver.find_element_by_partial_link_text()
driver.find_element_by_tag_name()
driver.find_element_by_name()#text属性是name