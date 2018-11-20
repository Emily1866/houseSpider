from scrapy import cmdline

cmdline.execute("scrapy crawl house".split())
# cmdline.execute("scrapy crawl house -o tt.csv -t csv".split())