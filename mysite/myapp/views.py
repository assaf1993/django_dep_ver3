from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver

def index(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    browser = webdriver.Chrome(options=chrome_options)
    try:
        browser.get("https://www.google.com")
        print("Page title was '{}'".format(browser.title))
    except Exception as e:
        print(e)
    finally:
        browser.quit()

    return HttpResponse("OK")
