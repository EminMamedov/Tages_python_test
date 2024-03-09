from utils.httpmethods import HttpMethods

"""Методы для тестирования api"""

base_url = "https://petstore.swagger.io/v2/store/order"              # Базовая URL

class Store:

    """"Метод для создания store"""
    @staticmethod
    def create_new_store():
        json_for_create_new_store = {
          "id": 9,
          "petId": 55,
          "quantity": 1,
          "shipDate": "2024-03-08T19:59:20.511Z",
          "status": "placed",
          "complete": True
}
        post_resourse = "https://petstore.swagger.io/v2/store/order"
        print(post_resourse)
        result_post = HttpMethods.post(post_resourse, json_for_create_new_store)
        print(result_post.text)
        return result_post

    """"Метод для проверки созданного store"""

    @staticmethod
    def get_new_store(id):
        get_resourse = base_url + "/" + str(id)
        print(get_resourse)
        result_get = HttpMethods.get(get_resourse)
        print(result_get.text)
        return result_get

    """"Метод для проверки удаления store"""

    @staticmethod
    def delete_new_store(id):
        delete_resourse = base_url + "/" + str(id)
        print(delete_resourse)
        json_for_delete_store = {
          "id": 9,
          "petId": 55,
          "quantity": 1,
          "shipDate": "2024-03-08T19:59:20.511Z",
          "status": "placed",
          "complete": True
}
        result_delete = HttpMethods.delete(delete_resourse, json_for_delete_store)
        print(result_delete.text)
        return result_delete