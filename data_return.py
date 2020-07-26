
def json_data():  
    with open('json_data.txt', 'r', encoding='utf-8-sig') as data_file:
        x = data_file.read()
    return x