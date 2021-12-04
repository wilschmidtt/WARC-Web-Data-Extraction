# Scrape HTML Text

import urllib
from bs4 import BeautifulSoup
import os

basepath = "C:\Users\William\Desktop\warc_project\unique_warc_uri"
z = 1

# Iterating throgh all files in the 'unique_warc_uri' folder
for filename in os.listdir(basepath):
    i = 1
    
    # Creating a new folder to store all the data scraped from each file inside of the 'unique_warc_uri' folder
    path = "C:\Users\William\Desktop\warc_project\uri_scraped_text\warc_uri_scrape_" +str(z)
    os.mkdir(path)
    
    # Opening the file in question that is inside of the 'unique_warc_uri' folder
    uri_path = os.path.join(basepath, filename)
    with open(uri_path) as openfile:
        
        # Iterating through all lines inside the file in question
        line = openfile.readline()
        while line != '':
            
            # Trying to open the URL in question using BeautifulSoup. Skips to next URL if an exception occurs
            try:
                url = line
                html = urllib.urlopen(url).read()
                soup = BeautifulSoup(html)
            except:
                line = openfile.readline()
                continue
            
            # If BeautifulSoup successfully connects to the url in question, we now create a .txt file to store the scraped data
            file_name = os.path.join(path, "uri_scrape_" + str(i) + ".txt")
            with open(file_name, 'w+') as text_file:
                
                # Write the URL in question to the .txt file
                text_file.write('URL: ' + url + '\n')
                
                # Tries to write title to the .txt file. If none exists, will just write the html body text to the .txt file
                try:
                    text_file.write('Title Attribute: ' + soup.title.string + '\n' + '\n')
                except:
                    text_file.write('Title Attribute: None Found' + '\n' + '\n')
                finally:    
                    
                    # kill all script and style elements
                    for script in soup(["script", "style"]):
                        script.extract()
                    
                    # get text
                    text = soup.get_text()
                    
                    # break into lines and remove leading and trailing space on each
                    lines = (line.encode('utf-8').strip() for line in text.splitlines())
                    # break multi-headlines into a line each
                    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                    # drop blank lines
                    text = '\n'.join(chunk for chunk in chunks if chunk)
                    
                    # Write the html body text to the .txt file
                    text_file.write(text)
                    
                    # Go to the next line of the file in question, which contains the next URL to scrape from
                    i += 1
                    line = openfile.readline()
    z += 1