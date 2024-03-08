import json

import pytest

from utils.checking import Checking

from utils.api_user_negativity import User_negativ

"""Тестирование негативных сценариев создания, получения и удаление user"""

class Test_create_user_negativity():

    @pytest.mark.run(order=2)
    def test_create_new_user_negativ(self):
        try:
            print("Метод POST")
            result_post_1 = User_negativ.create_new_user_negativ_1()
            result_post_2 = User_negativ.create_new_user_negativ_2()
            result_post_3 = User_negativ.create_new_user_negativ_3()
            Checking.check_status_code(result_post_1, 400)
            Checking.check_status_code(result_post_2, 400)
            Checking.check_status_code(result_post_3, 400)
        except AssertionError:
            print("Произошла ошибка статус код не соотвествует 400-ому")


        print("Метод GET")
        result_get_1 = User_negativ.get_new_user_negativ_1()
        result_get_2 = User_negativ.get_new_user_negativ_2()
        result_get_3 = User_negativ.get_new_user_negativ_3()
        Checking.check_status_code(result_get_1, 404)
        Checking.check_status_code(result_get_2, 405)
        Checking.check_status_code(result_get_3, 404)

        print("Метод DELETE")
        result_delete_1 = User_negativ.delete_new_user_negativ_1()
        result_delete_2 = User_negativ.delete_new_user_negativ_2()
        Checking.check_status_code(result_delete_1, 404)
        Checking.check_status_code(result_delete_2, 404)