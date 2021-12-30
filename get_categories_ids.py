"""
Gets possible category names and ids and writes them to a file,
then get store valid/wanted category names and ids
after manually deleting unwanted categories
"""
import get_songs as data

def store_categories(country: str) -> None:
    categories = data.get_categories(limit=50, country=country)
    with open('categories_ids.txt', mode='w', encoding='utf-8') as f:
        for category in categories:
            f.write(category + ': ' + categories[category] + '\n')

def get_category_ids() -> dict:
    with open('categories_ids.txt', mode='r') as f:
        category_to_id = {}
        for row in f:
            c = row.replace('\n', '').split(': ')
            category_to_id[c[0]] = c[1]

    return category_to_id

def get_id(category: str) -> str:
    categories = get_category_ids()
    category_id = categories[category]
    return category_id
