# %%
import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

url = r"https://api.fda.gov/food/enforcement.json?&limit=1000"
response = requests.get(url)
# if response.status_code != 200:
#     print('Error: ' + response.status_code)

# elif  response.status_code ==200:
#      print('Success')
# %%
raw_data = response.json()

results = raw_data['results']
# %%
for i in results:
    print(i)
# %%
results['country']
# %%
