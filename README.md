# Berk Spider

This is a web scraping project using Scrapy and Playwright to extract agent details from the Berkshire Hathaway HomeServices website.

## Project Overview

The `BerkSpider` spider scrapes a list of real estate agents from the [Berkshire Hathaway HomeServices website](https://www.bhhsamb.com/roster/Agents). For each agent, it collects the following information:
- Agent Name
- Job Title
- Phone Number
- Website
- Email Contact Page
- Address
- Profile Image URL

## Technologies Used

- **Scrapy**: A fast, high-level web crawling and web scraping framework for Python.
- **Playwright**: A library for automating web browsers, allowing you to handle dynamic content.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/muhammedshameemap/berk_scrapper.git
   cd berk_spider
   ```

2. **Install the Required Packages**:
   ```bash
   git clone https://github.com/muhammedshameemap/berk_scrapper.git
   cd berk_spider
   ```

3. **Install Playwright Browsers:**\
   ```bash
   playwright install
   ```

4. **Running the Spider**
    To run the spider and collect the output in both CSV and JSON formats, use the following commands:

5. **Outputs**
    **Outputs to CSV**

   ```bash
   scrapy crawl berk_spider -o output/agents.csv -t csv
   ```

    **Output to JSON**
   ```bash
   scrapy crawl berk_spider -o output/agents.json -t json
   ```

6. **Output Files**
   The spider will generate output files in the specified format and save them in the output directory. You can find the files as follows:

   output/agents.csv
   output/agents.json


7. **Code Structure**
   spiders/berk_spider.py: Contains the main spider implementation.
   output/: Directory where the output files will be stored.