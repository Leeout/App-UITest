"""获取测试用例的结果数据，case_total:%s | success:%s | failures:%s | errors:%s"""
from common.time_base import get_today_date


def get_report_data(file_name, case):
    """
    :param file_name:推送消息的标题
    :param case:测试结果
    :return:返回测试结果里具体的数据 格式为 case_total:%s | success:%s | failures:%s | errors:%s
    """
    head_title = '#### App UI Auto Test Report For %s' % get_today_date()
    body_title = file_name.split('.')[0]
    result = head_title + '\n - ' + body_title + '  | case_total:%s | success:%s | failures:%s | errors:%s  \n ' % (
        case.success_count + case.failure_count + case.error_count, case.success_count, case.failure_count,
        case.error_count)
    return result
