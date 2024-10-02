import os
import csv
import json
import pickle


def path_creater(dirr: str) -> None:
    rep = []
    for root, dirs, files in os.walk(dirr):
        for file in files:
            obh = {}
            obh['type'] = 'file'
            obh['name'] = file
            obh['root_dir'] = root
            obh['size'] = os.path.getsize(f'{root}/{file}')
            rep.append(obh)

        for d in dirs:
            obh = {}
            obh['type'] = 'dir'
            obh['name'] = d
            obh['root_dir'] = root
            obh['size'] = os.path.getsize(f'{root}/{d}')
            rep.append(obh)

    if rep:
        import_paths(rep)
    else:
        print('Каталог пуст')

def import_paths(paths):
    with open('zad_1/paths.json', 'w') as f:
        json.dump(paths, f, indent=4)

    with open('zad_1/paths.csv', 'w') as f:
        header = paths[0].keys()
        csv_paths = csv.DictWriter(f, fieldnames=header)
        csv_paths.writeheader()
        csv_paths.writerows(paths)

    with open('zad_1/paths.pickle', 'bw') as f:
        for row in paths:
            pickle.dump(row, f)


if __name__ == '__main__':
    path_creater('zad_3')