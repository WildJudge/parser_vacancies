from api.hh_api import HeadHunterAPI
from api.superjob_api import SuperJobAPI
from user_interface import user_interaction

if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()
    hh_vacancies = hh_api.get_vacancies("Python")
    superjob_vacancies = superjob_api.get_vacancies("Python")

    user_interaction()
