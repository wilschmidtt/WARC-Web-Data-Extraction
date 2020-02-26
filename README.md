Still in process of creating repo
# WARC-Archive-Web-Data-Extraction
![What](Images/header_art.png)

UC Davis has 15,000 archived WARC files that contain information about all UC Davis related websites from the past 10 years. The goal of this project was to create a program that would connect to the server containing the WARCs, and then use Selinium and BeautifulSoup to visit all of the target URI's and scrape the html body text from each one. Ultimately, a text-analysis will be run on the scraped data and given to the UC Davis Sociology department to conduct research upon. Project was created for UC Davis Data Science and Informatics lab.

### Prerequisites
* Python 2.7
  - [Install Python 2.7](https://www.python.org/downloads/release/python-2717/)
    - Python 2.7 must be used because the 'warc' module that is imported doesn't run on Python 3 versions
### Libraries to Install
* warc - allows user to work with WARC and ARC files
* paramiko - allows you to connect to a secured shell
* urllib - 
* bs4 - 
* os - 
* selenium

## Running the tests


## Authors

* **William Schmidt** - [LikedIn](https://www.linkedin.com/in/william-schmidt-152431168/)
