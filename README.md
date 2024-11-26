RedBus Project
1. Overview
This project describes how to use Selenium to scrape data of minimum 10 Government State Bus Transport from the RedBus website and store it in a MySQL database. This process involves setting up the environment, writing the web scraping code, managing data storage, data analysis using SQL and data visualization.

2. Prerequisites
• Python: Download and install from python.org. • Selenium: Install via pip. • MySQL: Install MySQL server and MySQL Workbench (for managing the database). • MySQL Connector for Python: Install via pip. • WebDriver: Download the appropriate WebDriver for your browser (e.g., ChromeDriver for Google Chrome).

2.1. Libraries Required to Install
pip install selenium: For web scraping
pip install mysql-connector-python: To connect Python with MySQL
pip install pandas: For data manipulation and analysis 
pip install pymysql: For connecting DB and streamlit
pip install streamlit: Framework for interactive web app in Python
3. Setup and Configuration
3.1. MySQL Database Setup
1. Start MySQL Server: Ensure the MySQL server is running
2. Create a Database: CREATE DATABASE IF NOT EXISTS redbus
3. Create a Table: 
                      CREATE TABLE IF NOT EXISTS redbus.bus_route 
                                     (id int primary key auto_increment,
                                     route_name text,
                                     route_link text,
                                     bus_name text,
                                     bus_type text,
                                     departing_time time,
                                     reaching time time,
                                     duration text,
                                     star_rating float,
                                     price decimal(10,2),
                                     seats_available int)
                                     
5. Web Scraping with Selenium
4.1. Setting up the web driver
driver = webdriver.Chrome() 
# Note: For Chrome Browser installed the chromium webdriver 
4.2. Open the RedBus link
driver.get(YOUR_URL)
5. Application Usage
5.1. Running the Scraper
1. Run the Streamlit: Execute the Streamlit to start the scraping process.
   Streamlit run stream.py
5.2. Verifying Data Storage
1. Open MySQL Workbench
2. Check the database:
   USE redbus; 
   SELECT * FROM bus_route;
This will display the data stored in the bus_route table
6. Error Handling and Debugging
 1. Element Not Found: Ensure the HTML structure hasn’t changed. Update the locators accordingly.
 2. Timeouts: Increase time.sleep() durations if pages take longer to load.
 3. Connection Errors: Verify MySQL server is running and credentials are correct.
7. Conclusion
This project outlines the steps for scraping data of minimum 10 Government State Transport Buses from RedBus using Selenium and storing it in MySQL. The code samples provided cover essential operations for extracting data and interacting with the database along with the application usage.

