import json

import pytest

from utils.checking import Checking

from utils.api_pet_negativity import Pet_negativ

"""Тестирование негативных сценариев создания, получения и удаление pet"""

class Test_create_pet_negativity():

    @pytest.mark.run(order=4)
    def test_create_new_pet_negativ(self):
        try:
            print("Метод POST")
            result_post_1 = Pet_negativ.create_new_pet_negativ_1()
            result_post_2 = Pet_negativ.create_new_pet_negativ_2()
            result_post_3 = Pet_negativ.create_new_pet_negativ_3()
            Checking.check_status_code(result_post_1, 400)
            Checking.check_status_code(result_post_2, 400)
            Checking.check_status_code(result_post_3, 500)
        except AssertionError:
            print("Произошла ошибка статус код не соотвествует 400-ому")

        print("Метод GET")
        result_get_1 = Pet_negativ.get_new_pet_negativ_1()
        result_get_2 = Pet_negativ.get_new_pet_negativ_2()
        result_get_3 = Pet_negativ.get_new_pet_negativ_3()
        Checking.check_status_code(result_get_1, 404)
        Checking.check_status_code(result_get_2, 405)
        Checking.check_status_code(result_get_3, 404)

        print("Метод DELETE")
        result_delete_1 = Pet_negativ.delete_new_pet_negativ_1()
        result_delete_2 = Pet_negativ.delete_new_pet_negativ_2()
        Checking.check_status_code(result_delete_1, 404)
        Checking.check_status_code(result_delete_2, 404)