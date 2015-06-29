from selenium import webdriver
from bs4 import BeautifulSoup
import csv
from nameparser import HumanName
import ipdb
import time
class BeenVerified:
    def search(self,name):
        name = HumanName(name)
        browser = webdriver.PhantomJS()
        browser.set_window_size(1200,800)
        page_url = 'https://www.beenverified.com/lp/116f02/2/search-results'
        #
        browser.get(page_url)
        search_button = browser.find_element_by_class_name('main-btn')
        fn_field = browser.find_element_by_name('fn')
        fn_field.clear()
        fn_field.send_keys(name.first)
        mi_field = browser.find_element_by_name('mi')
        mi_field.clear()
        ln_field = browser.find_element_by_name('ln')
        ln_field.clear()
        if name.middle.endswith('.'):
            mi_field.send_keys(name.middle[0])
            ln_field.send_keys(name.last)
        elif name.middle:
            ln_field.send_keys(' '.join([name.middle, name.last]))
        else:
            ln_field.send_keys(name.last)



        city_field = browser.find_element_by_name('city')
        city_field.clear()
        city_field.send_keys('Miami')
        age_field = browser.find_element_by_name('age')
        age_field.clear()
        state_field = browser.find_element_by_name('state')
        state_field.send_keys('FL')
        search_button.click()
        browser.implicitly_wait(15)
        time.sleep(15)

        #debug
        browser.save_screenshot(''.join([str(name), '.png']))

        result_set = browser.find_element_by_id('results-table')
        soup = result_set.get_attribute('outerHTML')



        f = open('sample.csv','w')
        a_writter = csv.writer(f)
        fd = open('doc.csv','a')
        b_writter = csv.writer(fd)

        soup = BeautifulSoup(soup)

        for row in soup.findAll("tr"):
            print row
            flag = 0
            alist= []
            items = row.findAll("td")
            for item in items:
                flag+=1
                text = item.text.strip()
                if "THAT'S THE ONE" in text:
                    continue
                text = text.replace("\n","#")
                alist.append(text)

            print flag
            a_writter.writerows([alist])
            alist.insert(0, name)
            print name
            b_writter.writerows([alist])
        f.close()
        fd.close()

        browser.close()
            # elif item.attrs['class'][0] == 'td-hash' :
            #     another_dict[item.attrs['class'][0]] = text.strip()
            # else:
            #     for tag in item.findAll():
            #         try:
            #             another_dict[tag['class'][0]] = tag.text
            #         except KeyError:
            #             # prev = tag.find_previous_sibling().attrs['class'][0]
            #             # if prev == 'aka-list-heading' and flag==0 :
            #             #     another_dict[prev] = tag.text
            #             #     flag = 1
            #             # elif flag==1:
            #             #     another_dict['address'] = tag.text
            #             ipdb.set_trace()
            #             print tag.text
            #             # continue
            #         else:
            #             print 'Hello world'
            #             # if tag.parent['class'][0] == 'aka-list':
            #             #     another_dict[tag.parent['class'][0]] = another_dict[tag.parent['class'][0]] +' '+ tag.text
            #             # print KeyError
            #             # print tag
            #             # ipdb.set_trace()
            #
            #
            #
            # print another_dict
            #

            # ipdb.set_trace()

