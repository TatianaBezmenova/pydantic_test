import datetime
import json
from typing import List

from pydantic import BaseModel, ValidationError, Field, PositiveInt


class Animal(BaseModel):
    """Пример модели данных.

    Пример с переименованием переменной.
    """
    name: str = Field(alias='animalName')
    birthday: datetime.date


class Person(BaseModel):
    """Пример модели данных.

    Пример с вложенной моделью.
    """
    name: str
    age: PositiveInt
    animals: List[Animal]


def process(data: json):
    """Парсит входные данные их JSONа в объект и проверяет их с помощью Pydantic"""
    print('-------')
    try:
        # Получим объект
        person = Person.model_validate_json(data)
        print(f'Объект: {person}')
    except ValidationError as e:
        print('Ошибка во входящих данных.')
        print(e.json(indent=2))
    else:
        # Изменим объект и преобразуем его обратно в json
        person.name = person.name.upper()
        print(person.model_dump_json(by_alias=True))


# Пример использования
data_1 = """{
    "name": "Алиса",
    "age": 25,
    "animals": [
        {"animalName": "Барсик", "birthday": "2023-11-11"}
    ]
}"""
process(data_1)

data_2 = """{
    "name": "Боб",
    "age": -25,
    "animals": [
        {"animalName": "Барсик", "birthday": "2023-11-11"}
    ]
}"""
process(data_2)

data_3 = """{
    "name": "Вася",
    "age": -4,
    "animals": 'нет'
}"""
process(data_3)
