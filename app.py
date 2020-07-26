from flask import Flask, request
from data_filter import filtered_data, json_data
from flask import jsonify
import pycountry


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
        return jsonify({
            'author': 'Pranav Bhatia',
            'author_linkedin': 'https://www.linkedin.com/in/bhatiapranav/',
            'base_url': 'https://bcorps.herokuapp.com/  ',
            'project_name': 'B Corps - API',
            'project_url': 'https://github.com/PRANAVBHATIA1999/B-Corps-API'
        })

@app.route('/bcorps', methods = ['GET'])
def bcorps():
    if 'country' in request.args:            
        country = request.args.get('country')
        if len(country)==2:
            country_name = pycountry.countries.get(alpha_2=country)
            return filtered_data(country_name.name) if country_name is not None else 'Enter correct Country code/Country name'
        return filtered_data(country)
    else:
        return json_data()
    return country

if __name__ == '__main__':
    app.run(debug=False)
