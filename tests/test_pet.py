import json

import pytest

from utils.checking import Checking

from utils.api_pet import Pet




class Test_create_pet():

    @pytest.mark.run(order=3)
    def test_create_new_pet(self):
        print("Метод Post")
        result_post = Pet.create_new_pet()
        check_post = result_post.json()
        id = check_post.get("id")
        Checking.check_status_code(result_post, 200)
        token = json.loads(
            result_post.text)  # Когда в ответе приходит много полей можно применить эту функцию и в дальнейшем просто скопировать и вставить в следующий запрос чтобы было проще
        print(list(token))
        Checking.check_json_token(result_post, ['id', 'category', 'name', 'photoUrls', 'tags', 'status'])
        Checking.check_json_value(result_post, 'id', 99)

        print("Метод Get")
        result_get = Pet.get_new_pet(id)
        Checking.check_json_value(result_get, 'id', 99)
        Checking.check_json_value(result_get, 'name', 'doggie')
        Checking.check_json_value(result_get, 'status', 'available')

        print("Метод Delete")
        result_delete = Pet.delete_new_pet(id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['code', 'type', 'message'])
        Checking.check_json_value(result_delete, 'code', 200)
        Checking.check_json_value(result_delete, 'message', '99')

        print("Метод GET - DELETE")  # Этим методом я проверяю что предыдущий запрос удалил user и его больше нет
        result_get = Pet.get_new_pet(id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_value(result_get, 'message', 'Pet not found')

        print("Тестирование создания, получения и удаления pet выполнено успешно!")