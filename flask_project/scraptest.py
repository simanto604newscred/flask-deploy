from urllib import urlencode
from selenium import webdriver
import time
import csv
from bs4 import BeautifulSoup
def main():

    payload = {'daterange': '7', 'countryid': '1', 'stateid': '12', 'affiliateid': '150'}

    page_url = ''.join(['http://www.legacy.com/obituaries/herald/obituary-search.aspx?',urlencode(payload)])
    print(page_url)


    browser = webdriver.Firefox()
    browser.get(page_url)
    total_count = browser.find_element_by_class_name('InlineTotalCount')
    total_count = total_count.text.encode('utf-8')
    total_count = total_count.split()
    total_count = int(total_count[4])

    number_of_scroll = 0

    if total_count > 10 :
        number_of_scroll = total_count / 10

    while number_of_scroll > 0:

        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        number_of_scroll = number_of_scroll-1


    contents = browser.find_elements_by_css_selector('div.obitName')


    f = open('test.csv','w')
    for content in contents:
        soup = content.get_attribute('innerHTML')
        soup = BeautifulSoup(soup)
        tag = soup.a
        a_writter = csv.writer(f)
        a_writter.writerows([[content.text, tag['href']]])

    f.close()
        # content.click()
        # browser.page_source

    browser.close()


if __name__ == '__main__':
    main()
