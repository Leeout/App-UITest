"""命令行执行测试脚本入口"""
import sys
import getopt

from common.logger import logger
from common.operate_directory import operate_directory

import testIOS.test_student_client as student_client


def __usage():
    """命令行使用帮助"""
    doc = """
测试脚本
Args:
    -h, --help                 显示帮助
    
    -r, --run=                 运行测试, 可选值
                            -- ipad             ios学生端测试用例
                            -- iphone           ios家长端测试用例
                            -- android          android家长端测试用例
    """
    logger.info(doc)


def __run_case(value):
    """
    :param value: 测试用例的集合名
    :return:
    """
    file_path = operate_directory('report/' + value + '/html_report/')
    if value == 'ipad':
        student_client.run_suite(file_path)


def __handle(opts):
    try:
        for command, value in opts:
            if command in ('-h', '--help'):
                __usage()
                return

            if command in ('-r', '--run'):
                if value not in ('ipad', 'ios', 'android'):
                    logger.error('输入的第二个参数有误！请检查该参数是否包含在允许运行的合集里，使用--help获取帮助！')
                    return
                __run_case(value)
                return

    except Exception as err:
        logger.error('Exception: %s', str(err))
        return


def main():
    """Main Function"""
    cmd_params = sys.argv[1:]
    logger.warning('脚本入参为:%s', cmd_params)

    try:
        opts, args = getopt.gnu_getopt(cmd_params, 'hr:', ['help', 'run='])
        logger.warning('有效命令为:%s', opts)
        __handle(opts)

    except Exception as err:
        logger.error('错误原因：%s \n 使用 --help获取帮助', err)
        return


if __name__ == '__main__':
    sys.exit(main())
