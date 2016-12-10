import requests
from bs4 import BeautifulSoup
import os
numArticles = 35333
articlesPerPage = 20
numPages = int(numArticles / articlesPerPage)
maxArticles = 100
def onion_spider(maxPages):
    curArticle = 1
    page = 1
    
    while page < maxPages:
        
        url = "http://www.theonion.com/search?before=2016-12-10&after=1996-01-01&page=" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll('a',{'data-track-action':'Content List: Article'}):
            href = 'http://www.theonion.com' + link.get("href")
            articleCode = requests.get(href)
            articleText = articleCode.text
            artSoup = BeautifulSoup(articleText , 'html.parser')
            writeLine = False
           
            #o_file= open(os.getcwd()+'/Data/OnionRaw/'+str(curArticle)+'.txt', 'w')
            if artSoup.p != None:
                text = str(artSoup.p)
                text.replace('<p>','')
                text.replace('</p>','')
                outFile = open(os.getcwd() + '/Data/OnionRaw/' + str(curArticle) + '.txt','w')
                outFile.write(text)
                outFile.close()
            
    
               
            curArticle += 1
            #print(curArticle)    
        page += 1

if __name__ == "__main__":
    onion_spider(2)
