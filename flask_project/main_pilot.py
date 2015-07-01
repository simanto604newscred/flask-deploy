from scraptest import Legacy
import csv, os
import operator
from beenVerified import BeenVerified
from crossmatch import CrossMatch

class MainPilot:
    def run(self):
        legacy_search = Legacy()
        legacy_search.search()
        f = open('result.csv','w')
        a_writter = csv.writer(f)
        been_verified = BeenVerified()
        try:
            os.remove('doc.csv')
        except OSError:
            pass
        with open('test.csv', 'rb') as csvfile:
            testreader = csv.reader(csvfile)
            for row in testreader:
                print row
                been_verified.search(row[0])
                result_dict = {}

                with open('sample.csv', 'rb') as another_csvfile:
                    sample_reader= csv.reader(another_csvfile)
                    for index,row_in_sample in enumerate(sample_reader):
                        print row_in_sample
                        crossmatch = CrossMatch()
                        obituary = row[2]
                        try:
                            if row_in_sample[4]:
                                score = crossmatch.extract_entities(obituary, row_in_sample[4].split('#'))
                                print score
                                if score:
                                    result_dict[index] = [score,row_in_sample]

                        except IndexError:
                            continue

                    if bool(result_dict):
                        dict_key = max(result_dict.iteritems(), key=operator.itemgetter(1))[0]
                        a_writter.writerows([result_dict[dict_key][1]])
                        print "One result written"

                print '***********One iteration finished break************'














