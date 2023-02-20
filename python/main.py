from fastapi import FastAPI
import requests
import json
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time
from seleniumwire import webdriver
from selenium.webdriver.common.by import By

app = FastAPI()

origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

user_db = {
}

done_db = {
}

done_arr = []


class User(BaseModel):
    name: str
    id: int


class Done(BaseModel):
    name: str
    id: int

with open('cookie.txt', 'r') as f:
    data = f.read()
cookie = data

@app.get("/in-progress")
def hello():
    url = "https://shawarmaland1.azurewebsites.net/Home/ShowAllUnfinishedOrder"
    with open('cookie.txt', 'r') as f:
        data = f.read()
    cookie = data
    payload = {}
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Cookie': cookie,
        'Origin': 'https://shawarmaland1.azurewebsites.net',
        'Referer': 'https://shawarmaland1.azurewebsites.net/Home/Users',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if str(response) == "<Response [200]>":
        resp_dict = response.json()

        l = 0
        while l < len(resp_dict):
            order = resp_dict[l]
            products = order.get("products")
            shaurma = products[0]
            id = shaurma.get("qId")
            l = l + 1

            x = {
                "name": "shawarmaland",
                "id": id
            }

            # user_db[id] = x
            if id not in done_arr:
                user_db[id] = x
    else:
        driver = webdriver.Chrome()
        driver.get("https://shawarmaland1.azurewebsites.net/Identity/Account/Login?ReturnUrl=/")
        username = driver.find_element(By.XPATH, '//*[@id="Input_Username"]')
        username.send_keys("admin")
        password = driver.find_element(By.XPATH, '//*[@id="Input_Password"]')
        password.send_keys("Password1.")
        login = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/section/form/div[4]/button')
        login.click()
        time.sleep(5)
        driver.get("https://shawarmaland1.azurewebsites.net/Home/Users#")
        progress = driver.find_element(By.XPATH, '/html/body/div[1]/ul/li[2]/a')
        progress.click()
        time.sleep(1)
        progress.click()
        headers = driver.execute_script(
            "var req = new XMLHttpRequest();req.open('GET', document.location, false);req.send(null);return req.getAllResponseHeaders()")

        # type(headers) == str
        x = driver.last_request
        z = x.headers
        cookie = z["Cookie"]
        with open('cookie.txt', 'w') as f:
            data = cookie
            f.write(data)
        url = "https://shawarmaland1.azurewebsites.net/Home/ShowAllUnfinishedOrder"

        payload = {}
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9,ka;q=0.8,ru;q=0.7',
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'Cookie': cookie,
            'Origin': 'https://shawarmaland1.azurewebsites.net',
            'Referer': 'https://shawarmaland1.azurewebsites.net/Home/Users',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        resp_dict = response.json()

        l = 0
        while l < len(resp_dict):
            order = resp_dict[l]
            products = order.get("products")
            shaurma = products[0]
            id = shaurma.get("qId")
            l = l + 1

            x = {
                "name": "shawarmaland",
                "id": id
            }

            # user_db[id] = x
            if id not in done_arr:
                user_db[id] = x

    return user_db


@app.post('/in-progress')
def create_user(user: User):
    id = user.id
    user_db[id] = user.dict()
    return user_db


@app.delete('/in-progress/{id}')
def delete_user(id: int):
    del user_db[id]
    return user_db


@app.get("/done")
def hello():
    return done_db


@app.post('/done')
def create_user(user: Done):
    ids = user.id
    done_db[ids] = user.dict()
    done_arr.append(ids)
    return done_db


@app.delete('/done/{ids}')
def delete_user(ids: int):
    del done_db[ids]
    url = "https://shawarmaland1.azurewebsites.net/Home/FinishOrder"

    payload = "QId=" + str(ids)
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': cookie,
        'Origin': 'https://shawarmaland1.azurewebsites.net',
        'Referer': 'https://shawarmaland1.azurewebsites.net/Home/Users',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    done_arr.remove(ids)

    return done_db