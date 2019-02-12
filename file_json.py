from files_and_json import way_file
import json

# Перевод json в словарь
if __name__ == '__main__':
    data = way_file('data.json')
    # print(data)
    obj = json.loads(data)
    print(obj,type(obj))

    # добавление нового элемента в словарь
    obj["new_key"] = "new_value"
    # создание из словаря объект вида json
    text_json_obj = json.dumps(obj,sort_keys=True,indent=10)
    print(text_json_obj)