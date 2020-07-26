import json 

with open('json_data.txt', 'r',encoding="utf-8") as data: 
    y = json.loads(data.read())


def filtered_data(country_name):
    filter_country = {}
    for item in y:
        country = y[item]['location'].split(', ')[-1]
        if country.lower() == country_name.lower():
            filter_country[item] = y[item]      
    json_output = json.dumps(filter_country, ensure_ascii=False)
    return json_output if len(filter_country) !=0 else "Enter correct Country code/Country name"

def json_data():  
    with open('json_data.txt', 'r', encoding='utf-8-sig') as data_file:
        x = data_file.read()
    return x