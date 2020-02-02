# libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# get the data
def get(url):
    """
    its a funtion to get the data from webpage
    """    
    page = requests.get(url) 
    if page.status_code == 200:
        htmldata = page.text
        soup = BeautifulSoup(htmldata, 'lxml')
        print('success')
        return soup
    else:
        print('error',page.status_code)

def extract(soup):
    page_products = [] # will hold the products from a page
    titles = soup.find_all('div',attrs={'class':'_3wU53n'})
    prices= soup.find_all('div',attrs={'class':'_1vC4OE _2rQ-NK'})
    links = soup.find_all('a', attrs={'class':'_31qSD5'})
 
    for t,p,a in zip(titles,prices,links):
        data = {
            'title' : t.text,
            'price' : p.text,
            'link':a.attrs.get('href'),
        }
        page_products.append(data)
    print('total product collected',len(page_products))
    return page_products

def save(dataset,filename="out.csv"):
    if len(dataset) > 0:
        print('saving dataset...')
        df = pd.DataFrame(dataset)
        df.to_csv(filename)
        print('saved file to', filename)
    else:
        print('could not save empty dataset')