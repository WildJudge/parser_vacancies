class Vacancy:
    def __init__(self, title, link, salary, requirements):
        """
        Конструктор класса Vacancy.

        Args:
            title (str): Название вакансии.
            link (str): Ссылка на вакансию.
            salary (str): Зарплата.
            requirements (str): Требования к вакансии.
        """
        self.title = title
        self.link = link
        self.salary = salary
        self.requirements = requirements

    def __repr__(self):
        """
        Возвращает строковое представление объекта Vacancy.

        Returns:
            str: Строковое представление объекта Vacancy.
        """
        return f"{self.title} - {self.salary}"

    def __lt__(self, other):
        """
        Оператор сравнения меньше для объектов Vacancy.
        Сравнивает вакансии по зарплате.

        Args:
            other (Vacancy): Другой объект Vacancy.

        Returns:
            bool: Результат сравнения.
        """
        return self.salary < other.salary
