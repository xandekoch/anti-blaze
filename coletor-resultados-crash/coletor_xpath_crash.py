import cv2
from mss import mss
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

last_crash_xpath = '//*[@id="crash-recent"]/div[2]/div[2]/span[1]'

# Open Browser
options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.get('https://blaze.com/pt/games/crash')


def get_result():
    time.sleep(1)
    last_crash = browser.find_element_by_xpath(last_crash_xpath).text.replace('X', '')

    #anotar string num .txt
    with open('database.txt', 'a') as file:
        A = time.ctime().split()
        hora, dia_mes, mes, dia_semana = A[3], A[2], A[1], A[0]
        file.write(f'{last_crash} - {hora} - {dia_mes} - {mes} - {dia_semana}\n')
        print(f'{last_crash} - {hora} - {dia_mes} - {mes} - {dia_semana}')
        file.close()

    time.sleep(5)


while True:
    red_pixel = ''
    
    while red_pixel != '[ 76  44 241]':
        mss().shot(output='fullscreen.png')
        sct = cv2.imread('fullscreen.png')
        red_pixel = str(sct[410, 840])
        time.sleep(0.5)
    else:
        get_result()