from csv_manager import CSV_Manager
from manipulator import Manipulator
import json

def filter_CSV(filter_field, value):
    reader = CSV_Manager("./articles.csv")
    articles = reader.get_csv_as_dicts()
    manipulator = Manipulator(articles)

    filtered = manipulator.filter_by(filter_field, value)
    return list(filtered)


def count_articles(key, value):
    return len(filter_CSV(key, value))

def is_article(key, value):
    return len(filter_CSV(key, value)) != 0

def longest_article(key, value):
    filtered = filter_CSV(key, value)
    maxObj = filtered[0]
    maxPages = int(filtered[0]['pages'])
    for obj in filtered:
        if (int(obj['pages']) > maxPages):
            maxPages = int(obj['pages'])
            maxObj = obj
    return maxObj

print("Articles with a title of t4:")
print(filter_CSV("title", "t4"))
print('')
print("Articles of a1 author:")
print(filter_CSV("author", "a1"))
print(count_articles('author', 'a1'))
print(is_article('title', 't1'))
print(longest_article('author', 'a1'))