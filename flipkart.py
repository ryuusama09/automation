
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def search_and_filter_product(driver , product_name):
    # Search for Samsung Galaxy S10
    search_box_xpath ="//*[@id='container']/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input"
    #/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input
    search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, search_box_xpath)))
    search_box.send_keys(product_name)
    search_box.submit()

    # Click on Mobiles in categories
    mobiles_category_xpath= "//*[@id='container']/div/div[3]/div[1]/div[1]/div/div[1]/div/div/section/div[3]/div/a"
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, mobiles_category_xpath))).click()

    # Apply Brand filter - Samsung
    brand_filter_xpath = "//*[@id='container']/div/div[3]/div[1]/div[1]/div/div[1]/div/section[3]/div[2]/div/div/div/label/div[2]"
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, brand_filter_xpath))).click()


    # # Sort by Price High to Low
    price_sort_xpath = "//*[@id='container']/div/div[3]/div/div[2]/div[1]/div/div/div[3]/div[4]"
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,price_sort_xpath ))).click()


    # Apply Flipkart Assured filter
    assured_filter_xpath = " //*[@id='container']/div/div[3]/div[1]/div[1]/div/div[1]/div/section[4]/label/div[2]/div"
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, assured_filter_xpath))).click()

  
    products = []
    prefix_xpath = "//*[@id='container']/div/div[3]/div[1]/div[2]/"
    name_suffix_xpath = "/div/div/div/a/div[2]/div[1]/div[1]"
    link_suffix_xpath = "/div/div/div/a"
    price_suffix_xpath = "/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]"
    for i in range(2,24):
      product = {}
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, prefix_xpath + f"div[{i}]" + name_suffix_xpath)))
      product['name'] = driver.find_element(By.XPATH, prefix_xpath + f"div[{i}]" + name_suffix_xpath).text
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, prefix_xpath + f"div[{i}]" + link_suffix_xpath)))
      product['link'] = driver.find_element(By.XPATH, prefix_xpath + f"div[{i}]" + link_suffix_xpath).get_attribute("href")
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, prefix_xpath + f"div[{i}]" + price_suffix_xpath)))
      product['price'] = float((driver.find_element(By.XPATH, prefix_xpath + f"div[{i}]" + price_suffix_xpath)).text.replace('₹', '').replace(',', '').strip())
      products.append(product)

    products_json = json.dumps(products)
    print(products_json)

def search_and_filter_product_mobile(driver , product_name):
    # Search for Samsung Galaxy S10
    search_box_xpath ="//*[@id='container']/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[2]"
    search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, search_box_xpath)))
    search_box.click()
    time.sleep(2)
    # # the xpath tree changes so we need to find the new search bar
    new_bar = driver.find_element(By.XPATH ,"//*[@id='input-searchsearchpage-input']")
    new_bar.send_keys(product_name)
    new_bar.submit()
    
    # # open filters 
    filter_button_xpath = "//*[@id='container']/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div[3]/div/div[2]"
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,filter_button_xpath))).click()
    
     # # click on assured
    assured_xpath = "//*[@id='_parentCtr_']/div[1]/div/div/div/div[1]/div/div/div/div/div[3]/div/div/div/div/div/div"
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,assured_xpath))).click()

    # # click on assured plus
    time.sleep(1)
    assured_button_xpath = "//*[@id='_parentCtr_']/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div"
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,assured_button_xpath))).click()

    # # click on brand filter
    brand_button_xpath = "//*[@id='_parentCtr_']/div[1]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div"
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,brand_button_xpath))).click()

    # # click on brand samsung
    samsung_button_xpath = "//*[@id='_parentCtr_']/div[2]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div"
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,samsung_button_xpath))).click()

    # # apply button xpath
    apply_button_xpath = "//*[@id='container']/div/div[1]/div/div/div/div/div[3]/div[1]/div/div/div/div[1]/div[2]/div/div"
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,apply_button_xpath))).click()

    # sort button click
    sort_button_xpath= "//*[@id='container']/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div[1]/div/div"
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, sort_button_xpath))).click()


    # apply price high to low 
    time.sleep(1)
    price_high_to_low = "/html/body/div[4]/div/div[2]/div/div/div[3]/div[4]/div/div/div[1]/div"
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, price_high_to_low))).click()
    
    

    products = []
    prefix_xpath = "//*[@id='_parentCtr_']/"
    name_suffix_xpath = "/div/div[1]/div/div/div/div[2]/div[1]/div"
    link_suffix_xpath = "/div/div[1]/div/div/div"
    price_suffix_xpath = "/div/div[1]/div/div/div/div[2]/div[4]/div/div[1]/div"
    
    for i in range(2,5):
      product = {}
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, prefix_xpath + f"div[{i}]" + name_suffix_xpath)))
      product['name'] = driver.find_element(By.XPATH, prefix_xpath + f"div[{i}]" + name_suffix_xpath).text
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, prefix_xpath + f"div[{i}]" + price_suffix_xpath)))
      # Extract the price value without the percentage off
      price_element = driver.find_element(By.XPATH, prefix_xpath + f"div[{i}]" + price_suffix_xpath)
      if '%' in price_element.text:
        price_element = driver.find_element(By.XPATH, prefix_xpath + f"div[{i}]" + price_suffix_xpath + "[2]")
      if '₹' in price_element.text:
          price_text = price_element.text.replace('₹', '').replace(',', '').strip()
      product['price'] = float(price_text)
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, prefix_xpath + f"div[{i}]" + link_suffix_xpath)))
      product['link'] = driver.find_element(By.XPATH, prefix_xpath + f"div[{i}]" + link_suffix_xpath).get_attribute("href")
      products.append(product)
    products_json = json.dumps(products)
    print(products_json)



# Use context manager to handle driver's lifecycle

options = webdriver.ChromeOptions()
mobile_emulation = {"deviceName": "Pixel 4"}
options.add_experimental_option("mobileEmulation", mobile_emulation)
with webdriver.Chrome() as driver:
    driver.get("https://www.flipkart.com/")
    user_agent = driver.execute_script("return navigator.userAgent")
    if "Mobile" in user_agent or "Android" in user_agent or "iPhone" in user_agent:
      search_and_filter_product_mobile(driver)
    else:  
      search_and_filter_product(driver)