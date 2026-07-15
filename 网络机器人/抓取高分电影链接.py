# 获取高分列表信息
import requests
from lxml import html
import csv
urls_top = "https://www.themoviedb.org/movie/top-rated"
urls_movie = "https://www.themoviedb.org"
# 发送请求
response = requests.get(urls_top)
document = html.fromstring(response.text)
movie_list = document.xpath('//div/div[2]/div/a/h2/span/text()')
movie_links = document.xpath('//div/div[2]/div/a/@href')   # 直接取 a 标签的 href 属性
# 输出时先有电影名后再有链接
# for movie_name, movie_link in zip(movie_list, movie_links):
#     print(f"《{movie_name}》        {urls_movie + movie_link}")

# 保存为csv文件
with open("网络机器人\\top_movies.csv", "w", encoding="utf-8")as f:
    writer = csv.writer(f)
    writer.writerow(["电影名", "链接"])
    for movie_name, movie_link in zip(movie_list, movie_links):
        writer.writerow([movie_name, urls_movie + movie_link])
