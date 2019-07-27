"""
该文件封装了钉钉消息通知的方法
"""
from dingtalkchatbot.chatbot import DingtalkChatbot


def ding_message_push(open_api, title, text):
    """
    :param open_api: 消息接受群组的接口
    :param title: 消息的标题
    :param text: markdown格式的消息内容
    :return: 返回消息发送结果
    """
    chat_bot = DingtalkChatbot(open_api)
    chat_bot.send_markdown(title=title, text=text)
