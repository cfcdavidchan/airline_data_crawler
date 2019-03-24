# Web Crawler for tripadvisor.com Airline data (Windows OS)

## Description
This is a web crawler project of crawling airline data from [Tripadvisor.com](https://www.tripadvisor.com/Airlines/). With the url of the airline company and the name of the airline company, the python script will be able to crawl the related reviews from Tripadvisor.com

The basic function of the entire project is a web-crawler function by applying python scrapy library. Apart from that, a supporting script (such as airline_crawl.py) is created in order to automatize the crawler. However, the supprting part is not the main purpose of the project, it will not be mentioned a lot.  

## Installation

1. Install Python( Windows user can use 3.5.4)

  * [Python 3.5.6](https://www.python.org/downloads/release/python-356/)

2. **[Optional but Recommend]** Using virtualenv to create a virtual environment that is isolated to your original Python

  2.1 Installing virtualenv
        * `pip install virtualenv`
  2.2 Creating a virtual environment
        * `cd [the project path]`
        * `virtualenv [virtual environment name]`
  2.3 activate
        * `[project path]\[virtual environment name]\Scripts\activate.bat`

3. Library pre-install

  * `pip install -r requirement.txt`

## Web-crawler

Getting into the root directory of scrapy.

* `cd tripadvisorSpider_crawler/`

Start crawling
* `scrapy crawl scrapy crawl tripadvisor_airline -a start_url="TARGET URL" -a name="COMPANY NAME"`


After running the code directoy will be created under the root directory of scrapy. Then, the review data will be stored into a csv file.


###### Bonus
`airline_crawl.py` can be used to run the crawler semi automatically by running the subprocess library.
Try to run the code if you want to understnad how to do that.
