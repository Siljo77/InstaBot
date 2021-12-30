from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from random import randint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui


class InstaBot():
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome('/Users/ivansijan/Desktop/chromedriver')
       
    def fullSizeScreen(self):  
        bot =self.bot
        bot.maximize_window()
    
    def notification_1(self):
        bot = self.bot
        bot.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
    
    def goToInsta(self):
        bot = self.bot
        bot.get('http://instagram.com')
        
    def login(self):
        bot = self.bot
        bot.find_element_by_name("username").send_keys(self.username)
        bot.find_element_by_name("password").send_keys(self.password + Keys.RETURN)
    
    def notification_2(self):
        bot = self.bot
        ui.WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "cmbtv"))).click() 
        
        
    def notification_3(self):
        bot = self.bot
        not_3 = bot.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')   
        not_3.click()
        
    def person(self,person):
        bot = self.bot
        bot.get("https://www.instagram.com/" + person + '/')
        self.likeFirstPhoto()
        #self.likePhotos()
        
    def likeFirstPhoto(self):
        bot = self.bot
        # open a pikcure
        bot.find_element_by_class_name('v1Nh3').click()
        time.sleep(randint(1,3))
        # like the pikcure
        like = bot.find_element_by_class_name('fr66n')
        like.click()
        time.sleep(randint(1,3))
        # click next pikcure
        bot.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/div/button').click()
     
    def follow(self):
        bot = self.bot
        folow = bot.find_element_by_xpath("/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button")
        folow.click()
        folow_cancle = bot.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[2]")
        folow_cancle.click()
        
    def likePhotos(self,amount):
        bot = self.bot
        
        i = 1
        while i <= amount:
            time.sleep(randint(1,5))
            # like the pikcure a pikcure
            bot.find_element_by_class_name('fr66n').click()
            time.sleep(randint(1,2))
            # folow user
            self.follow()
            time.sleep(randint(1,2))
            # next pikcure
            bot.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/div[2]/button').click()
        
            i += 1
            
            
        
    def hashtag(self,hashtag):
        bot = self.bot
        hashtag = ['pythonprogramming','instabots','bots','vscode'] #'robotica','seleniumwebdriver',
        for has in hashtag:
            bot.get("https://www.instagram.com/explore/tags/" + has + '/')
            time.sleep(randint(1,3))
            self.likeFirstPhoto()
            time.sleep(randint(1,2))
            self.likePhotos(20)
            
    
        bot.get('https://www.instagram.com/' + 'bogda2709')
        
    
insta = InstaBot('robotantonio6','robotantonio66')
insta.fullSizeScreen()

insta.goToInsta()
time.sleep(randint(1,2))

insta.notification_1()
time.sleep(randint(1,3))

insta.login()
time.sleep(randint(1,5))

insta.notification_2()
time.sleep(randint(1,3))

insta.notification_3()
time.sleep(randint(1,3))
#insta.person('bogda2709')
#time.sleep(randint(1,3))
#insta.likeFirstPhoto()
#time.sleep(randint(1,3))
#insta.likePhotos(74)
insta.hashtag('has')
time.sleep(randint(1,3))
#time.sleep(randint(1,3))

    