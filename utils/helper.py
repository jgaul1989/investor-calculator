import csv


def read_csv(file_name):
    with open(file_name, mode='r', encoding='utf-8') as file:
        return list(csv.DictReader(file))


def preprocess_data(data_set):
    for data in data_set:
        for key, value in data.items():
            if value == '':  # Check for empty strings
                data[key] = None  # Replace empty strings with None
    return data_set