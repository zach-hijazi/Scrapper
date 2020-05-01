from bs4 import BeautifulSoup
import requests
import pdb

class WebScrapper:

    def __init__(self):

        self.start_url = "https://coinmarketcap.com/"

        self.cryptos = []
        self.counter = 1

    def scrape(self):

        self.url = self.start_url

        while True:
            
            # If no more new pages, exit
            if not self.url:
                break

            self.page = requests.get(self.url)
            # get formatted version of page content
            self.content = BeautifulSoup(self.page.content, 'html.parser')

            # parse content
            result = self.content.find_all('a', title=True)
            for alt in result:
                self.cryptos.append(alt.text)

            new_page = self.getNextPage()
            self.url = self.new_url
        print(self.cryptos)

    def getNextPage(self):
        # determine if a next page exists, if so return page url, else return false
        headerDiv = self.content.find('div', {'class': 'cmc-button-group'})

        for div in headerDiv:
            text = div.text
            if "Next" in text:
                self.counter +=1
                # page_number = [string for string in text.split() if string.isdigit()][0]
                self.new_url = self.start_url + str(self.counter) + '/'
                return

        self.new_url = False

        return




if __name__ == "__main__":
    # run scrapper
    scapper = WebScrapper()
    scapper.scrape()
