import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

URL = 'https://xxxxxx'
CSS1 = 'ul:nth-child(2) > li:nth-child(1) > table > tbody > tr > td.'
CSS2 = 'ul:nth-child(2) > li:nth-child(2) > table > tbody > tr > td.'
CSS3 = 'ul:nth-child(4) > li:nth-child(1) > table > tbody > tr > td.'
CSS4 = 'ul:nth-child(4) > li:nth-child(2) > table > tbody > tr > td.'
CSS = CSS4

def soup(driver):
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    return soup

def posts(driver, css):
    posts = []
    for a in driver.find_elements_by_css_selector(css):
        posts.append(a.text)
    return posts

def scrape_posts(driver, css):
    cols = ['num', 'pos', 'time', 'name', 'data']
    df = pd.DataFrame()

    for col in cols:
        post = posts(driver, css + col)
        df[col] = post
    
    return df

if __name__ == '__main__':

    driver = webdriver.PhantomJS()
    driver.get(URL)
    df = scrape_posts(driver, CSS)
    print(df)
