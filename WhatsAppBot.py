import sys
import time as t
import functions as f

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

user_name_list = ['#Mama']
user_answer_list = ['Minhstdercoolste']

valid_end = ['!end'
]


# Function for getting user from
def new_chat(user_name):
    # Selecting the new chat search textbox
    new_chat = chrome_browser.find_element_by_xpath('//*[@id="side"]/descendant::div[contains(@data-tab, "3")]')
    new_chat.click()

    # Enter the name of chat
    new_chat.send_keys(user_name)

    print(f"start to search for {user_name}")
    for x in range(200):
        try:
            # Select for the title having user name
            user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
            print(user.get_attribute("title"))
            user.click()
            break
        except NoSuchElementException:
            print('Given user "{}" not found in the contact list'.format(user_name))
            pass
        except Exception as e:
            # Close the browser
            chrome_browser.close()
            print(e)
            sys.exit()


def checkUnread():
    unread_users = []
    unread = chrome_browser.find_elements_by_class_name('OUeyt')
    print(unread)
    for user in unread:
        parent = user.find_element_by_xpath("./../../../../..")
        name = parent.find_element_by_xpath('.//span[@dir="auto"]')
        unread_users.append(name.get_attribute("title"))

    print(unread_users)
    return unread_users


def getlastTextMessage(message_list):
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


def getMessage():
#    print("try to get message")
    message = chrome_browser.find_elements_by_xpath('//*[@id="main"]/descendant::div[contains(@class, "message-in")]')
#    print(f"found a message{message}")
#    print(f"data id is {message[-1].get_attribute('data-id')}")

    child = getlastTextMessage(message)
    text = child.find_element_by_xpath('./*').text
 #   print(text)
    return text

def clickUser(user_name):
    try:
        # Select for the title having user name
        user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        user.click()
        return
    except NoSuchElementException as se:
        print("user")
        new_chat(user_name)

    except ElementClickInterceptedException:
        print('element not clickable at the moment')
        t.sleep(2)
        clickUser(user_name)

def writeMessageToUser(user_name, message):
    clickUser(user_name)

    # Typing message into message box

    message_box = chrome_browser.find_element_by_xpath('//*[@id="main"]/descendant::div[contains(@data-tab, "1")]')
    message_box.send_keys(message)

    # Click on send button
    message_box = chrome_browser.find_element_by_xpath('//*[@id="main"]/descendant::span[@data-icon="send"]')
    message_box.click()


# TODO: reply automatically depending on the user input
# TODO: Set a busy or not trigger to run this script

def repeatFunc(user):
    x = ""
    writeMessageToUser(user, "Repeat Funktion wurde gestarted")
    while 1:
            clickUser(user)
            msg = getMessage()
            if msg != x and msg.lower().replace(" ", "") != "!startrepeat":
                if msg.lower().replace(" ", "") in valid_end:
                    writeMessageToUser(user, "Repeat Funktion wurde beendet")
                    return 1
                else:
                    writeMessageToUser(user, msg)
                    x = getMessage()

def getHelp(u):
    writeMessageToUser(u, "Hallo")


def getfunction(message, u):
    x = message.lower().replace(" ", "")
    if x.startswith('!'):
        if x == "!startrepeat":
            repeatFunc(u)
        elif x == "!help":
            getHelp(u)


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=C:\\Users\\Minh\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
    options.add_argument('--profile-directory=Default')

    # Register the drive
    chrome_browser = webdriver.Chrome(
        executable_path=r'C:\Program Files (x86)\Python37-32\Lib\site-packages\chromedriver.exe',
        options=options)  # Change the path as per your local dir.
    chrome_browser.get('https://web.whatsapp.com/')

    # Sleep to scan the QR Code
    for x in range(10000):
        try:
            chat = chrome_browser.find_element_by_xpath('//span[@data-icon="chat"]')
            break
        except NoSuchElementException as se:
            pass

    while 1:
        for user in user_name_list:
            clickUser(user)
            msg = getMessage()
            getfunction(msg, user)




    # unread_users = checkUnread()
    # for user in unread_users:
    #
    #     if user in user_answer_list:
    #         writeMessageToUser(user)
    #     else:
    #         print(f'{user} is no defined user')

#    chrome_browser.close()
