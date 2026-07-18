import requests
from lxml import html
import csv
# 常量
TMDB_BASE_URL = 'https://www.themoviedb.org'
TMDB_TOP_URL_1 = 'https://www.themoviedb.org/movie/top-rated'
TMDB_TOP_URL_2 = 'https://www.themoviedb.org/discover/movie/items'
MOVE_LIST_FILE = 'D:\github\python-noob\网络机器人\move_list.csv'


def get_move_info(movie_info_url):
    # 发送请求
    response = requests.get(movie_info_url, timeout=60)
    # 解析数据
    document = html.fromstring(response.text)
    # 电影名称
    movie_names = document.xpath(
        '//*[@id="original_header"]/div[2]/section/div[1]/h2/a/text()')
    movie_years = document.xpath(
        '//*[@id="original_header"]/div[2]/section/div[1]/h2/span/text()')
    movie_date = document.xpath(
        '//*[@id="original_header"]/div[2]/section/div[1]/div/span[@class="release"]/text()')
    movie_tags = document.xpath(
        '//*[@id="original_header"]/div[2]/section/div[1]/div/span[@class="genres"]/a/text()')
    movie_cost_time = document.xpath(
        '//*[@id="original_header"]/div[2]/section/div[1]/div/span[@class="runtime"]/text()')
    movie_scores = document.xpath(
        '//*[@id="consensus_pill"]/div/div[1]/div/div/@data-percent')
    movie_languages = document.xpath(
        '//*[@id="media_v4"]/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()')
    movie_directors = document.xpath(
        '//*[@id="original_header"]/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()')
    movie_authors = document.xpath(
        '//*[@id="original_header"]/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()')
    movie_solgans = document.xpath(
        '//*[@id="original_header"]/div[2]/section/div[3]/h3[1]/text()')
    movie_descriptions = document.xpath(
        '//*[@id="original_header"]/div[2]/section/div[3]/div/p/text()')

    # 返回电影详情
    movie_info = {
        '电影名': movie_names[0].strip() if movie_names else '',
        '年份': movie_years[0].strip() if movie_years else '',
        '上映日期': movie_date[0].strip() if movie_date else '',
        '类型': ','.join(movie_tags) if movie_tags else '',
        '时长': movie_cost_time[0].strip() if movie_cost_time else '',
        '评分': movie_scores[0].strip() if movie_scores else '',
        '语言': movie_languages[0].strip() if movie_languages else '',
        '导演': ','.join(movie_directors) if movie_directors else '',
        '作者': ','.join(movie_authors) if movie_authors else '',
        '宣传语': movie_solgans[0].strip() if movie_solgans else '',
        '简介': movie_descriptions[0].strip() if movie_descriptions else ''
    }
    print(movie_info)
    return movie_info


def save_movies(all_movies):
    # 使用csv.DictWriter正确写入CSV文件
    with open(MOVE_LIST_FILE, 'w', encoding='utf-8-sig', newline='') as f:
        fieldnames = ['电影名', '年份', '上映日期', '类型',
                      '时长', '评分', '语言', '导演', '作者', '宣传语', '简介']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        # 写入表头
        writer.writeheader()
        # 写入数据行
        for movie in all_movies:
            writer.writerow(movie)


def main():
    all_movies = []
    for page_num in range(1, 6):
        # 1.发送请求 获取高分电影榜单数据
        if page_num == 1:
            response = requests.get(TMDB_TOP_URL_1, timeout=60)
        else:
            # POST请求参数
            payload = {
                'air_date.gte': '',
                'air_date.lte': '',
                'certification': '',
                'certification_country': 'CN',
                'debug': '',
                'first_air_date.gte': '',
                'first_air_date.lte': '',
                'include_adult': 'false',
                'include_softcore': 'false',
                'latest_ceremony.gte': '',
                'latest_ceremony.lte': '',
                'page': str(page_num),
                'primary_release_date.gte': '',
                'primary_release_date.lte': '',
                'region': '',
                'release_date.gte': '',
                'release_date.lte': '2026-12-29',
                'show_me': 'everything',
                'sort_by': 'vote_average.desc',
                'vote_average.gte': '0',
                'vote_average.lte': '10',
                'vote_count.gte': '300',
                'watch_region': 'CN',
                'with_genres': '',
                'with_keywords': '',
                'with_networks': '',
                'with_origin_country': '',
                'with_original_language': '',
                'with_watch_monetization_types': '',
                'with_watch_providers': '',
                'with_release_type': '',
                'with_runtime.gte': '0',
                'with_runtime.lte': '400'
            }
            response = requests.post(TMDB_TOP_URL_2, data=payload, timeout=60)
        # 2.解析数据，获得电影列表
        document = html.fromstring(response.text)
        movie_list = document.xpath(
            '//*[@class="media-list-results contents"]/div')

        for movie in movie_list:

            movie_urls = movie.xpath('.//a[@data-media-type="movie"]/@href')
            if movie_urls:
                # 每个电影详情url地址
                movie_info_url = TMDB_BASE_URL + movie_urls[0]
                # 发送请求，获取电影详情数据
                move_info = get_move_info(movie_info_url)
                all_movies.append(move_info)

    # 4.保存数据
    save_movies(all_movies)


if __name__ == '__main__':
    main()
