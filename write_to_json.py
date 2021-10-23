import json


def write_to_json(string, dictionary):
    file_name = string + '.json'
    with open(file_name, 'w') as outfile:
        json.dump(dictionary, outfile)
