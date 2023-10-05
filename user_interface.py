from vacancy.vacancy_manager import VacancyManager
from file_saver.json_saver import JSONSaver
from vacancy.vacancy import Vacancy


def user_interaction():
    vacancy_manager = VacancyManager()
    json_saver = JSONSaver()

    while True:
        print("\nМеню:")
        print("1. Добавить вакансию")
        print("2. Удалить вакансию")
        print("3. Фильтровать вакансии")
        print("4. Сортировать вакансии")
        print("5. Получить вакансии по зарплате")
        print("6. Сохранить вакансии в файл")
        print("0. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название вакансии: ")
            link = input("Введите ссылку на вакансию: ")
            salary = float(input("Введите зарплату: "))
            requirements = input("Введите требования к вакансии: ")
            vacancy = Vacancy(title, link, salary, requirements)
            vacancy_manager.add_vacancy(vacancy)
            print("Вакансия добавлена.")

        elif choice == "2":
            title = input("Введите название вакансии для удаления: ")
            filtered_vacancies = vacancy_manager.filter_vacancies([title.lower()])
            if filtered_vacancies:
                vacancy_manager.delete_vacancy(filtered_vacancies[0])
                print("Вакансия удалена.")
            else:
                print("Вакансия не найдена.")

        elif choice == "3":
            keyword = input("Введите ключевое слово для фильтрации вакансий: ").lower()
            filtered_vacancies = vacancy_manager.filter_vacancies([keyword])
            print_vacancies(filtered_vacancies)

        elif choice == "4":
            vacancy_manager.sort_vacancies()
            print_vacancies(vacancy_manager.vacancies)

        elif choice == "5":
            salary_range = input("Введите диапазон зарплаты (мин-макс): ")
            filtered_vacancies = json_saver.get_vacancies_by_salary(salary_range)
            print_vacancies(filtered_vacancies)

        elif choice == "6":
            json_saver.save_to_json("vacancies.json")
            print("Вакансии сохранены в файл vacancies.json.")

        elif choice == "0":
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите существующий вариант.")


def print_vacancies(vacancies):
    if vacancies:
        for index, vacancy in enumerate(vacancies, start=1):
            print(f"{index}. {vacancy}")
    else:
        print("Нет вакансий, соответствующих заданным критериям.")
