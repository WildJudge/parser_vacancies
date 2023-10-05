class VacancyManager:
    def __init__(self):
        """Конструктор класса VacancyManager"""
        self.vacancies = []

    def add_vacancy(self, vacancy):
        """
        Добавляет вакансию в список.

        Args:
            vacancy (Vacancy): Объект Vacancy.
        """
        self.vacancies.append(vacancy)

    def filter_vacancies(self, filter_words):
        """
        Фильтрует вакансии по ключевым словам.

        Args:
            filter_words (list): Список ключевых слов.

        Returns:
            list: Отфильтрованный список вакансий.
        """
        filtered_vacancies = []
        for vacancy in self.vacancies:
            if any(word in vacancy.title.lower() for word in filter_words):
                filtered_vacancies.append(vacancy)
        return filtered_vacancies

    def sort_vacancies(self):
        """
        Сортирует вакансии по зарплате.
        """
        self.vacancies.sort(reverse=True)

    def delete_vacancy(self, vacancy):
        """
        Удаляет вакансию из списка.

        Args:
            vacancy (Vacancy): Объект Vacancy.
        """
        self.vacancies.remove(vacancy)
