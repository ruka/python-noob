import requests

# 定义爬取的URL
target_url = "https://www.tiobe.com/tiobe-index/"

# 获取网页内容
response = requests.get(target_url)

# 输出网页内容
print(response.text)
