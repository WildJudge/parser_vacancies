import requests
from .abstract_api import AbstractAPI
from config import SUPERJOB_APP_ID, SUPERJOB_SECRET_KEY


class SuperJobAPI(AbstractAPI):
    def __init__(self):
        """Конструктор класса SuperJobAPI"""
        self.app_id = SUPERJOB_APP_ID
        self.secret_key = SUPERJOB_SECRET_KEY

    def get_vacancies(self, search_query):
        """
        Получает вакансии с сайта SuperJob по заданному запросу.

        Args:
            search_query (str): Поисковый запрос.

        Returns:
            list: Список объектов Vacancy.
        """
        headers = {
            'X-Api-App-Id': self.app_id,
            'X-Api-Secret-Key': self.secret_key
        }
        url = 'https://api.superjob.ru/2.0/vacancies'
        params = {'town': 'Москва', 'keywords': search_query}
        response = requests.get(url, params=params, headers=headers)
        data = response.json()

        # Проверяем наличие ключа 'objects' в JSON-ответе
        if 'objects' in data:
            vacancies = data['objects']
            return vacancies
        else:
            print("Ошибка при получении вакансий с SuperJob.")
            return []
