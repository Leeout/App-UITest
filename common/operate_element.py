"""
该文件是操作设备的一系列方法封装
todo:
1.webview内识别元素 --已完成 存在小问题 要看下
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
        logger.warning('正在尝试关闭系统权限申请弹窗......')
        while True:
            # if "不允许" in driver.page_source or "Don't Allow" in driver.page_source:
            driver.switch_to.alert.accept()
            logger.debug('已关闭系统权限申请弹窗！')
            break

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
    return element.click()


def __input_character(element, character):
    """
    该方法用于在输入框内输入字符
    :param element: 找到的元素
    :param character: 输入的字符
    """
    return element.send_keys(character)


def __error_screenshot(driver, screenshot_path):
    """
    该方法用于抛异常时截取屏幕
    :param driver: 初始化设备信息 self.driver
    """
    driver.get_screenshot_as_file(screenshot_path)
    logger.warning('当前生成了一张错误截图!')
    return


def __operate_webview(driver, is_switch):
    """
    该方法用于进入webview
    :param driver: 初始化设备信息 self.driver
    :param is_switch: 控制切换webview、native 1:webview || 0:native
    """
    try:
        contexts = driver.contexts
        driver.switch_to.context(contexts[is_switch])
        logger.debug('当前所处:%s'), driver.current_context
        return True

    except Exception as error:
        logger.error("operate webview fail: %s", error)
        return False


def __control_execution(driver, element_key):
    return __scroll_screen(driver) if element_key['operate_type'] == 'swip' else __operate_webview(driver, element_key[
        'position'])


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
        element_key = kwargs[key]

        try:
            logger.debug('获取元素字典:%s \n开始执行操作:%s', element_key, element_key['operate_message'])

            # 隐式等待(15秒)，隐式等待执行测试的时候，如果WebDriver没有在DOM中找到元素，将继续等待，超出设定时间后将抛出找不到元素的异常
            driver.implicitly_wait(20)

            if element_key['operate_type'] in ('swip', 'webview'):
                __control_execution(driver, element_key)
                continue

            element = __find_element(driver, platform, element_key['find_type'], element_key['position'])

            __click_element(element)
            logger.debug('点击了:%s', element_key['position'])

            if element_key['input_character'] != "":
                __input_character(element, element_key['input_character'])
                logger.debug('输入了字符：%s', element_key['input_character'])

            logger.debug('执行%s操作完毕', element_key['operate_message'])

        except Exception as error:
            logger.error("operate element:%s \nexplain:%s \nexception occurred:%s", element_key['position'],
                         element_key['operate_message'], error)
            __error_screenshot(driver, operate_directory(
                yaml + platform + '/error_screenshot/') + '/' + get_current_hour_minute() + '_error.png')
            driver.quit()

    return
