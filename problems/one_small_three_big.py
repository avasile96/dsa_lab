import requests
import re

from collections import Counter

url = 'http://www.pythonchallenge.com/pc/def/equality.html'
response = requests.get(url)

# Print the HTML source code
print(response.text)

# Data cleaning
# Finding the correct comment
data = response.text.split('<!--')[1]
print(data)

