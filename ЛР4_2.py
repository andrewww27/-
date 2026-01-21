# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, mode="r", encoding="utf-8") as csv_f:  # TODO считать содержимое csv файла
        reader = csv.DictReader(csv_f)
        data = [row for row in reader]
    with open(OUTPUT_FILENAME, mode="w", encoding="utf-8") as json_f:
        json.dump(data, json_f, indent=4, ensure_ascii=False)

# TODO Сериализовать в файл с отступами равными 4

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")
