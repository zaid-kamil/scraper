import multi_page_scraper as mps

# "https://www.flipkart.com/search?q=tv&page=1"

url = "https://www.flipkart.com/search?"
search_term = "laptop"
page = 1
filename = 'laptop_23dec.csv'

scraped_products = [] 
while True:
    starturl = f"{url}q={search_term}&page={page}"
    print('getting data from',starturl,'...')
    soup = mps.get(starturl)
    if not soup:
        print('scraper closed')
        break
    else:
        output = mps.extract(soup)
        if len(output) == 0:
            print('scraper closed')
            break
        scraped_products.extend(output)
        print('total size of collected data', len(scraped_products))
        page += 1

# save the stuff
mps.save(scraped_products,filename)
        
