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
        ui.WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.CLASS_NAME, "cmbtv"))).click() 
        
        
    def notification_3(self):
        bot = self.bot
        ui.WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.CLASS_NAME, "aOOlW.HoLwm"))).click() 
        
        
    def person(self,person):
        bot = self.bot
        bot.get("https://www.instagram.com/" + person + '/')
        self.likeFirstPhoto()
        #self.likePhotos()
       
                                   
    def follow(self):
        bot = self.bot
        # follow the users
        try:
            follow_button = bot.find_element_by_class_name("sqdOP.yWX7d.y3zKF")
            follow_button.click()
        except:
             pass
    
    
    def like(self):
        bot = self.bot
         # like the pikcures
        try:
            like_if = bot.find_element_by_class_name("QBdPU.rrUvL")
            like_if.click()
        except:
             pass
         
         
    def likeFirstPhoto(self):
        bot = self.bot
        # open a pikcure
        open_pikcure =bot.find_element_by_class_name('v1Nh3')
        open_pikcure.click()
        time.sleep(randint(1,3))
        # like the pikcure
        self.like()
        time.sleep(randint(1,3))
        # follow
        self.follow()
        time.sleep(randint(1,3))
        # click next pikcure
        next_pikcure = bot.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/button")
        next_pikcure.click()
        
       
        
    def likePhotos(self,amount):
        bot = self.bot
        time.sleep(randint(1,2))
        i = 1
        while i <= amount:
            time.sleep(randint(1,5))
            # like the pikcure 
            self.like()
            time.sleep(randint(1,2))
            # folow user
            self.follow()
            time.sleep(randint(1,2))
            # next pikcure
            next = bot.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[2]/button')
            next.click()
            
            i += 1
            
            
    def hashtag(self,hashtag):
        bot = self.bot
        # hashtags list
        hashtag = ['seleniumwebdriver','pythonprogramming','instabots','bots',] #'robotica','seleniumwebdriver','pythonprogramming','instabots','bots',
        for has in hashtag:
            time.sleep(randint(1,3))
            
            # go to every hastag in the list
            bot.get("https://www.instagram.com/explore/tags/" + has + '/')
            time.sleep(randint(1,3))
            self.likeFirstPhoto()
            time.sleep(randint(1,3))
            self.likePhotos(20)
            
    
        bot.get('https://www.instagram.com/' + 'robotantonio6')
        
        
    def get_names(self):
        bot = self.bot
        pop_up_window = WebDriverWait(bot, 4).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='isgrP']")))

        # scroll the pop_up_window window to the end of the list
        last_ht, ht = 0,1
        while last_ht != ht:
            last_ht = ht
            time.sleep(randint(1,2))
            ht = bot.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, pop_up_window)
            
        # finde all the tags in the followers list
        links = pop_up_window.find_elements_by_tag_name("a")
        
        # put all the names in the names list 
        names = [name.text for name in links if name.text != '']
        return names
    
    
    def get_unfollowers(self):
        bot = self.bot
        bot.get('https://www.instagram.com/' + 'robotantonio6')
        
        # open a window with followers
        bot.find_element_by_partial_link_text("followers").click()
        follovers = self.get_names()
        
        bot.get('https://www.instagram.com/' + 'robotantonio6')
        
        #open a window with following
        bot.find_element_by_partial_link_text("following").click()
        following = self.get_names()
        
        # check which users are not following back
        self.not_following_back = [user for user in following if user not in follovers]
        print(self.not_following_back)
        

    def unfollow(self):
        bot = self.bot
        
        self.not_following_back
        
        for user in self.not_following_back:
            time.sleep(randint(1,3))
            
            # open every user which is not following back
            bot.get('https://www.instagram.com/' + user)
            
            # open unfollow window
            unfollow_button = bot.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button/div/span")
            unfollow_button.click()
            time.sleep(randint(1,3))
            
            # unfollow user
            unfollow = bot.find_element_by_class_name("aOOlW.-Cab_")
            unfollow.click()
            
        
insta = InstaBot('robotantonio6','robotantonio66')
#insta = InstaBot('ivan.sijan@gmail.com','Medvescak77')
insta.fullSizeScreen()

insta.goToInsta()
time.sleep(randint(1,2))

insta.notification_1()
time.sleep(randint(1,3))

insta.login()
time.sleep(randint(1,3))

insta.notification_2()
time.sleep(randint(1,3))

insta.notification_3()
time.sleep(randint(1,3))

#insta.get_unfollowers()
#time.sleep(randint(1,3))

#insta.unfollow()
#time.sleep(randint(1,3))

insta.hashtag('has')
time.sleep(randint(1,3))

#insta.person('bogda2709')
#time.sleep(randint(1,3))






    