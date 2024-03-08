import json

import pytest

from utils.checking import Checking

from utils.api_user import User

"""Создание, изменение и удаление новой локации"""

class Test_create_user():

    @pytest.mark.run(order=1)
    def test_create_new_user(self):

        print("Метод POST")
        result_post = User.create_new_user()
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['code', 'type', 'message'])
        Checking.check_json_value(result_post, 'message', '99')

        print("Метод GET")
        result_get = User.get_new_user()
        Checking.check_status_code(result_get, 200)
        token = json.loads(result_get.text)                           # Когда в ответе приходит много полей можно применить эту функцию и в дальнейшем просто скопировать и вставить в следующий запрос чтобы было проще
        print(list(token))
        Checking.check_json_token(result_get, ['id', 'username', 'firstName', 'lastName', 'email', 'password', 'phone', 'userStatus'])
        Checking.check_json_value(result_get, 'id', 99)
        Checking.check_json_value(result_get, 'username', 'Elvis')
        Checking.check_json_value(result_get, 'userStatus', 99)

        print("Метод DELETE")
        result_delete = User.delete_new_user()
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['code', 'type', 'message'])
        Checking.check_json_value(result_delete, 'code', 200)
        Checking.check_json_value(result_delete, 'message', 'Elvis')

        print("Метод GET - DELETE")                        # Этим методом я проверяю что предыдущий запрос удалил user и его больше нет
        result_get = User.get_new_user()
        Checking.check_status_code(result_get, 404)
        Checking.check_json_value(result_get, 'message', 'User not found')

        print("Тестирование создания, получения и удаления user выполнено успешно!")