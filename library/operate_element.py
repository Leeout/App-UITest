# -*- coding: utf-8 -*-
"""
封装 识别元素、点击元素、发送字符的操作方法
"""
import os
from logger import logger
from time_base import get_current_time

get_file = os.path
path = get_file.dirname(get_file.realpath(__file__))
yaml = get_file.join(path, "../testReport/error_screenshot/")


def operate_element(driver, **kwargs):
    """
    :param driver: 初始化设备信息 self.driver
    :param kwargs:
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

                if 'xpath' in new_dic['find_type']:
                    element = driver.find_element_by_xpath(new_dic['position'])
                else:
                    element = driver.find_element_by_id(new_dic['position'])

                if 'click' in new_dic['operate_type']:
                    element.click()
                    logger.debug('点击了元素：%s', new_dic['position'])

                if new_dic['input_character'] != "":
                    element.send_keys(new_dic['input_character'])
                    logger.debug('输入了字符：%s', new_dic['input_character'])
                logger.debug('执行%s操作完毕', new_dic['operate_message'])

        except Exception as error:
            logger.error("operation exception: %s", error)
            driver.get_screenshot_as_file(yaml + 'error_' + get_current_time() + '.png')

    return
