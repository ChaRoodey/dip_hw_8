import os
import csv
import json
import pickle


def path_creater(dirr: str) -> None:
    rep = []
    obh = {}
    for root, dirs, files in os.walk(dirr):
        for file in files:
            obh['type'] = 'file'
            obh['name'] = file
            obh['root_dir'] = root
            obh['size'] = os.path.getsize(file)
            rep.append(obh)

        for d in dirs:
            obh['type'] = 'dir'
            obh['name'] = d
            obh['root_dir'] = root
            obh['size'] = os.path.getsize(d)
            rep.append(obh)

    print(rep)


if __name__ == '__main__':
    path_creater('.zad_3')