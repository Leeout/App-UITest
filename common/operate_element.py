"""
该文件是操作设备的一系列方法封装
todo:1.滑屏  2.webview内识别元素
"""
import os

from common.logger import logger
from common.time_base import get_current_time

get_file = os.path
path = get_file.dirname(get_file.realpath(__file__))
yaml = get_file.join(path, "../report/screenshot/")


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


def __scroll_screen(driver, duration='right', number=2):
    """
    todo:该方法用于滑屏操作
    :param driver: 初始化设备信息 self.driver
    :param duration: 滑动持续时长
    :param number: 滚动的次数 默认滑动 次
    """
    try:
        logger.info('开始滑动屏幕......')
        # 滑屏第一种方法：
        # TouchAction(driver).press(x=1, y=395).move_to(x=5, y=419).release().perform()

        # 滑屏第二种方法：
        for i in range(number):
            driver.execute_script("mobile: swipe", {"direction": duration})
            logger.info('已滑动屏幕：%s', i + 1)
        return

        # 滑屏第三种方法：
        # size = driver.get_window_size()
        # logger.debug('设备尺寸：%s', size)
        # x1 = int(size['width'] * 0.75)
        # y1 = int(size['height'] * 0.5)
        # x2 = int(size['width'] * 0.25)
        # for i in range(number):
        #     driver.swipe(x1, y1, x2, y1, duration)
        #     logger.info('已滑动屏幕：%s次', i + 1)

    except Exception as error:
        logger.error("scroll screen exception: %s", error)
        return


def __find_element(driver, platform, find_type, element_position):
    """
    该方法用于识别元素
    :param driver: 初始化设备信息 self.driver
    :param find_type: 获取元素方式
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
        logger.error('find element fail %s', error)
        return


def operate_element(driver, platform, **kwargs):
    """
    该方法封装了：识别元素、点击元素、发送字符 操作方法
    :param driver: 初始化设备信息 self.driver
    :param platform: 被测设备系统 android | ios 用以存放到不同的报告目录下
    :param kwargs: 被测元素的嵌套字典集合
    kwargs['position']:element position
    kwargs['find_type']:find_type id or xpath
    kwargs['operate_type']:click
    kwargs['operate_message']:operational information
    kwargs['input_character']:input character
    :return:
    """
    for key in kwargs:
        new_dic = kwargs[key]

        try:
            if new_dic is not None:
                logger.info('获取元素信息：%s', new_dic)
                logger.debug('开始执行操作:%s', new_dic['operate_message'])
                # 隐式等待，使用隐式等待执行测试的时候，如果WebDriver没有在DOM中找到元素，将继续等待，超出设定时间后将抛出找不到元素的异常
                driver.implicitly_wait(10)  # 设置10秒时间等待

                element = __find_element(driver, platform, new_dic['find_type'], new_dic['position'])

                if 'click' in new_dic['operate_type']:
                    element.click()
                    logger.debug('点击了元素：%s', new_dic['position'])

                if new_dic['input_character'] != "":
                    element.send_keys(new_dic['input_character'])
                    logger.debug('输入了字符：%s', new_dic['input_character'])
                logger.debug('执行%s操作完毕', new_dic['operate_message'])

        except Exception as error:
            logger.error("operate element:%s\nexplain:%s\nexception occurred %s", new_dic['position'],
                         new_dic['operate_message'], error)
            driver.get_screenshot_as_file( yaml + platform + '/error_' + get_current_time() + '.png')
            logger.warning('当前生成了一张错误截图!')
            driver.quit()

    return
