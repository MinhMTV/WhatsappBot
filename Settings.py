from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

user_name_list = ['#Mama']
user_answer_list = ['Minhstdercoolste', 'My Lan', 'My Linh', '#Mama']

special_character = [r'@', '_', '!', '$', '%', '^', '&', '*', '(', ')', '<', '>', '?', '/', '\\', '|', '}', '{',
                     '~', ': '
                     ]

valid_end = ['!end'
             ]


def startChrome():
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=C:\\Users\\Minh\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
    options.add_argument('--profile-directory=Default')

    # Register the drive
    chrome_browser = webdriver.Chrome(
        executable_path=r'C:\Program Files (x86)\Python37-32\Lib\site-packages\chromedriver.exe',
        options=options)  # Change the path as per your local dir.

    print(type(chrome_browser))
    return chrome_browser
