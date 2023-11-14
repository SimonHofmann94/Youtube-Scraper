# Youtube-Scraper
A quick web scraper for scraping comments of youtube

The code provided is a web scraper using YouTube Data API v3 to scrape comments from youtubes trending videos. It is necessary to access YouTube Data API and create an API-key to make this work. In my first test run this scraper returned a CSV file with around 115k lines of comments. Sadly it is not perfect yet and also returns some empty lines inbetween. These can be deleted to get a sound dataset of youtube comments.

To make it work, just insert your YouTube Data API v3 key as a string at api_key and run the code. Takes about 10 minutes to get the data. I will continue to scrape youtube comments to build a large natural language dataset for NLP purposes. The dataset will also be provided here. Enjoy!
