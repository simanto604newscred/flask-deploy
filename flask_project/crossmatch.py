import urllib2
import nltk
from bs4 import BeautifulSoup

class CrossMatch:



    def match(self,url):
        # url = 'http://www.legacy.com/obituaries/herald/obituary.aspx?n=DAVID-BALOGH&pid=175028004'
        response = urllib2.urlopen(url)
        soup = response.read()
        soup = BeautifulSoup(soup)
        item = soup.find(class_='ObitTextHtml')
        item = item.text
        end = item.find('(function()')
        text = item[:end]
        # alist_to_be_matched = 'Andrew Balogh#Cara Hope Balogh#David R Balogh#Sallie R Balogh#Robert B Balough'.split('#')
        # score = self.extract_entities(item, alist_to_be_matched)
        # # url = 'http://www.legacy.com/obituaries/herald/obituary.aspx?n=DAVID-BALOGH&pid=175028004'
        #
        # response = urllib2.urlopen()
        # text = '''
        # BALOGH, DAVID, a resident of Miami Beach for nearly seventy years and founder of Balogh Jewelers, passed away peacefully on June 4, 2015. He was surrounded by loved ones in the comfort of his home. Just a month short of his ninety-fifth birthday, David led an incredibly full life that reflected the American Dream in every respect. Starting from scratch and surviving World War II, he became a world-class jeweler and an icon of Miami Beach society. Born in Astoria, Queens on July 7, 1920, David met his beloved wife, Sallie, at the tender age of fifteen. In 1945, after the war ended, he and Sallie moved to Miami Beach where they created the legendary Balogh Jewelers. In addition to thriving as a world class jeweler and a real estate developer, David excelled as a musician. A virtuoso on the piano and a genius on the flute, he played first flutist in the Miami Beach Symphony Orchestra. Among all his achievements, David felt proudest of his family whom he adored. He spent many loving years with his daughter, Joan Erdheim, and son, Bobby Balogh. David is also survived by his adoring son-in-law, Marty Erdheim, daughter-in-law, Cara Balogh, and four grandchildren for whom he had endless love: Cara Erdheim; Anna Henschel; Andrew Balogh; and Alexandra Balogh. He spent the later years with Monique Beaudet, an extremely devoted companion whom he loved dearly. A heartfelt thank you also to William Murray, a most dedicated caretaker who became a truly loyal friend to David. We are forever indebted to Nancy Petroza, Patricia Hart, Ann Marie Miller, Monica Elliott, Dr. Georgi Miller, Dr. Peter Segall, and Dr. Seymour Nash for their love and kindness. Funeral Services will be held 12:30 PM Monday, June 8 at Temple Beth Shalom in Miami Beach, with private burial to follow. In lieu of flowers, donations may be made to research for Alzheimer's, Cancer, Diabetes, or a
        # '''
        print 'notice*******'+text
        return text


    def extract_entities(self, text, list_to_be_matched):
        score = 0
        for sent in nltk.sent_tokenize(text,language='english'):
            try:
                for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
                    if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
                        for ele in chunk.leaves():
                            if ele[0] in ' '.join(list_to_be_matched):
                                score=score+1
            except UnicodeDecodeError:
                continue
        return score






