<h1>Web Scraper with Selenium and Openpyxl</h1>

<h2>Overview</h2>
<p>This Python script uses Selenium and Openpyxl libraries to scrape data from a website and save it to an Excel file.</p>

<h2>Prerequisites</h2>
<ul>
    <li>Python 3.x</li>
    <li>Selenium</li>
    <li>Openpyxl</li>
</ul>

<h2>Installation</h2>
<ol>
    <li>Install Python from <a href="https://www.python.org/downloads/">python.org</a>.</li>
    <li>Install Selenium using pip:
        <pre>pip install selenium</pre>
    </li>
    <li>Install Openpyxl using pip:
        <pre>pip install openpyxl</pre>
    </li>
    <li>Download the ChromeDriver from <a href="https://sites.google.com/chromium.org/driver/">chromedriver.chromium.org</a>.</li>
    <li>Place the ChromeDriver executable in your system's PATH.</li>
</ol>

<h2>Usage</h2>
<ol>
    <li>Run the script <code>web_scraper.py</code>.</li>
    <li>Enter the URL of the website when prompted.</li>
    <li>Provide the XPATH for the Title and Price elements on the website.</li>
    <li>The script will scrape the data, create an Excel file named "Produtos.xlsx", and save the scraped data.</li>
</ol>

<h2>Example</h2>
<pre>
========================================
Website's URL: https://www.example.com
Title's XPATH: //div[@class='product-title']
Price's XPATH: //div[@class='product-price']
========================================
</pre>

<h2>Note</h2>
<ul>
    <li>Ensure that you have the Chrome browser installed.</li>
    <li>Adjust XPATHs according to the structure of the website you are scraping.</li>
</ul>
