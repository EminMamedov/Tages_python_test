from utils.http_methods import http_methods

"""Методы для тестирования api"""

base_url = "https://petstore.swagger.io/v2/user"              # Базовая URL

class User_negativ():
    # Подготовил несколько вариантов негативных сценариев , в действительности проверок может быть много, поэтому я сделаю три варианта
    """1. Отсутствие обязательного поля:
   - Удалить одно из обязательных полей (например, username или вообще все поля) и проверить,
   как API обработает запрос без этого поля."""

    @staticmethod
    def create_new_user_negativ_1():
        json_for_create_new_user_negativ_1 = {

        }
        post_resourse = "https://petstore.swagger.io/v2/user"
        print(post_resourse)
        result_post = http_methods.post(post_resourse, json_for_create_new_user_negativ_1)
        print(result_post.text)
        return result_post

    """2. Слишком длинное значение поля:
   - Передать слишком длинное значение(так еще и из цифр - сразу две проверки) для поля 
   username, firstName, или lastName и проверить, как API будет обрабатывать такую ситуацию."""

    @staticmethod
    def create_new_user_negativ_2():
        json_for_create_new_user_negativ_2 = {
            "id": 99,
            "username": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
            "firstName": "2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222",
            "lastName": "33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333",
            "email": "test@mail.ru",
            "password": "test123",
            "phone": "999999",
            "userStatus": 99
        }
        post_resourse = "https://petstore.swagger.io/v2/user"
        print(post_resourse)
        result_post = http_methods.post(post_resourse, json_for_create_new_user_negativ_2)
        print(result_post.text)
        return result_post

    """3. Отрицательное значение для id или userStatus:
   - Измените значение поля id или userStatus на отрицательное число и убедитесь, 
   что API корректно обрабатывает такое значение."""

    @staticmethod
    def create_new_user_negativ_3():
        json_for_create_new_user_negativ_3 = {
            "id": -123,
            "username": "Elya",
            "firstName": "Elya",
            "lastName": "Presli",
            "email": "test@mail.ru",
            "password": "test123",
            "phone": "999999",
            "userStatus": -555
        }
        post_resourse = "https://petstore.swagger.io/v2/user"
        print(post_resourse)
        result_post = http_methods.post(post_resourse, json_for_create_new_user_negativ_3)
        print(result_post.text)
        return result_post

    """1. Запрос несуществующего ресурса:
   - Попробовать выполнить GET запрос к несуществующему эндпоинту и проверить, 
    как API обрабатывает такой запрос (должен вернуться код ошибки 404 Not Found)."""

    @staticmethod
    def get_new_user_negativ_1():
        get_resourse = base_url + "/" + "Elvis28379712494239729"
        print(get_resourse)
        result_get = http_methods.get(get_resourse)
        print(result_get.text)
        return result_get

    """2. Отсутствие обязательных параметров:
   - Попробуйте выполнить GET запрос, для которого не переданы обязательные параметры в запросе, и убедитесь, 
    что API корректно обрабатывает такие случаи."""

    @staticmethod
    def get_new_user_negativ_2():
        get_resourse = base_url
        print(get_resourse)
        result_get = http_methods.get(get_resourse)
        print(result_get.text)
        return result_get

    """3. Некорректный формат запроса:
   - Отправить GET запрос с некорректным форматом запроса (например, неверный заголовок Content-Type) 
    и проверить, как API отвечает на это."""

    @staticmethod
    def get_new_user_negativ_3():
        get_resourse = base_url + "/" + "Elvis28379712494239729"
        print(get_resourse)
        result_get = http_methods.get_negativ(get_resourse)
        print(result_get.text)
        return result_get

    """1. Удаление несуществующего ресурса:
   - Попробовать выполнить DELETE запрос к несуществующему ресурсу и проверить, 
    как API обрабатывает такой запрос (должен вернуться код ошибки 404 Not Found)."""

    @staticmethod
    def delete_new_user_negativ_1():
        delete_resourse = base_url + "/" + "Elweokfnvowenfknwekoewvbokwnbokp"
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

    """2. Повторное удаление уже удаленного ресурса:
   - Попробовать повторно удалить ресурс, который уже был удален, и убедитесь, 
    что API возвращает соответствующее сообщение или статус об этом."""

    @staticmethod
    def delete_new_user_negativ_2():
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






