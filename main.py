import hashlib
import json

WIKIPEDIA_LINKS = 'wiki_links.txt'
COUNTRIES = 'countries.json'
WIKI_URL = 'https://en.wikipedia.org/wiki/'


class WikiLink:

    def __init__(self, country_file_path):
        with open(country_file_path) as file:
            countries_data = json.load(file)
            country_names = (country['name']['common'] for country in countries_data)
            self.country_names_iter = iter(country_names)

    def get_link(self, country_name: str):
        country_name = country_name.replace(' ', '_')
        country_wiki_url = f'{WIKI_URL}{country_name}'
        return country_wiki_url

    def __iter__(self):
        return self

    def __next__(self):
        country_name = next(self.country_names_iter)
        log = f'{country_name} - {self.get_link(country_name)}'
        return log


def get_hash(path: str):
    with open(path) as file:
        for line in file:
            yield hashlib.md5(line.encode()).hexdigest()


if __name__ == '__main__':
    with open(WIKIPEDIA_LINKS, 'w') as country_names_file:
        for country_link in WikiLink(COUNTRIES):
            country_names_file.write(f'{country_link}\n')

    for hash_str in get_hash(WIKIPEDIA_LINKS):
        print(hash_str)