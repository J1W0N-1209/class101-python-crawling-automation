import requests
import json

response = requests.get("https://ac.search.naver.com/nx/ac?q=%EC%A3%BC%EC%8B%9D%20%E3%84%B1&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100&_callback=_jsonp_5")
origin_data = response.text
str_data = origin_data.split("_jsonp_5(")[1][:-1]
print(type(str_data))
dic_data = json.loads(str_data)
print(type(dic_data))