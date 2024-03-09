from utils.httpmethods import HttpMethods

"""Методы для тестирования api"""

base_url = "https://petstore.swagger.io/v2/pet"              # Базовая URL

class PetNegativ:
    # Подготовил несколько вариантов негативных сценариев , в действительности проверок может быть много, поэтому я сделаю три варианта
    """1. Отсутствие обязательного поля:
   - Удалить одно из обязательных полей (например, id или вообще все поля) и проверить,
   как API обработает запрос без этого поля."""

    @staticmethod
    def create_new_pet_negativ_1():
        json_for_create_new_pet_negativ_1 = {

        }
        post_resourse = "https://petstore.swagger.io/v2/pet"
        print(post_resourse)
        result_post = HttpMethods.post(post_resourse, json_for_create_new_pet_negativ_1)
        print(result_post.text)
        return result_post

    """2. Слишком длинное значение поля:
   - Передать слишком длинное значение(так еще и из цифр - сразу две проверки) для поля 
     Name и status и проверить, как API будет обрабатывать такую ситуацию."""

    @staticmethod
    def create_new_pet_negativ_2():
        json_for_create_new_pet_negativ_2 = {
            "id": 88,
          "category": {
            "id": 97,
            "name": "Elvis"
          },
          "name": "doggie1346134655555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555",
          "photoUrls": [
            "null"
          ],
          "tags": [
            {
              "id": 78,
              "name": "Armi"
            }
          ],
          "status": "23462346163"
        }
        post_resourse = "https://petstore.swagger.io/v2/pet"
        print(post_resourse)
        result_post = HttpMethods.post(post_resourse, json_for_create_new_pet_negativ_2)
        print(result_post.text)
        return result_post

    """3. Слишком длинное значение поля:
   - Передать слишком длинное значение для поля 
     id и проверить, как API будет обрабатывать такую ситуацию"""

    @staticmethod
    def create_new_pet_negativ_3():
        json_for_create_new_pet_negativ_3 = {
            "id": 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999,
          "category": {
            "id": 99,
            "name": "Elvis"
          },
          "name": "doggie13461345",
          "photoUrls": [
            "null"
          ],
          "tags": [
            {
              "id": 78,
              "name": "Armi"
            }
          ],
          "status": "23462346163"
        }
        post_resourse = "https://petstore.swagger.io/v2/pet"
        print(post_resourse)
        result_post = HttpMethods.post(post_resourse, json_for_create_new_pet_negativ_3)
        print(result_post.text)
        return result_post

    """1. Запрос несуществующего ресурса:
   - Попробовать выполнить GET запрос к несуществующему эндпоинту и проверить, 
    как API обрабатывает такой запрос (должен вернуться код ошибки 404 Not Found)."""

    @staticmethod
    def get_new_pet_negativ_1():
        get_resourse = base_url + "/" + "28379712494239729"
        print(get_resourse)
        result_get = HttpMethods.get(get_resourse)
        print(result_get.text)
        return result_get

    """2. Отсутствие обязательных параметров:
   - Попробуйте выполнить GET запрос, для которого не переданы обязательные параметры в запросе, и убедитесь, 
    что API корректно обрабатывает такие случаи."""

    @staticmethod
    def get_new_pet_negativ_2():
        get_resourse = base_url
        print(get_resourse)
        result_get = HttpMethods.get(get_resourse)
        print(result_get.text)
        return result_get

    """3. Некорректный формат запроса:
   - Отправить GET запрос с некорректным форматом запроса (например, неверный заголовок Content-Type) 
    и проверить, как API отвечает на это."""

    @staticmethod
    def get_new_pet_negativ_3():
        get_resourse = base_url + "/" + "99"
        print(get_resourse)
        result_get = HttpMethods.get_negativ(get_resourse)
        print(result_get.text)
        return result_get

    """1. Удаление несуществующего ресурса:
   - Попробовать выполнить DELETE запрос к несуществующему ресурсу и проверить, 
    как API обрабатывает такой запрос (должен вернуться код ошибки 404 Not Found)."""

    @staticmethod
    def delete_new_pet_negativ_1():
        delete_resourse = base_url + "/" + "234612341634614631346"
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
          "status": "23462346163"
        }
        result_delete = HttpMethods.delete(delete_resourse, json_for_delete_pet)
        print(result_delete.text)
        return result_delete

    """2. Повторное удаление уже удаленного ресурса:
   - Попробовать повторно удалить ресурс, который уже был удален, и убедитесь, 
    что API возвращает соответствующее сообщение или статус об этом."""

    @staticmethod
    def delete_new_pet_negativ_2():
        delete_resourse = base_url + "/" + "Elvis"
        print(delete_resourse)
        json_for_delete_pet = {
              "id": 99,
              "category": {
                "id": 99,
                "name": "Elvis"
              },
              "name": "doggie5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555",
              "photoUrls": [
                "null"
              ],
              "tags": [
                {
                  "id": 78,
                  "name": "Armi"
                }
              ],
              "status": "2452452"
}
        result_delete = HttpMethods.delete(delete_resourse, json_for_delete_pet)
        print(result_delete.text)
        return result_delete