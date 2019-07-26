"""获取测试用例的结果数据，case_total:%s | success:%s | failures:%s | errors:%s"""


def get_report_data(file_name, case):
    """
    :param file_name:推送消息的标题
    :param case:测试结果
    :return:返回测试结果里具体的数据 格式为 case_total:%s | success:%s | failures:%s | errors:%s
    """
    body_title = file_name.split('.')[0]
    success_count = case.success_count
    failure_count = case.failure_count
    error_count = case.error_count
    case_count = success_count + failure_count + error_count
    head_title = '### App UI Auto Test'
    return head_title + '\n > ' + body_title + '  | case_total:%s | success:%s | failures:%s | errors:%s  \n ' % (
        case_count, success_count, failure_count, error_count)
