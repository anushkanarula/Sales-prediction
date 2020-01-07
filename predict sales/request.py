#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, jsonify
url = 'http://127.0.0.1:5000/' 
r = requests.post(url,json={'rate':5, 'sales_in_first_month':200, 'sales_in_second_month':400})
print(r.json())

