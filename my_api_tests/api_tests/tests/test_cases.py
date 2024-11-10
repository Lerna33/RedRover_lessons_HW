import pytest
from my_api_tests.api_tests.models.case_model import CaseModel
from my_api_tests.api_tests.utils.response_logging import log_response


def test_read_all_cases(api_client):
    # Отправляем GET-запрос на получение всех тест-кейсов
    response = api_client.make_request(handle="/testcases", method="GET")

    # Логируем ответ
    log_response(response)

    # Проверяем, что статус-код 200
    assert response.status_code == 200


# Тест для проверки создания нового тест-кейса
def test_create_case(api_client):
    # Данные для создания нового тест-кейса
    test_case_data = {
        "id": 104,
        "name": "Новый тест-кейс",
        "description": "Описание тест-кейса",
        "steps": ["Шаг 1", "Шаг 2"],
        "expected_result": "Ожидаемый результат",
        "priority": "средний"
    }

    # Отправляем POST-запрос на создание тест-кейса
    response = api_client.make_request(handle="/testcases", method="POST", json=test_case_data)

    # Логируем ответ
    log_response(response)

    # Проверяем, что статус-код 200 (создано)
    assert response.status_code == 200, "Ошибка: тест-кейс не создан"

    # Проверяем, что структура данных в ответе соответствует модели CaseModel
    created_case = CaseModel(**response.json())
    assert created_case.id == test_case_data["id"], "Ошибка: id не совпадает"
    assert created_case.name == test_case_data["name"], "Ошибка: имя не совпадает"
    assert created_case.description == test_case_data["description"], "Ошибка: описание не совпадает"
    assert created_case.steps == test_case_data["steps"], "Ошибка: шаги не совпадают"
    assert created_case.expected_result == test_case_data["expected_result"], "Ошибка: ожидаемый результат не совпадает"
    assert created_case.priority == test_case_data["priority"], "Ошибка: приоритет не совпадает"


def test_read_case_by_id(api_client):
    # Данные для чтения ранее созданного тест-кейса
    test_case_data = {
        "id": 104,
        "name": "Новый тест-кейс",
        "description": "Описание тест-кейса",
        "steps": ["Шаг 1", "Шаг 2"],
        "expected_result": "Ожидаемый результат",
        "priority": "средний"
    }

    # Отправляем GET-запрос на получение  тест-кейса по id
    response = api_client.make_request(handle=f"/testcases/{test_case_data['id']}", method="GET")

    # Логируем ответ
    log_response(response)

    # Проверяем, что статус-код 200
    assert response.status_code == 200, "Ошибка: тест-кейс не получен"

    # Проверяем, что структура данных в ответе соответствует модели CaseModel
    created_case = CaseModel(**response.json())
    assert created_case.id == test_case_data["id"], "Ошибка: id не совпадает"
    assert created_case.name == test_case_data["name"], "Ошибка: имя не совпадает"
    assert created_case.description == test_case_data["description"], "Ошибка: описание не совпадает"
    assert created_case.steps == test_case_data["steps"], "Ошибка: шаги не совпадают"
    assert created_case.expected_result == test_case_data["expected_result"], "Ошибка: ожидаемый результат не совпадает"
    assert created_case.priority == test_case_data["priority"], "Ошибка: приоритет не совпадает"


def test_update_case_by_id(api_client):
    # Данные для обновления предыдущего тест-кейса
    test_case_data = {
        "id": 104,
        "name": "Обновленный тест-кейс",
        "description": "Новое описание тест-кейса",
        "steps": ["Шаг 1- новый", "Шаг 2- новый", "Шаг 3 - добавлен"],
        "expected_result": "Новый ожидаемый результат",
        "priority": "низкий"
    }

    # Отправляем PUT-запрос на обновление тест-кейса
    response = api_client.make_request(handle=f"/testcases/{test_case_data['id']}", method="PUT", json=test_case_data)

    # Логируем ответ
    log_response(response)

    # Проверяем, что статус-код 200
    assert response.status_code == 200, "Ошибка: тест-кейс не обновлен"

    # Проверяем, что структура данных в ответе соответствует модели CaseModel
    updated_case = CaseModel(**response.json())
    assert updated_case.name == test_case_data["name"], "Ошибка: имя не совпадает"
    assert updated_case.description == test_case_data["description"], "Ошибка: описание не совпадает"
    assert updated_case.steps == test_case_data["steps"], "Ошибка: шаги не совпадают"
    assert updated_case.expected_result == test_case_data["expected_result"], "Ошибка: ожидаемый результат не совпадает"
    assert updated_case.priority == test_case_data["priority"], "Ошибка: приоритет не совпадает"


def test_delete_case_by_id(api_client):
    # Данные для удаления  тест-кейса по id
    test_case_data = {
        "id": 104
    }

    # Отправляем DELETE-запрос на удаление  тест-кейса по id
    response = api_client.make_request(handle=f"/testcases/{test_case_data['id']}", method="DELETE")

    # Логируем ответ
    log_response(response)

    # Проверяем, что статус-код 200
    assert response.status_code == 200, "Ошибка: тест-кейс не удален"

    # Отправляем GET-запрос на проверку удаления  тест-кейса по id
    response = api_client.make_request(handle=f"/testcases/{test_case_data['id']}", method="GET")

    # Логируем ответ
    log_response(response)

    # Проверяем, что статус-код 200
    assert response.status_code == 404, "Ошибка: тест-кейс не удален"