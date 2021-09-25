from selenium import webdriver


class song():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\webdriver\chromedriver.exe')

    def play(self, query):
        self.query = query
        self.driver.get(url="https://music.youtube.com/search?q=" + query)
        sng = self.driver.find_element_by_xpath(
            '//*[@id="contents"]/ytmusic-responsive-list-item-renderer/div[2]/div[1]/yt-formatted-string')
        sng.click()

# assist=song()
# assist.play('perfect')
