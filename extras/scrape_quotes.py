from bs4 import BeautifulSoup
import requests
import sys

# getting the html code
def get_html(q, p):
    url = "https://www.goodreads.com/quotes/search?"
    q = str(q)
    p = str(p)
    content = requests.get(url+"page="+p+"&"+"q="+q)
    return content.text

# getting the required item as dictionary
def get_quotes(query, page=1):
    soup = BeautifulSoup(get_html(query, page), 'html5lib')

    # get the quotes
    try:
        quotes = soup.find_all("div", class_="quoteText")
    except:
        quotes = []

    # get no of pages 
    try:
        pages = int(soup.find("a", class_="next_page").find_previous_sibling("a").text)
    except:
        pages = 0

    list_quotes = []
    for quote in quotes:
        dict_quote = {}
        q_text = (quote.text).strip().split("―")[0].strip()
        q_author = (quote.text).strip().split("―")[1].strip().split(",")[0]
        dict_quote["text"] = q_text
        dict_quote["author"] = q_author
        list_quotes.append(dict_quote)

    return list_quotes, pages

# for testing 
if len(sys.argv) == 2:
    query = sys.argv[1]
    print(get_quotes(query))


