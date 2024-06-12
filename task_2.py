# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ —
# значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое
# представление.

def fun(**kwargs):
    result = {}
    for key in kwargs:
        if (kwargs[key].__hash__):
            result[kwargs[key]] = key
        else:
            result[str(kwargs[key])] = key
    return result


print(fun(bananas=23, apples=(234, 456), potato=[345, 456, 667]))