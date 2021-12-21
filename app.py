from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

username = 'robotrobi010192@gmail.com'
password = 'Robotrobi92'


class InstaBot():
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome("C:/Users/IvanSijan/Downloads/chromedriver_win32/chromedriver.exe")
        
    
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
        time.sleep(3)
    
    def notification_2(self):
        bot = self.bot
        bot.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
        
    def hashtag(self,hashtag):
        bot = self.bot
        bot.get("https://www.instagram.com/explore/tags/" + hashtag + '/')
        
        
        
    def person(self,person):
        bot = self.bot
        bot.get("https://www.instagram.com/" + person + '/')
        
        
    def likeFirstPhoto(self):
        bot = self.bot
        bot.find_element_by_class_name('v1Nh3').click()
        time.sleep(1)
        bot.find_element_by_class_name('fr66n').click()
        time.sleep(1)
        bot.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/div/button').click()
        
        
    def likephotos(self,amount):
        bot = self.bot
        
        i = 1
        while i <= amount:
            time.sleep(1)
            bot.find_element_by_class_name('fr66n').click()
            bot.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/div[2]/button').click()
        
            i += 1
            
        bot.get('https://www.instagram.com/' + self.username)
        
        
insta = InstaBot('robotrobi010192@gmail.com','Robotrobi92')
insta.goToInsta()
time.sleep(2)
insta.notification_1()
time.sleep(1)
insta.login()
time.sleep(2)
insta.notification_2()
time.sleep(1)
insta.person('andrea_britvec')
time.sleep(2)
#insta.hashtag("newyork")
#time.sleep(1)
insta.likeFirstPhoto()
time.sleep(1)
insta.likephotos(11)
    