from selenium import webdriver

class music():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\webdriver\chromedriver.exe')

    def play(self , query):
        self.query =query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        vedio =self.driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
        vedio.click()

#assist=music()
#assist.play('dynamite by bts')
