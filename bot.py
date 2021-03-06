import time
import sys
import colorama

from wait import wait_css, wait_xpath
from selenium import webdriver
from __banner.myBanner import bannerTop
from datetime import datetime
import random



class LinkedBOT:
    def __init__(self, email, password, key, geoURN):
        self.email = email
        self.password = password
        self.isLoggedIn = 0
        self.Key = "%20".join(key.split(' '))
        self.geoURN = geoURN
        self.driver = webdriver.Chrome(executable_path=r'./webdriver/chromedriver')
        self.page = 0
        self.successful_invites = 0
        self.__Login()

    def __Login(self):
        self.driver.get('https://www.linkedin.com')
        wait_xpath(self.driver,
                   '//*[@id="session_key"]')
        # entring email and password and clicking login button
        self.driver.find_element_by_xpath('//*[@id="session_key"]').send_keys(self.email)
        self.driver.find_element_by_xpath('//*[@id="session_password"]').send_keys(self.password)
        self.driver.find_element_by_xpath('/html/body/main/section[1]/div[2]/form/button').click()
        wait_css(self.driver, "#global-nav")
        self.isLoggedIn = 1
        print('Logged in successfully! ')

    def __getIdsButtonsOfPage(self):
        ids = []
        wait_xpath(self.driver, '//*[@id="main"]/div/div/div[2]/ul/li[1]/div/div/div[3]')
        ul = self.driver.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/ul')
        for li in ul.find_elements_by_tag_name('li'):
            try:
                btn = li.find_element_by_tag_name("button")
                if "con" in btn.text:
                    ids.append(btn.get_attribute('id'))
            except:
                pass
        return ids

    def __visitNextPage(self):
        self.page += 1
        self.driver.get(
            'https://www.linkedin.com/search/results/people/?geoUrn=' + self.geoURN + '&keywords=' + self.Key + '&origin=FACETED_SEARCH&page=' + str(
                self.page))
        wait_xpath(self.driver, '//*[@id="main"]/div/div/div[2]')
        time.sleep(2)

    def Connect(self, NbrConnects):
        while (NbrConnects > 0):
            self.__visitNextPage()
            Ids = self.__getIdsButtonsOfPage()
            if len(Ids) > 0:
                for id in Ids:
                    if (NbrConnects > 0):
                        time.sleep(random.randint(1, 2))
                        self.driver.find_element_by_xpath('//*[@id="' + id + '"]').click()
                        try:
                            time.sleep(1)
                            modal = self.driver.find_element_by_class_name("artdeco-modal__actionbar")
                            modal.find_elements_by_tag_name("button")[1].click()
                        except:
                            pass
                        time.sleep(1)
                        self.successful_invites += 1
                        print(str(self.successful_invites) + " Invitations sent")
                        NbrConnects -= 1
                    else:
                        break


def __getInterests():
    with open(r'./__constants/InterestsList', "r") as f:
        return f.read().split('\n')


def __getLocalisations():
    with open(r'./__constants/Localisations', "r") as f:
        lines = f.read().split('\n')
    localisations = []
    for line in lines:
        localisations.append(line.split('|')[0])
    return localisations


def __getGeoUrn(localisation):
    with open(r'./__constants/Localisations', "r") as f:
        lines = f.read().split('\n')
    for line in lines:
        if line.split('|')[0] == localisation:
            return line.split('|')[1].strip()


def __getEmail():
    with open(r'./__constants/account', "r") as f:
        return f.read().split('\n')[0]


def __getPassword():
    with open(r'./__constants/account', "r") as f:
        return f.read().split('\n')[1]


def StartBot():
    # declaring vars
    global input
    interests = __getInterests()
    localisations = __getLocalisations()
    email = __getEmail()
    password = __getPassword()
    # banner
    sys.stdout.write(bannerTop())
    print(colorama.Fore.YELLOW)

    # Menu
    

    print("     Interests : ")
    i = 0
    for interest in interests:
        i += 1
        print(str(i) + ")  " + interest)
    input_Interest = input("Select your interest: ")

    print("     Location : ")
    i = 0
    for localisation in localisations:
        i += 1
        print(str(i) + ")  " + localisation)
        
    input_Localisation = input("Select your localization: ")
    usersNum = input("Select the number of users to invite: ")

    # menu end

    geoURN = __getGeoUrn(localisations[int(input_Localisation) - 1])
    print("Bot started at " + datetime.now().strftime("%H:%M:%S"))

    L = LinkedBOT(email, password, interests[int(input_Interest) - 1], geoURN)
    L.Connect(int(usersNum))
    print("Total invites : " + str(L.successful_invites))


if __name__ == '__main__':
    StartBot()
