import csv
import json


def json_to_csv(name_json: str) -> None:
    with open(name_json, 'r') as fj:
        json_data = json.load(fj)

    with open('zad_3\products.csv', 'w') as fc:
        headers = json_data[0].keys()
        csv_data = csv.DictWriter(fc, fieldnames=headers)
        csv_data.writeheader()
        csv_data.writerows(json_data)


if __name__ == '__main__':
    json_to_csv('zad_3\products.json')