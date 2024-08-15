#     Необходимо создать функцию, которая принимает объект (любого типа)
#     в качестве аргумента и проводит интроспекцию этого объекта, чтобы
#     определить его тип, атрибуты, методы, модуль, и другие свойства.
#
# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.

# 2. Используйте встроенные функции и методы интроспекции Python
# для получения информации о переданном объекте.
#
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
#    - Тип объекта.
#    - Атрибуты объекта.
#    - Методы объекта.
#    - Модуль, к которому объект принадлежит.

import inspect


def introspection_info(obj):
    obj_type = type(obj)
    obj_type_name = obj_type.__name__
    obj_module = inspect.getmodule(obj)
    obj_module_name = obj_module.__name__ if obj_module else 'Built-in'
    all_attributes = dir(obj)
    methods = []
    attributes = []
    for attribute in all_attributes:
        attr_value = getattr(obj, attribute)
        if inspect.ismethod(attr_value) or inspect.isfunction(attr_value):
            methods.append(attribute)
        else:
            attributes.append(attribute)

    info = {
        'Тип объекта': obj_type_name,
        'Модуль': obj_module_name,
        'Атрибуты': attributes,
        'Методы': methods
    }
    return info


if __name__ == "__main__":
    class SomeClass:
        """Пример класса"""

        def somemethod(self):
            """Пример метода"""
            pass


    example_obj = SomeClass()
    info = introspection_info(example_obj)
    for key, value in info.items():
        print(f"{key}: {value}")
