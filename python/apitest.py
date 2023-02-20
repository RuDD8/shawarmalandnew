import requests

url = "https://shawarmaland1.azurewebsites.net/Home/ShowAllUnfinishedOrder"

payload={}
headers = {
  'Accept': '*/*',
  'Accept-Language': 'en-US,en;q=0.9,ka;q=0.8,ru;q=0.7',
  'Connection': 'keep-alive',
  'Content-Length': '0',
  'Cookie': 'ARRAffinity=4741f22325c9805749ece58501e97de960d6a967f0a185d34ae8b1fcba6ea91e; ARRAffinitySameSite=4741f22325c9805749ece58501e97de960d6a967f0a185d34ae8b1fcba6ea91e; .AspNetCore.Antiforgery.w5W7x28NAIs=CfDJ8KumqFpNJUlBuFsrKPXcXHNynQQQEzQryAth054X4-k__NE0dneD_19J6az5Kt83i8ENWmin5gK-jjgksZFsrrcKiSac4El8MGv-e_NiPql5VElLkoAb4QgZlZz2hf6OMVzaF3pYhE1vIrQrpcMpBcc; IdentityCookie=CfDJ8KumqFpNJUlBuFsrKPXcXHOiKGsWQcpNCrqx0tTyNQJdLY43rTZgRibuPgGS4XGEvMfZRl62DCg4gMdXF0YyhQTimziZaJhvEnuPBG0M34hW_DibNouP0uDBj_Grf9C-SLYEv4SSO47ik6zPkotAKYUONPoE8Uu6qpAEl_61FmNe3PJndbU61GT7IPeilY_zTD-KHCp90GGUWOFg1OKovOx_wNH0lXVkZ7HvLDDFdtxyGuWa46w4y3Qqcw9IVCcucFDdBymGMg_sUMRrM3a7y9QLocG2c-pR9FzWxWxROCEx--Kf04Tt39H8RZ89rDKcXjt8edx_WPH8YEB0xbWKa5k0C-PTW4Tne2hZppHX0i4qCDgdVm95TMe1PQ2eqBqaqeS7STB7w4QHLPyUvrFmXB6dqFVSaemh_IxjmuTyDtbNhnaoFhFUFUVnNpjGvWf14wY9Xbz4JLuMVhqeJ6axlqI3_gy5oNA-9RxGkXCMfgDGtNdaWKQCXKh0h7QMvJB2bvkCqTQa3thVwstC1gFIeYsdZYhfM_aWUSDV1k-LfgKpKct7gWXgdWmclwyd8cefSr2nyBrdbc8x7ZCUVqoEcTTH-BHwzCdafWigZGSJlw07ZN0bJ7w1TVk7TJUzImt4F3No-ma8UuCvHcU-LLSNjo04hVAbn9ZPKF2Nzm9lQHiwJATDFJH2ktJV-idxVW9pbA',
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

food_db = {
}

x = 0
for i in resp_dict:
    prod = resp_dict[x]

    products = prod.get("products")

    products_dict = products[0]

    x = x + 1

    #print(products_dict)

    qId = products_dict.get("qId")
    #print(qId)

    food_db["qId"] = qId

print(food_db)

food_db = {
   'jack': {'ID': "1"}
}

print(type(food_db))