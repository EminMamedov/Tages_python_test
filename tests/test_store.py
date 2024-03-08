import json

import pytest

from utils.checking import Checking

from utils.api_store import Store




class Test_create_store():

    @pytest.mark.run(order=5)
    def test_create_new_store(self):
        print("Метод Post")
        result_post = Store.create_new_store()
        check_post = result_post.json()
        id = check_post.get("id")
        Checking.check_status_code(result_post, 200)
        token = json.loads(
            result_post.text)  # Когда в ответе приходит много полей можно применить эту функцию и в дальнейшем просто скопировать и вставить в следующий запрос чтобы было проще
        print(list(token))
        Checking.check_json_token(result_post, ['id', 'petId', 'quantity', 'shipDate', 'status', 'complete'])
        Checking.check_json_value(result_post, 'id', 9)

        print("Метод Get")
        result_get = Store.get_new_store(id)
        Checking.check_json_value(result_get, 'id', 9)
        Checking.check_json_value(result_get, 'complete', True)
        Checking.check_json_value(result_get, 'status', 'placed')

        print("Метод Delete")
        result_delete = Store.delete_new_store(id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['code', 'type', 'message'])
        Checking.check_json_value(result_delete, 'code', 200)
        Checking.check_json_value(result_delete, 'message', '9')

        print("Метод GET - DELETE")  # Этим методом я проверяю что предыдущий запрос удалил user и его больше нет
        result_get = Store.get_new_store(id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_value(result_get, 'message', 'Order not found')

        print("Тестирование создания, получения и удаления pet выполнено успешно!")