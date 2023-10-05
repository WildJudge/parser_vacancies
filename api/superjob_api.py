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
        response = requests.get(f'https://api.superjob.ru/2.0/vacancies?town=Москва&keywords={search_query}',
                                headers=headers)
        vacancies = response.json()['objects']
        return vacancies
