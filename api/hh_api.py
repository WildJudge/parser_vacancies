import requests
from .abstract_api import AbstractAPI
from config import HH_CLIENT_ID


class HeadHunterAPI(AbstractAPI):
    def __init__(self):
        """Конструктор класса HeadHunterAPI"""
        self.client_id = HH_CLIENT_ID

    def get_vacancies(self, search_query):
        """
        Получает вакансии с сайта HH.ru по заданному запросу.

        Args:
            search_query (str): Поисковый запрос.

        Returns:
            list: Список объектов Vacancy.
        """
        response = requests.get(f'https://api.hh.ru/vacancies?text={search_query}&client_id={self.client_id}')
        vacancies = response.json()
        return vacancies
