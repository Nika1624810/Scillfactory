import csv
import json
import re
import requests
from bs4 import BeautifulSoup


class IMDbTopParser:
    BASE_URL = 'https://www.imdb.com/chart/top/'

    def __init__(self):
        self.movies = []
        self.headers = {
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/115.0 Safari/537.36'
            )
        }

    def fetch_top250(self, sort_by='rk', ascending=False):
        '''
        Загружаем список фильмов с IMDb с учётом сортировки на сайте.
        sort_by: параметр сортировки (rk, user_rating, release_date,
        num_votes, alpha, moviemeter, runtime)
        ascending: True = asc, False = desc
        '''
        direction = 'asc' if ascending else 'desc'
        url = f'https://www.imdb.com/chart/top/?sort={sort_by}%2C{direction}'

        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            raise Exception('Не удалось загрузить страницу IMDb')
        soup = BeautifulSoup(response.text, 'html.parser')

        self.movies = []

        films = soup.find('ul', class_='ipc-metadata-list').find_all(
            'li', class_='ipc-metadata-list-summary-item'
        )

        for film in films:
            title = film.find('h3', class_='ipc-title__text').text
            title = title.split('. ', 1)[1] if '. ' in title else title
            rating = film.find('span', class_='ipc-rating-star--rating').text
            link = film.find('a', class_='ipc-title-link-wrapper').get('href')

            metadata_items = film.find('div', class_='cli-title-metadata').find_all('span', class_='cli-title-metadata-item')
            metadata_texts = [x.text for x in metadata_items]
            year = int(metadata_texts[0]) if len(metadata_texts) > 0 else None
            time = (
                self._parse_time(metadata_texts[1]) if len(metadata_texts) > 1
                else None
            )
            age = metadata_texts[2] if len(metadata_texts) > 2 else None

            film_dict = {
                'title': title,
                'rating': float(rating),
                'year': year,
                'time': time,
                'age': age,
                'link': f'https://www.imdb.com{link}'
            }
            self.movies.append(film_dict)

    def _parse_time(self, time_str):
        '''
        Парсим длительность вида '2h 30m' → в минуты
        '''
        if not time_str or not isinstance(time_str, str):
            return 0

        hours = minutes = 0
        if 'h' in time_str:
            h = re.search(r'(\d+)h', time_str)
            if h:
                hours = int(h.group(1))
        if 'm' in time_str:
            m = re.search(r'(\d+)m', time_str)
            if m:
                minutes = int(m.group(1))
        return hours * 60 + minutes

    def filter_movies(
        self,
        min_rating=None,
        max_rating=None,
        min_year=None,
        max_year=None,
        title_contains=None,
        title_regex=None,
        min_time=None,
        max_time=None,
        age_in=None
    ):
        '''
        Фильтрация фильмов по условиям
        '''
        filtered = []
        for m in self.movies:
            if min_rating is not None and m['rating'] < min_rating:
                continue
            if max_rating is not None and m['rating'] > max_rating:
                continue
            if min_year is not None and m['year'] < min_year:
                continue
            if max_year is not None and m['year'] > max_year:
                continue
            if min_time is not None and m['time'] < min_time:
                continue
            if max_time is not None and m['time'] > max_time:
                continue
            if age_in and m['age'] not in age_in:
                continue
            if title_contains and title_contains.lower() not in m['title'].lower():
                continue
            if title_regex and not re.search(title_regex, m['title'], re.IGNORECASE):
                continue
            filtered.append(m)
        return filtered


    def sort_movies(self, key='rating', reverse=True):
        '''
        key: по какому полю сортировать ('rating', 'year', 'time', 'title')
        reverse: True = по убыванию
        '''
        if not self.movies:
            return []
        return sorted(self.movies, key=lambda x: x[key], reverse=reverse)

    def save_json(self, movies, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(movies, f, indent=2, ensure_ascii=False)

    def save_csv(self, movies, filename):
        if not movies:
            return
        keys = movies[0].keys()
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            dict_writer = csv.DictWriter(f, keys)
            dict_writer.writeheader()
            dict_writer.writerows(movies)



if __name__ == '__main__':
    parser = IMDbTopParser()
    parser.fetch_top250()
    print('✅ Скачан список фильмов 25 лучших фильмов всех времен (IMDb Top)')

    current_movies = parser.movies

    while True:
        print('\n--- Меню ---')
        print('1. Показать первые N фильмов')
        print('2. Фильтровать фильмы')
        print('3. Сортировать фильмы')
        print('4. Сохранить результат (CSV/JSON)')
        print('5. Обновить список фильмов с IMDb')
        print('0. Выйти')

        choice = input('Выберите действие: ').strip()

        if choice == '1':
            n = int(data if (data := input('Сколько фильмов показать? (Максимум 25): ')) else 25)
            for m in current_movies[:n]:
                print(f'{m["title"]} ({m["year"]}) — {m["rating"]}⭐ {m["time"]} мин. [{m["age"]}]')
            print(f'Показано {min(n, len(current_movies))} фильмов')

        elif choice == '2':
            min_rating = input('Мин. рейтинг (или Enter): ')
            min_rating = float(min_rating) if min_rating else None
            max_rating = input('Макс. рейтинг (или Enter): ')
            max_rating = float(max_rating) if max_rating else None
            min_year = input('Мин. год (или Enter): ')
            min_year = int(min_year) if min_year else None
            max_year = input('Макс. год (или Enter): ')
            max_year = int(max_year) if max_year else None
            title_contains = input('Название содержит (или Enter): ')
            title_regex = input('Регулярка для названия (или Enter): ')
            min_time = input('Мин. длительность в минутах (или Enter): ')
            min_time = int(min_time) if min_time else None
            max_time = input('Макс. длительность в минутах (или Enter): ')
            max_time = int(max_time) if max_time else None

            current_movies = parser.filter_movies(
                min_rating=min_rating,
                max_rating=max_rating,
                min_year=min_year,
                max_year=max_year,
                title_contains=title_contains or None,
                title_regex=title_regex or None,
                min_time=min_time,
                max_time=max_time
            )
            print(f'✅ Найдено фильмов: {len(current_movies)}')

        elif choice == '3':
            print('Доступные ключи сортировки: ranking, rating, release_date, num_votes, alphabetical, popularity, runtime')
            key = input('Сортировать по: ').strip()
            reverse = input('По убыванию? (y/n): ').strip().lower() == 'y'
            parser.fetch_top250(sort_by=key, ascending=not reverse)
            current_movies = parser.movies
            print('✅ Сортировка на сайте применена')

        elif choice == '4':
            fmt = input('Сохранить в (csv/json): ').strip().lower()
            filename = input('Введите имя файла: ').strip()
            if fmt == 'csv':
                parser.save_csv(current_movies, filename)
            elif fmt == 'json':
                parser.save_json(current_movies, filename)
            print(f'✅ Сохранено в {filename}')

        elif choice == '5':
            parser.fetch_top250()
            current_movies = parser.movies
            print('✅ Список обновлён')
