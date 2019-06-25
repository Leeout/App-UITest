"""命令行执行测试脚本入口"""
import sys
import getopt

from common.logger import logger
import testIOS.test_student_client as student_client


def __usage():
    """命令行使用帮助"""
    doc = """
测试脚本
Args:
    -h, --help                 显示帮助
    
    -r, --run=                 运行测试, 可选值
                            -- ipad             iOS学生端测试用例
                            -- ios              ios家长端测试用例
                            -- android          android家长端测试用例
    """
    logger.info(doc)


def __run_case(value):
    """
    :param value: 测试用例的集合名
    :return:
    """
    file_path = 'report/html_report/'
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
                else:
                    __run_case(value)
                    return

    except Exception as err:
        logger.error('Exception: %s', str(err))
        return


def main():
    """Main Function"""
    cmd_params = sys.argv[1:]
    logger.warning('cmd_params:%s', cmd_params)

    try:
        opts, args = getopt.gnu_getopt(cmd_params, 'hr:', ['help', 'run='])
        logger.warning('opts:%s', opts)
        logger.warning('args:%s', args)
        __handle(opts)

    except Exception as err:
        logger.error('错误原因：%s \n 使用 --help获取帮助', err)
        return


if __name__ == '__main__':
    sys.exit(main())
