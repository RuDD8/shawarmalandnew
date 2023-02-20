from fastapi import FastAPI
import requests
import json
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel



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



url = "https://shawarmaland1.azurewebsites.net/Home/ShowAllUnfinishedOrder"

payload = {}
headers = {
  'Accept': '*/*',
  'Accept-Language': 'en-US,en;q=0.9,ka;q=0.8,ru;q=0.7',
  'Connection': 'keep-alive',
  'Content-Length': '0',
  'Cookie': 'ARRAffinity=4741f22325c9805749ece58501e97de960d6a967f0a185d34ae8b1fcba6ea91e; ARRAffinitySameSite=4741f22325c9805749ece58501e97de960d6a967f0a185d34ae8b1fcba6ea91e; .AspNetCore.Antiforgery.w5W7x28NAIs=CfDJ8KumqFpNJUlBuFsrKPXcXHNZqHbUZVORktyxhWidO4VMI8on2z9uWjI2GQAevAYHZ_alkRH8Zpx9SkFgbxxdcYkcQZHvqdC7DHgq_e8AQ9vUGc2PzhOTqeYuSr5lQU-1h7r6V2WK-m7A_VZECEZFR24; IdentityCookie=CfDJ8KumqFpNJUlBuFsrKPXcXHPWycYP7tGqK5T6d1W0IKuWsXTvYgcmp8Qsp78vKtORLfOKjG6IUs3ixf_I71JKxVxX-VPBZPG0alaoGKMtgf9387GNxsysx0QHWUmFoy3VTtDH3s5KU1v728urVjN-Rv681fbQb41y4NCcM8pnk_4TbAl-1T8KoZ7ack7kFSo-u2SeOFPXyRar6mY7botIYYS9dQctEGJSr12Knul9HSl_QVufXBuGaNxxfGDwIpBUtJBfKtccSSjJNcIgsuFh8Yof2tjw7rmRrjvUgpdgM6YTZ54ddTeFkKvLoS-778zgi7tGJvxRHm5FwBwczbQ0bNdRv4CjU2cbd6JyJdGiXA4pMZ_HqsPTRkB6lW_C8SkPapW9D7tS76Qq0Y4OkLOXkgcWv1vmMEJpzF91mKyCzE-QMipPOZoRL4Iar77ewf0nTPy3y9jMh2_doF8ElXDRQb_d4jdOAIUgBdiikzqRTSb5JfACirof7WRK0OSLAXqJeI8BFBfZeFjfZIuj-ZDiUCcKPWfH4W8tpsXUTu1XAUdCwTo6UokKMqjxkioCftXTouxlZhmnpXOetb8XWZ8R31A-Bn9jHsYJptPte050yUHOilVWeI0PREUrum4dceL2yix2PkifszxaXgAcS4adLi1EHjCYEtLa2fP5lXCerCob; .AspNetCore.Antiforgery.w5W7x28NAIs=CfDJ8KumqFpNJUlBuFsrKPXcXHMwESiUgV_656K6kKsA496kPZe7dznePp8HahUPR6bRRLVRf03T-jrHDp7_6qo10JBUVZkUbb7Xx7TxBuj7pHXbld_JsDoYWC5b9hfaF1--wxqE2f-NwL079WGiRutjx58; ARRAffinity=4741f22325c9805749ece58501e97de960d6a967f0a185d34ae8b1fcba6ea91e; ARRAffinitySameSite=4741f22325c9805749ece58501e97de960d6a967f0a185d34ae8b1fcba6ea91e; IdentityCookie=CfDJ8KumqFpNJUlBuFsrKPXcXHPJD5jn85VZA_HrZrwO9tqBW0CPp9M2rWe8EVtjCCvX5Oh_bR-sazPna4STXuTXG-b272EwRu2sn7KHDiQ_IF2CzVvb4Flacw1r2rtvnioExcs-4UUO_pKGxhqyd07F0hKsb2XJgFK4H_KERq9TMMGIE-1E-ZMHusAEMrWqUnNI9APqw69oEklecUv0fKxWFikn2YEU_dPQSXg5XTMTLGHnS2F3ZPX8iKcpiXkWVuRID4Ua7kEsHcLBn1EUeBbG1KHyusaBWevQK5lM4bcCU_54mdo6WlnHHKp30C2CnkWIxnQJm500JMjabAz5nVyQCnNoNweyhWWqBX4a3cHgcInGk_mqjp_EYpT5ebUImhxvyjQLm0jd3nxyMtOLe9xVNU5JxkaJsBYXFDSj5MOj52HBDK2Wy5UcCLIIdiEB4ErChu6_knPkCDJLTQpBTAeO0zYeXWDi7rPbSAuHEpqrB8wAHjV_eW4kKVGP9IrATBP1hyP435yZRgEmDBo34KumUP2S-WbKm_QRLIXoLJxNDXgqJ7uEj1Byqmmzb_fCPKQZnIRcq3l1o7-UJ8c-S0p4P3l3QTG3fapAGKLKHIqHttukPvDMoERVsxl5iGJOE4RCNKIaf2OTBFLTGqTN8qTl4iaCiy62ksJhsxtP4ncRGyKJ',
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

user_db = {
}

class User(BaseModel):
    username: int
    location: str
    age: int

@app.get("/in-progress")
def hello():
  return resp_dict

@app.post('/in-progress')
def create_user(user: User):
    username = user.username
    user_db[username] = user.dict()
    return user_db