import requests
from bs4 import BeautifulSoup
import json


articles = []

years_english = [2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012]
years_german = [2021, 2020, 2019, 2018, 2017, 2016]
years_spanish = [2021, 2020, 2019, 2018, 2017, 2016]
years_france = [2021, 2020, 2019, 2018, 2017, 2016]
years_italian = [2021, 2020, 2019, 2018, 2017]
years_japanse = [2021, 2020, 2019, 2018, 2017, 2016]
years_korean = [2021, 2020, 2019, 2018, 2017, 2016]
years_polish = [2021, 2020, 2019, 2018, 2017, 2016]
years_portugues = [2021, 2020, 2019, 2018, 2017, 2016]
years_russian = [2021, 2020, 2019, 2018, 2017]
#years_thai = [] #had no years
years_turkish = [2021, 2020, 2019, 2018, 2017, 2016]
years_chinese = [2021, 2020, 2019, 2018, 2017, 2016]

def function (years, urls, language):

  for i in years:

    url = urls+str(i)
    
    page = requests.get(url)

    html = BeautifulSoup(page.content, "html.parser")

    items = html.find_all("div", class_="c-card-post c-card-post--extra-small cms-editor-link")

    for item in items:

      title = item.find("h3").get_text()
      description = item.find("p", class_="c-card-post__inner__description c-card-post__inner__description--extra-small").get_text()
      date = item.find("p", class_="c-card-post__inner__date c-card-post__inner__date--extra-small").get_text().strip()

      article = {"title": title, "description": description, "date": date, "year": i, "language": language}
      articles.append(article)


function(years_english, "https://blog.twitch.tv/en/archive/", "english")
function(years_german, "https://blog.twitch.tv/de-de/archive/", "german")
function(years_spanish, "https://blog.twitch.tv/es-mx/archive/", "spanish")
function(years_france, "https://blog.twitch.tv/fr-fr/archive/", "france")
function(years_italian, "https://blog.twitch.tv/it-it/archive/", "italian")
function(years_japanse, "https://blog.twitch.tv/ja-jp/archive/", "japanse")
function(years_korean, "https://blog.twitch.tv/ko-kr/archive/", "korean")
function(years_polish, "https://blog.twitch.tv/pl-pl/archive/", "polish")
function(years_portugues, "https://blog.twitch.tv/pt-br/archive/", "portugues")
function(years_russian, "https://blog.twitch.tv/ru-ru/archive/", "russian")
function(years_turkish, "https://blog.twitch.tv/tr-tr/archive/", "turkish")
function(years_chinese, "https://blog.twitch.tv/zh-tw/archive/", "chinese")


with open("graph1_blogs_languages.json", "w") as json_file:
  json.dump(articles, json_file)



