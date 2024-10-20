import inspect, pprint

def introspection_info(obj):
    info = {
        'type': type(obj).__name__,
        'attributes': dir(obj),
        'methods': [method for method in dir(obj) if inspect.isfunction(getattr(obj, method))],
        'module': inspect.getmodule(obj)
    }
    return info


# Пример использования
number_info = introspection_info(42)
pprint.pprint(number_info)