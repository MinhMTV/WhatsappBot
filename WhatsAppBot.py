import sys
import time as t
import functions as f
import re
import Settings as s
import keyfunc as k

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException


# global LAST_BOT_MSG
# LAST_BOT_ELE = ""


# # function to change savedUserName from Bot to real Name from User
# # define your own change
# def getUserName(name):
#     regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
#     if regex.search(name) is None:
#         pass
#
#     else:
#         for x in special_character:
#             regext = f'(.*?)\s*\\{x}'
#             if re.compile(regext).match(name) is not None:
#                 name = re.compile(regext).match(name).group(1)
#
#     if name == "Grüner Mann":
#         name = "Marten"
#
#     print(name)
#     return name
#
#
# # Function for getting user from
# def new_chat(user_name):
#     # Selecting the new chat search textbox
#     new_chat = chrome_browser.find_element_by_xpath('//*[@id="side"]/descendant::div[contains(@data-tab, "3")]')
#     new_chat.click()
#
#     # Enter the name of chat
#     new_chat.send_keys(user_name)
#
#     print(f"start to search for {user_name}")
#     for x in range(200):
#         try:
#             # Select for the title having user name
#             user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
#             print(user.get_attribute("title"))
#             user.click()
#             break
#         except NoSuchElementException:
#             print('Given user "{}" not found in the contact list'.format(user_name))
#             pass
#         except Exception as e:
#             # Close the browser
#             chrome_browser.close()
#             print(e)
#             sys.exit()
#
#
# def checkUnread():
#     unread_users = []
#     unread = chrome_browser.find_elements_by_class_name('OUeyt')
#  #   print(unread)
#     for user in unread:
#         parent = user.find_element_by_xpath("./../../../../..")
#         name = parent.find_element_by_xpath('.//span[@dir="auto"]')
#         unread_users.append(name.get_attribute("title"))
#
#  #   print(unread_users)
#     return unread_users
#
#
# def getlastTextMessage(message_list):
#     count = -1
#     while True:
#         try:
#             child = message_list[count].find_element_by_xpath('.//span[@dir="ltr"]')
#             #          print(child.get_attribute('class'))
#             return child
#         except NoSuchElementException as se:
#             try:
#                 child = message_list[count].find_element_by_xpath('.//span[contains(@class, "selectable-text")]')
#                 return child
#
#             except NoSuchElementException as se:
#                 print("message was not a text message")
#         count -= 1
#
#
# def getMessage():
#     #    print("try to get message")
#     global LAST_BOT_ELE
#     message = chrome_browser.find_elements_by_xpath('//*[@id="main"]/descendant::div[contains(@class, "message-in")]')
#     #    print(f"found a message{message}")
#     #    print(f"data id is {message[-1].get_attribute('data-id')}")
#     try:
#         if message[-1].get_attribute('data-id') != LAST_BOT_ELE:
#             LAST_BOT_ELE = message[-1].get_attribute('data-id')
#             print(message[-1].get_attribute('data-id'))
#         else:
#             return
#     except IndexError:
#         print("no message received")
#         return
#
#     try:
#         child = getlastTextMessage(message)
#         text = child.find_element_by_xpath('./*').text
#         print(text)
#         return text
#     except IndexError:
#         print("no message received")
#         return
#
#
# def clickUser(user_name):
#     try:
#         # Select for the title having user name
#         user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
#         user.click()
#         return
#     except NoSuchElementException as se:
#         print("user")
#         new_chat(user_name)
#
#     except ElementClickInterceptedException:
#         print('element not clickable at the moment')
#         t.sleep(2)
#         clickUser(user_name)
#
#
# def writeMessageToUser(user_name, message):
#     clickUser(user_name)
#
#     # Typing message into message box
#
#     message_box = chrome_browser.find_element_by_xpath('//*[@id="main"]/descendant::div[contains(@data-tab, "1")]')
#     message_box.send_keys(message)
#
#     # Click on send button
#     message_box = chrome_browser.find_element_by_xpath('//*[@id="main"]/descendant::span[@data-icon="send"]')
#     message_box.click()
#     return message

# def noticeAllUser():
#     for u in user_answer_list:
#         t.sleep(2)
#         writeMessageToUser(u, f"Hallo {getUserName(u)}")
#         writeMessageToUser(u, f"Mein Name ist Chris und ich bin ein WhatsApp-Bot programmiert von meinem Erfinder, dem sensationellen *Minh*")
#         writeMessageToUser(u, f"Erfahre mehr über mich mit dem Befehl *!Bot*")
#         writeMessageToUser(u, f"Lerne alle meine Funktionen kennen mit dem Befehl *!Help*")
#         writeMessageToUser(u, f"Erfahre mehr über Minh, dem Erfinder mit dem Befehl *!Minh*")
#
#
# # TODO: reply automatically depending on the user input
# # TODO: Set a busy or not trigger to run this script
#
# def repeatFunc(user):
#     global LAST_BOT_MSG
#     x = ""
#     LAST_BOT_MSG = writeMessageToUser(user, "Repeat Funktion wurde gestarted")
#     while 1:
#         msg = getMessage()
#         try:
#             if msg != x and msg.lower().replace(" ", "") != "!startrepeat":
#                 if msg.lower().replace(" ", "") in valid_end:
#                     writeMessageToUser(user, "Repeat Funktion wurde beendet")
#                     return 1
#                 else:
#                     writeMessageToUser(user, msg)
#                     x = getMessage()
#         except AttributeError:
#             pass
#
#
# def getHelp(u):
#     writeMessageToUser(u, f"Hallo {getUserName(u)}")
#     writeMessageToUser(u, f"Mein Bot hat einige Funktionen, die du durch eine TextNachricht aktivieren kannst")
#     writeMessageToUser(u, f"1.")
#     writeMessageToUser(u, f"*!Start Repeat*")
#     writeMessageToUser(u, f"Wiederholt jedes Wort, welches du mir schreibst. Beenden kannst du die Funktion mit dem Befehl: *!End*")
#
#     return
#
#
# def getfunction(message, u):
#     x = message.lower().replace(" ", "")
#     if x.startswith('!'):
#         if x == "!startrepeat":
#             repeatFunc(u)
#         elif x == "!help":
#             getHelp(u)

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
    f.noticeAllUser()

    while 1:
        for user in s.user_name_list:
            k.clickUser(user)
            msg = k.getMessage()
            if msg is not None:
                f.getfunction(msg, user)

        unread_users = k.checkUnread()
        # for user in unread_users:
        #
        #     if user in user_answer_list:
        #         writeMessageToUser(user,)
        #     else:
        #         print(f'{user} is no defined user')

#    chrome_browser.close()
