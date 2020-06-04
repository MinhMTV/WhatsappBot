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
    activate = None
    while 1:
        unread = k.checkUnread()
        for x in unread:
            if x in s.user_answer_list:
                # print(x)
                # print("guckt ob user funktion aktiviert hat")
                activate = f.getFunction(x, unread[x])
                # print(activate)
                # if activate is None:
                #     k.writeMessageToUser(x, "hi")
        if activate is not None:
            if activate in s.funcs:
                print("user used already func")
                lastmsg = activate
                activate = None

        else:
            msg = k.getMessage()
            user = k.getActiveChat()
            if msg is not None and lastmsg != msg:
                f.getFunction(user, msg)
        t.sleep(1)



    # for user in s.user_answer_list:
    #
    #             print("user already ask function")
    #     else:
    #         msg = k.getMessage()
    #         if msg is not None:
    #             f.getFunction(x, msg)


        # for user in unread_users:
        #
        #     if user in user_answer_list:
        #         writeMessageToUser(user,)
        #     else:
        #         print(f'{user} is no defined user')

#    chrome_browser.close()
