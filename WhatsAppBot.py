import sys
import time as t
import functions as f
import re
import Settings as s
import keyfunc as k
import os

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

FILE_CREATION = os.path.abspath(__file__)


def getBrowser():
    return chrome_browser


if __name__ == '__main__':
    chrome_browser = s.startChrome()
    chrome_browser.get('https://web.whatsapp.com/')
    k = k.Keyfunc(chrome_browser)

    # Sleep to scan the QR Code
    for x in range(10000):
        try:
            chat = chrome_browser.find_element_by_xpath('//span[@data-icon="chat"]')
            break
        except NoSuchElementException as se:
            pass

    f = f.Func(chrome_browser)
    lastmsg = ""
    lastMsgByUser = {}
    while 1:
        unread = k.checkUnread()
        activate = None
        unread_user = k.getActiveChat()
        for user_name in unread:
            if user_name in s.user_answer_list:
                #unread[user_name] = text_value
                activate = f.getFunction(user_name, unread[user_name])
                if activate is not None:
                    if activate in s.funcs:
                        print("user used already func")
                        unread_user = user_name
                        lastMsgByUser[user_name] = activate
                        activate = None
                        break
        else:
            msg = k.getMessage()
            user = k.getActiveChat()
            try:
                if msg is not None and lastMsgByUser[user] != msg.lower().replace(" ", "") and user == unread_user:
                    lastMsgByUser[user] = f.getFunction(user, msg)
            except KeyError:
                if msg.lower().replace(" ", "") in s.funcs:
                    lastMsgByUser[user] = msg

#    chrome_browser.close()
