import requests
import matplotlib.pyplot as plt

from collections import Counter

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
response = requests.get(url)

# Print the HTML source code
print(response.text)

# Data cleaning
# Finding the correct comment
data = response.text.split('<!--')[2]
print(data)

# Feature extraction
chars_count = Counter(data)
chars = chars_count.keys()
counts = chars_count.values()
print(chars)
print(counts)

# plt.figure(figsize=(12, 6))
# plt.bar(chars, counts)
# plt.xlabel('Character')
# plt.ylabel('Frequency')
# plt.title('Character Frequency Histogram')
# plt.show()

# Feature engineering
print(chars_count.keys())
print([k for k, v in chars_count.items() if v < 5])

