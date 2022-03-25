# WARC-Archive-Web-Data-Extraction
 
UC Davis has 15,000 archived WARC files that contain information about all UC Davis related websites from the past 10 years. The goal of this project was to create a program that would connect to the server containing the WARCs, and then use Selinium and BeautifulSoup to visit all of the target URI's and scrape the html body text from each one. Ultimately, a text-analysis will be run on the scraped data and given to the UC Davis Sociology department to conduct research upon. Project was created for UC Davis Data Science and Informatics lab.
 
### Prerequisites
* Python 2.7
  - [Install Python 2.7](https://www.python.org/downloads/release/python-2717/)
    - Python 2.7 must be used because the 'warc' module that is imported doesn't run on Python 3 versions
* UC Davis Library VPN
  - [VPN - Instillation and Use Instructions](https://www.library.ucdavis.edu/service/connect-from-off-campus/)
    - VPN can only be installed if you are a UC Davis student/staff
### Libraries to Install
* warc - allows user to work with WARC and ARC files
* paramiko - allows you to connect to a secured shell
* urllib - used to open URL's
* bs4 - library for pulling data out of HTML and XML files
* selenium - allows you to connect with your browser and load dynamic web pages
 
## Running the Program
* First, open the file titled 'warc_parser.py' in any text editor
* Next, navigate to line 11 and change 'user_name' to your Kerberos ID, then change 'password' to your Kerberos password. This will allow you to connect to the UC Davis DataSci server through SSH.
* The next step is to go through and find all the lines that contain the address of a local directory and update them to the where you wish to save the output files on your machine.
* Next, simply run the program. From here, you can expect a few things to happen:
  1) The program will begin to fetch WARC's from the DataSci server and store them on your machine
  2) The program will store both a raw, unedited version of the WARC, as well as a .txt file for each WARC that contains only the relevant info within the file. These two items will be stored in folders titled 'raw_warc_files' and 'warc_info_files' respectively.
  3) For each Warc info file, the program will go through, extract all of the URL's that the WARC in question visited, write these URL's to a .txt file, then store the file in a folder tilted 'warc_uri'
  4) The program will then go through each .txt file in the 'warc_uri' folder, and create a new .txt files that only contains unique URL's. The reason for this is that there can be many duplicate URL's in the original file, and when using the list of URL's, we only want to have each one contained a single time so that we do not scrape the same website twice
* Once this program finishes running, you will have all the relevant files that you need to perfrom the second half of the process. The relevant files are the 'warc_info_files' and the 'unique_uri' files.
* When ready, open up the program titled 'uri_text_scrape.py', and as you did with the previous program, you will need to go through and change all the paths so that they reference locations on your machine.
* Once this step is done, you can run the program and wait for it to finished. Once complete, this program will return a folder titled 'uri_scrapped_text'
* Within this folder, you will see sub-folders, each corresponding to a single WARC file. Within the sub-folders, you will see a variety of .txt files. Each of these .txt files corresponds to a unique URL that was contained within that WARC, and the .txt file stores all of the data that was scrapped from the URL in question
* Once the second program finishes running, you are done. You now have all of the scrapped data from the WARC files, and you can use this to run a desired text report

## Final Thoughts
* A big draw-back with these two programs is that they both store all of the data on your local machine. Not only will the data take up an enormous amount of space (probably more than your machine can handle), but it will take far longer than is practical to finish running.
* To get around this problem, I created a program that works in a similar fashion on the UC Davis DataSci server, where the WARC's were stored. This way, I didn't need to re-download any files, and all of the .txt files that contained scrapped data could be stored directly on the server for later use. This program was created using Linux CentOS, Python 2.7, and all the same libraries as above. I could not post this program on GitHub though because you must have root-priveleges to run it.
* In addition, I posted a couple sample folders to repo that demonstrate what the programs would return if run on your local machine.
