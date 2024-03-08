from utils.http_methods import http_methods

"""Методы для тестирования api"""

base_url = "https://petstore.swagger.io/v2/user"              # Базовая URL

class User():

    """"Метод для создания user"""
    @staticmethod
    def create_new_user():
        json_for_create_new_user = {
          "id": 99,
          "username": "Elvis",
          "firstName": "Elvis",
          "lastName": "Presli",
          "email": "test@mail.ru",
          "password": "test123",
          "phone": "999999",
          "userStatus": 99
}
        post_resourse = "https://petstore.swagger.io/v2/user"
        print(post_resourse)
        result_post = http_methods.post(post_resourse, json_for_create_new_user)
        print(result_post.text)
        return result_post

    """"Метод для проверки созданного user"""

    @staticmethod
    def get_new_user():
        get_resourse = base_url + "/" + "Elvis"
        print(get_resourse)
        result_get = http_methods.get(get_resourse)
        print(result_get.text)
        return result_get

    """"Метод для проверки удаления user"""

    @staticmethod
    def delete_new_user():
        delete_resourse = base_url + "/" + "Elvis"
        print(delete_resourse)
        json_for_delete_user = {
          "id": 99,
          "username": "Elvis",
          "firstName": "Elvis",
          "lastName": "Presli",
          "email": "test@mail.ru",
          "password": "test123",
          "phone": "999999",
          "userStatus": 99
}
        result_delete = http_methods.delete(delete_resourse, json_for_delete_user)
        print(result_delete.text)
        return result_delete