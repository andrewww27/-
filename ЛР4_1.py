import json

def task() -> float:
    filename = 'input.json'
    try:
        # Уровень 1: внутри блока try
        with open(filename, 'r', encoding='utf-8') as f:
            # Уровень 2: внутри блока with (работа с файлом)
            data = json.load(f)

        # Снова Уровень 1: файл закрыт, считаем сумму
        total_sum = sum(item["score"] * item["weight"] for item in data)
        return round(total_sum, 3)

    except FileNotFoundError:
        # Уровень 1: код, если файл не найден
        print(f"Ошибка: Файл {filename} не найден.")
        return 0.0
    except (KeyError, TypeError) as e:
        # Уровень 1: код, если в JSON не те ключи
        print(f"Ошибка в структуре данных: {e}")
        return 0.0


print(task())
