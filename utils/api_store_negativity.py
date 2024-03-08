from utils.http_methods import http_methods

"""Методы для тестирования api"""

base_url = "https://petstore.swagger.io/v2/store/order"              # Базовая URL

class Store_negativ():
    # Подготовил несколько вариантов негативных сценариев , в действительности проверок может быть много, поэтому я сделаю три варианта
    """1. Отсутствие обязательного поля:
   - Удалить одно из обязательных полей (например, id или вообще все поля) и проверить,
   как API обработает запрос без этого поля."""

    @staticmethod
    def create_new_store_negativ_1():
        json_for_create_new_store_negativ_1 = {

        }
        post_resourse = "https://petstore.swagger.io/v2/store/order"
        print(post_resourse)
        result_post = http_methods.post(post_resourse, json_for_create_new_store_negativ_1)
        print(result_post.text)
        return result_post

    """2. Pначение поля id более 10, судя по запросу get допускается до 10:
   - Передать значение id для поля id 
     более 10 и проверить, как API будет обрабатывать такую ситуацию."""

    @staticmethod
    def create_new_store_negativ_2():
        json_for_create_new_store_negativ_2 = {
            "id": 444444,
          "petId": 55,
          "quantity": 1,
          "shipDate": "2024-03-08T19:59:20.511Z",
          "status": "placed",
          "complete": True
        }
        post_resourse = "https://petstore.swagger.io/v2/store/order"
        print(post_resourse)
        result_post = http_methods.post(post_resourse, json_for_create_new_store_negativ_2)
        print(result_post.text)
        return result_post

    """3. Передать в поле complete значение не являющимся ture или false"""

    @staticmethod
    def create_new_store_negativ_3():
        json_for_create_new_store_negativ_3 = {
            "id": 444444,
          "petId": 55,
          "quantity": 1,
          "shipDate": "2024-03-08T19:59:20.511Z",
          "status": "placed",
          "complete": "tasksasl"
        }
        post_resourse = "https://petstore.swagger.io/v2/store/order"
        print(post_resourse)
        result_post = http_methods.post(post_resourse, json_for_create_new_store_negativ_3)
        print(result_post.text)
        return result_post

    """1. Запрос несуществующего ресурса:
   - Попробовать выполнить GET запрос к несуществующему эндпоинту и проверить, 
    как API обрабатывает такой запрос (должен вернуться код ошибки 404 Not Found)."""

    @staticmethod
    def get_new_store_negativ_1():
        get_resourse = base_url + "/" + "999"
        print(get_resourse)
        result_get = http_methods.get(get_resourse)
        print(result_get.text)
        return result_get

    """2. Отсутствие обязательных параметров:
   - Попробуйте выполнить GET запрос, для которого не переданы обязательные параметры в запросе, и убедитесь, 
    что API корректно обрабатывает такие случаи."""

    @staticmethod
    def get_new_store_negativ_2():
        get_resourse = base_url
        print(get_resourse)
        result_get = http_methods.get(get_resourse)
        print(result_get.text)
        return result_get

    """3. Некорректный формат запроса:
   - Отправить GET запрос с некорректным форматом запроса (например, неверный заголовок Content-Type) 
    и проверить, как API отвечает на это."""

    @staticmethod
    def get_new_store_negativ_3():
        get_resourse = base_url + "/" + "99"
        print(get_resourse)
        result_get = http_methods.get_negativ(get_resourse)
        print(result_get.text)
        return result_get

    """1. Удаление несуществующего ресурса:
   - Попробовать выполнить DELETE запрос к несуществующему ресурсу и проверить, 
    как API обрабатывает такой запрос (должен вернуться код ошибки 404 Not Found)."""

    @staticmethod
    def delete_new_store_negativ_1():
        delete_resourse = base_url + "/" + "234612341634614631346"
        print(delete_resourse)
        json_for_delete_store = {
            "id": 444444,
          "petId": 55,
          "quantity": 1,
          "shipDate": "2024-03-08T19:59:20.511Z",
          "status": "placed",
          "complete": True
        }
        result_delete = http_methods.delete(delete_resourse, json_for_delete_store)
        print(result_delete.text)
        return result_delete

    """2. Повторное удаление уже удаленного ресурса:
   - Попробовать повторно удалить ресурс, который уже был удален, и убедитесь, 
    что API возвращает соответствующее сообщение или статус об этом."""

    @staticmethod
    def delete_new_store_negativ_2():
        delete_resourse = base_url + "/" + "9"
        print(delete_resourse)
        json_for_delete_store = {
              "id": 9,
          "petId": 55,
          "quantity": 1,
          "shipDate": "2024-03-08T19:59:20.511Z",
          "status": "placed",
          "complete": True
}
        result_delete = http_methods.delete(delete_resourse, json_for_delete_store)
        print(result_delete.text)
        return result_delete