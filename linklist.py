from selenium import webdriver
from bs4 import BeautifulSoup

URL = 'https://www.xxxx/xxxx{}/'
CSS = 'tr > td.linkWrap.three.twoline > ul > li:nth-of-type(4) > a'

def soup(driver):
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    return soup

if __name__ == '__main__':

    driver = webdriver.PhantomJS()

    for i in range(3, 9):
        driver.get(URL.format(i))
        s = soup(driver)

        for a in s.select(CSS):
            print(a)
