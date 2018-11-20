# -*- coding: utf-8 -*-

import csv

class CSVWithEncodingHousePipeline(object):

    def process_item(self,item, spider):
        # print(item['house_name'], item['house_address'], item['house_price'], item['house_url'])
        with open('tt.csv', 'a+', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, dialect='excel')
            writer.writerow((item['house_name'], item['house_address'], item['house_price'], item['house_url']))

        return item


