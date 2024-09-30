import json


def merg_json(files: list, output_file: str) -> None:
    rez = []

    for file in files:
        with open(file, 'r') as f:
            try:
                rez.extend(json.load(f))
            except json.JSONDecodeError:
                print(f'Ошибка при чтении файла: {file}')

    with open(output_file, 'w') as f:
        json.dump(rez, f, indent=4)


if __name__ == '__main__':
    merg_json(['zad_2\employees1.json', 'zad_2\employees2.json', 'zad_2\employees3.json'], 'output_file.json')