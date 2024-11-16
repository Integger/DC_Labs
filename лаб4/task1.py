import json

# TODO решите задачу
def task() -> float:
    try:
        with open ('input.json') as json_file:
            data = json.load(json_file)

            value_to_return = 0.0

            for element in data:
                value_to_return += element['score'] * element['weight']

            return round(value_to_return, 3)

    except json.JSONDecodeError as e:
        print (f'Ошибка декодирования input.json: {e}')
    except FileNotFoundError:
        print (f'Файл input.json не был найден')

    return 0.0


print(task())
