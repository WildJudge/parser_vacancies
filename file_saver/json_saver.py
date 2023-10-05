import json


class JSONSaver:
    def __init__(self):
        """Конструктор класса JSONSaver"""
        self.vacancies = []

    def add_vacancy(self, vacancy):
        """
        Добавляет вакансию в список.

        Args:
            vacancy (Vacancy): Объект Vacancy.
        """
        self.vacancies.append(vacancy)

    def get_vacancies_by_salary(self, salary_range):
        """
        Возвращает вакансии по заданному диапазону зарплаты.

        Args:
            salary_range (str): Диапазон зарплаты.

        Returns:
            list: Отфильтрованный список вакансий.
        """
        min_salary, max_salary = map(int, salary_range.split('-'))
        filtered_vacancies = [vacancy for vacancy in self.vacancies if min_salary <= vacancy.salary <= max_salary]
        return filtered_vacancies

    def delete_vacancy(self, vacancy):
        """
        Удаляет вакансию из списка.

        Args:
            vacancy (Vacancy): Объект Vacancy.
        """
        self.vacancies.remove(vacancy)

    def save_to_json(self, filename):
        """
        Сохраняет вакансии в JSON-файл.

        Args:
            filename (str): Имя файла для сохранения.
        """
        with open(filename, 'w') as file:
            json.dump([vars(vacancy) for vacancy in self.vacancies], file)
