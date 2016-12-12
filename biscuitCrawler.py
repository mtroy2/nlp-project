import requests
from bs4 import BeautifulSoup
import os
numArticles = 8260

articlesPerPage = 20
numPages = 413
def biscuit_spider(maxPages):
    curArticle =6100
    page = 300
    
    
    while page < maxPages:
        print(page)
        url = "http://www.newsbiscuit.com/page/" + str(page) + '/?s=+'

        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll('h3'):
            try:
                link_s = str(link)
                link_s = link_s[13:-9]
                end = link_s.find('"')
                if end != -1:
                    link_s = link_s[:end]
                href = link_s
                # load new article
                articleCode = requests.get(href)    
      
                    
                articleText = articleCode.text
                artSoup = BeautifulSoup(articleText , 'html.parser')
                writeLine = False
               
                #o_file= open(os.getcwd()+'/Data/OnionRaw/'+str(curArticle)+'.txt', 'w')
                for line in artSoup.findAll('div',{'class':'textcontent clearfix entry-content'}):
                    prevTitle = ""
                    for pageSegment in line:
          
                        pageString = str(pageSegment)
                        if pageString.find('Sociable') != -1:
                            break
                        else:
                            
                            title = str(artSoup.title)
                            if prevTitle == title:
                                break
                            else:
                                prevTitle = title
                            title = title[7:]
                            if 'more soon' in title.lower():
                                break
                            end = title.find('NewsBiscuit')
                            title = title[:end]
                            
                            text = str(line)
                            if text.find('div class') != -1:
                                text = text[51:-8]
                            else:
                                text = text[3:-8]
                            
                   
                            outFile = open(os.getcwd() + '/Data/BiscuitRaw/biscuit' + str(curArticle) + '.txt','w')
                            outFile.write(title)
                            outFile.write('\n')
                            outFile.write(text)
                            outFile.close()
                            curArticle += 1
            except requests.exceptions.ConnectionError:
                curArticle += 1 
        page += 1

if __name__ == "__main__":
    biscuit_spider(410)
