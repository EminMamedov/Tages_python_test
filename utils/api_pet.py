from utils.httpmethods import HttpMethods

"""Методы для тестирования api"""

base_url = "https://petstore.swagger.io/v2/pet"              # Базовая URL

class Pet:

    """"Метод для создания pet"""
    @staticmethod
    def create_new_pet():
        json_for_create_new_pet = {
          "id": 99,
          "category": {
            "id": 99,
            "name": "Elvis"
          },
          "name": "doggie",
          "photoUrls": [
            "null"
          ],
          "tags": [
            {
              "id": 78,
              "name": "Armi"
            }
          ],
          "status": "available"
}
        post_resourse = "https://petstore.swagger.io/v2/pet"
        print(post_resourse)
        result_post = HttpMethods.post(post_resourse, json_for_create_new_pet)
        print(result_post.text)
        return result_post

    """"Метод для проверки созданного pet"""

    @staticmethod
    def get_new_pet(id):
        get_resourse = base_url + "/" + str(id)
        print(get_resourse)
        result_get = HttpMethods.get(get_resourse)
        print(result_get.text)
        return result_get

    """"Метод для проверки удаления pet"""

    @staticmethod
    def delete_new_pet(id):
        delete_resourse = base_url + "/" + str(id)
        print(delete_resourse)
        json_for_delete_pet = {
          "id": 99,
          "category": {
            "id": 99,
            "name": "Elvis"
          },
          "name": "doggie",
          "photoUrls": [
            "null"
          ],
          "tags": [
            {
              "id": 78,
              "name": "Armi"
            }
          ],
          "status": "available"
}
        result_delete = HttpMethods.delete(delete_resourse, json_for_delete_pet)
        print(result_delete.text)
        return result_delete