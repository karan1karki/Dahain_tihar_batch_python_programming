import json
import os

def read_json(file_name):

    if not os.path.exists(file_name):
        return {}

    with open(file_name, "r") as file:
        return json.load(file)


def write_json(file_name, data):

    folder = os.path.dirname(file_name)

    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)