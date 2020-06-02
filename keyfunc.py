import sys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import re
import time as t
import Settings as s

LAST_BOT_ELE = ""

class Keyfunc:
    def __init__(self, browser):
        self.chrome_browser = browser

    # function to change savedUserName from Bot to real Name from User
    # define your own change
    def getUserName(self, name):
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if regex.search(name) is None:
            pass

        else:
            for x in s.special_character:
                regext = f'(.*?)\s*\\{x}'
                if re.compile(regext).match(name) is not None:
                    name = re.compile(regext).match(name).group(1)

        if name == "Grüner Mann":
            name = "Marten"

        print(name)
        return name

    # Function for getting user from
    def new_chat(self, user_name):
        # Selecting the new chat search textbox
        new_chat = self.chrome_browser.find_element_by_xpath('//*[@id="side"]/descendant::div[contains(@data-tab, "3")]')
        new_chat.click()

        # Enter the name of chat
        new_chat.send_keys(user_name)

        print(f"start to search for {user_name}")
        for x in range(200):
            try:
                # Select for the title having user name
                user = self.chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
                print(user.get_attribute("title"))
                user.click()
                break
            except NoSuchElementException:
                print('Given user "{}" not found in the contact list'.format(user_name))
                pass
            except Exception as e:
                # Close the browser
                self.chrome_browser.close()
                print(e)
                sys.exit()

    def checkUnread(self):
        unread_users = []
        unread = self.chrome_browser.find_elements_by_class_name('OUeyt')
        #   print(unread)
        for user in unread:
            parent = user.find_element_by_xpath("./../../../../..")
            name = parent.find_element_by_xpath('.//span[@dir="auto"]')
            unread_users.append(name.get_attribute("title"))

        #   print(unread_users)
        return unread_users

    def getlastTextMessage(self, message_list):
        count = -1
        while True:
            try:
                child = message_list[count].find_element_by_xpath('.//span[@dir="ltr"]')
                #          print(child.get_attribute('class'))
                return child
            except NoSuchElementException as se:
                try:
                    child = message_list[count].find_element_by_xpath('.//span[contains(@class, "selectable-text")]')
                    return child

                except NoSuchElementException as se:
                    print("message was not a text message")
            count -= 1

    def getMessage(self):
        #    print("try to get message")
        global LAST_BOT_ELE
        message = self.chrome_browser.find_elements_by_xpath(
            '//*[@id="main"]/descendant::div[contains(@class, "message-in")]')
        #    print(f"found a message{message}")
        #    print(f"data id is {message[-1].get_attribute('data-id')}")
        try:
            if message[-1].get_attribute('data-id') != LAST_BOT_ELE:
                LAST_BOT_ELE = message[-1].get_attribute('data-id')
                print(message[-1].get_attribute('data-id'))
            else:
                return
        except IndexError:
            print("no message received")
            return

        try:
            child = self.getlastTextMessage(message)
            text = child.find_element_by_xpath('./*').text
            print(text)
            return text
        except IndexError:
            print("no message received")
            return

    def clickUser(self, user_name):
        try:
            # Select for the title having user name
            user = self.chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
            user.click()
            return
        except NoSuchElementException as se:
            print("user")
            self.new_chat(user_name)

        except ElementClickInterceptedException:
            print('element not clickable at the moment')
            t.sleep(2)
            self.clickUser(user_name)

    def writeMessageToUser(self, user_name, message):
        self.clickUser(user_name)

        # Typing message into message box

        message_box = self.chrome_browser.find_element_by_xpath(
            '//*[@id="main"]/descendant::div[contains(@data-tab, "1")]')
        message_box.send_keys(message)

        # Click on send button
        message_box = self.chrome_browser.find_element_by_xpath('//*[@id="main"]/descendant::span[@data-icon="send"]')
        message_box.click()
        return message
