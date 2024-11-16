# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    raw_content = []

    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        raw_content = list(csv_reader)

    if raw_content:
        content = []

        column_num = len (raw_content[0])
        row_num = len (raw_content)

        for row_counter in range(1, row_num):
            dict_to_append = {}

            for column_counter in range(0, column_num):
                dict_to_append[raw_content[0][column_counter]] = raw_content[row_counter][column_counter]

            content.append(dict_to_append)

     # TODO Сериализовать в файл с отступами равными 4
        with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as json_file:
            json.dump(content, json_file, indent=4)
    else:
        print ("Cannot read csv file")

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")