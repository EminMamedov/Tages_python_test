import json

import pytest

from utils.checking import Checking

from utils.api_store_negativity import StoreNegativ

"""Тестирование негативных сценариев создания, получения и удаление pet"""

class Test_create_store_negativity():

    @pytest.mark.run(order=6)
    def test_create_new_store_negativ(self):
        try:
            print("Метод POST")
            result_post_1 = StoreNegativ.create_new_store_negativ_1()
            result_post_2 = StoreNegativ.create_new_store_negativ_2()
            result_post_3 = StoreNegativ.create_new_store_negativ_3()
            Checking.check_status_code(result_post_1, 400)
            Checking.check_status_code(result_post_2, 400)
            Checking.check_status_code(result_post_3, 500)
        except AssertionError:
            print("Произошла ошибка статус код не соотвествует 400-ому")

        print("Метод GET")
        result_get_1 = StoreNegativ.get_new_store_negativ_1()
        result_get_2 = StoreNegativ.get_new_store_negativ_2()
        result_get_3 = StoreNegativ.get_new_store_negativ_3()
        Checking.check_status_code(result_get_1, 404)
        Checking.check_status_code(result_get_2, 405)
        try:
            Checking.check_status_code(result_get_3, 400)
        except AssertionError:
            print("Произошла ошибка статус код не соотвествует 400-ому")

        print("Метод DELETE")
        result_delete_1 = StoreNegativ.delete_new_store_negativ_1()
        result_delete_2 = StoreNegativ.delete_new_store_negativ_2()
        Checking.check_status_code(result_delete_1, 404)
        Checking.check_status_code(result_delete_2, 404)