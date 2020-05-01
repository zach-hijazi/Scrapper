from bs4 import BeautifulSoup
import requests
import pdb

class TwitterScrapper:

    def __init__(self):
        param1 = "ethereum"
        param2 = "enterprise"
        param3 = "alliance"
        self.start_url = f"https://twitter.com/search?q={param1}%20{param2}%20{param3}&src=typed_query&f=live"

        self.tweets = []
        self.counter = 1

    def scrape(self):

        self.url = self.start_url



        # If no more new pages, exit
        #if not self.url:
        #    break

        self.page = requests.get(self.url)
        # get formatted version of page content
        self.content = BeautifulSoup(self.page.content, 'html.parser')

        # parse content
        pdb.set_trace()
        results = self.content.find_all('span.css-901oao')
        results = self.content.find_all('div', {'class': 'css-1dbjc4n'})
        pdb.set_trace()
        for result in results:
            pdb.set_trace()



if __name__ == "__main__":
    # run scrapper
    scapper = TwitterScrapper()
    scapper.scrape()
