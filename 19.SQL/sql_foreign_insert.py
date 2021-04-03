#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sql_foreign_models import Phone,Company
from sql_insert import insert
  
companys = {
            "Apple":"Amercian",
            "Xiaomi":"China",
            "Huawei":"China",
            "Sungsum":"Korea",
            "Nokia":"Finland"
           }
phones = (
        [1,"iphoneX","Apple",8400],
        [2,"xiaomi2s","Xiaomi",3299],
        [3,"Huaweimate10","Huawei",3399],
        [4,"SungsumS8","SungSum",4099], 
        [5,"NokiaLumia","Nokia",2399],
        [6,"iphone4s","Apple",3800]
         )        
 
 
for key in companys:
    new_company = Company(name=key,location=companys[key]) 
    insert(new_company)
 
for phone in phones:
    id = phone[0]
    model = phone[1]
    company_name = phone[2]
    price = phone[3]
 
    new_phone = Phone(id=id,model=model,company_name=company_name,price=price)
    insert(new_phone)