"""
该文件是操作设备的一系列方法封装
todo:
1.webview内识别元素
2.断言
"""
import os

from common.logger import logger
from common.time_base import get_current_hour_minute
from common.operate_directory import operate_directory

get_file = os.path
path = get_file.dirname(get_file.realpath(__file__))  # 当前文件所在目录
yaml = get_file.join(path, "../report/")


def __handle_popup(driver):
    """
    该方法用于处理系统弹窗，默认点击"同意"
    :param driver: 初始化设备信息 self.driver
    """
    try:
        logger.info('正在尝试关闭系统权限申请弹窗......')
        while True:
            # if "不允许" in driver.page_source or "Don't Allow" in driver.page_source:
            driver.switch_to.alert.accept()
            break
        logger.info('已关闭系统权限申请弹窗！')

    except Exception as error:
        logger.error("handle permission popup exception: %s", error)
        return


def __scroll_screen(driver, number=4, direction="left"):
    """
    该方法用于滑动屏幕
    :param driver: 初始化设备信息 self.driver
    :param number: 滑屏的次数 默认是4次
    :param direction: 滑动屏幕的方法 默认是往左滑动
    """
    try:

        # 滑屏第一种方法：对ios机器有效，android未尝试
        for i in range(number):
            logger.debug('开始滑动屏幕......')
            driver.execute_script("mobile: swipe", {"direction": direction})
            logger.debug('滑动屏幕：第%s次', i + 1)

        # 滑屏第二种方法：
        # TouchAction(driver).press(x=1, y=395).move_to(x=5, y=419).release().perform()
        # 滑屏第三种方法：(对ios机器无效 会报错)
        # size = driver.get_window_size()
        # logger.debug('设备尺寸：%s', size)
        # x1 = int(size['width'] * 0.75)
        # y1 = int(size['height'] * 0.5)
        # x2 = int(size['width'] * 0.05)
        # # for i in range(number):
        # driver.swipe(x1, y1, x2, y1, duration)
        # logger.info('已滑动屏幕 1次')

    except Exception as error:
        logger.error("scroll screen exception: %s", error)
        return


def __find_element(driver, platform, find_type, element_position):
    """
    该方法用于识别元素
    :param driver: 初始化设备信息 self.driver
    :param platform: 被测设备系统 android | ios
    :param find_type: 发现元素方式
    :param element_position: 元素位置
    :return: element 找到的元素
    """
    try:
        if 'xpath' in find_type:
            element = driver.find_element_by_xpath(element_position)
        elif 'id' in find_type and platform == 'ios':
            element = driver.find_element_by_accessibility_id(element_position)
        else:
            element = driver.find_element_by_id(element_position)
        return element

    except Exception as error:
        logger.error('find element fail: %s', error)
        return


def __click_element(element):
    """
    该方法用于点击元素
    :param element: 找到的元素
    """
    element.click()


def __input_character(element, character):
    """
    该方法用于在输入框内输入字符
    :param element: 找到的元素
    :param character: 输入的字符
    """
    element.send_keys(character)


def __error_screenshot(driver, screenshot_path):
    """
    该方法用于抛异常时截取屏幕
    :param driver: 初始化设备信息 self.driver
    """
    driver.get_screenshot_as_file(screenshot_path)
    logger.warning('当前生成了一张错误截图!')


def __into_webview(driver):
    """
    该方法用于进入webview
    :param driver: 初始化设备信息 self.driver
    """
    try:
        contexts = driver.contexts
        driver.switch_to.context(contexts[1])  # contexts[1]:webview || contexts[0]:native
        if "WEBVIEW_" in driver.current_context:
            return True
    except Exception as error:
        logger.error("into webview fail: %s", error)
        return False


def __quit_webview(driver):
    """
    该方法用于退出webview
    :param driver: 初始化设备信息 self.driver
    """
    try:
        contexts = driver.contexts
        driver.switch_to.context(contexts[0])  # contexts[1]:webview || contexts[0]:native
        if "NATIVE_APP" in driver.current_context:
            return True
    except Exception as error:
        logger.error("quit webview fail: %s", error)
        return False


def __control_execute(key, driver, element):
    switch_case = {
        "swip": __scroll_screen(driver),
        "click": __click_element(element)
    }
    switch_case.get(key['operate_type'])


def main_operate(driver, platform, **kwargs):
    """
    该方法是测试用例执行时运行的主函数
    :param driver: 初始化设备信息 self.driver
    :param platform: 被测设备系统 android | ios 用以存放到不同的报告目录下
    :param kwargs: 被测元素的嵌套字典集合
    kwargs['position']:element position
    kwargs['find_type']:find_type id or xpath
    kwargs['operate_type']:click
    kwargs['operate_message']:operational information
    kwargs['input_character']:input character
    """
    for key in kwargs:
        new_dic = kwargs[key]

        try:
            logger.info('获取元素信息：%s', new_dic)
            logger.debug('开始执行操作:%s', new_dic['operate_message'])

            # 隐式等待(10秒)，使用隐式等待执行测试的时候，如果WebDriver没有在DOM中找到元素，将继续等待，超出设定时间后将抛出找不到元素的异常
            driver.implicitly_wait(10)

            element = __find_element(driver, platform, new_dic['find_type'], new_dic['position'])

            __control_execute(new_dic, driver, element)

            if new_dic['input_character'] != "":
                __input_character(element, new_dic['input_character'])
                logger.debug('输入了字符：%s', new_dic['input_character'])

            logger.debug('执行%s操作完毕', new_dic['operate_message'])

        except Exception as error:
            logger.error("operate element:%s \nexplain:%s \nexception occurred %s", new_dic['position'],
                         new_dic['operate_message'], error)
            __error_screenshot(driver, operate_directory(
                yaml + platform + '/error_screenshot/') + '/' + get_current_hour_minute() + '_error.png')
            driver.quit()

    return
