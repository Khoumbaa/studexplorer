from flask import Flask, render_template, request
import random
import os
import requests
import json

app = Flask(__name__, template_folder='template')

def find_category(city_name, category, api_key):
    categories_endpoints = {
        "restaurants": "restaurant",
        "supermarches": "grocery_or_supermarket",
        "sport": ["gym", "stadium", "yoga_studio", "natation_club", "handball_club", "football_club", "hockey_club", "basketbal_club", ],  
        "fastfood": "fast_food",
        "divertissement": ["movie_theater", "museum", "bowling_alley", "escape_game", "theater", "concert", "amusement_park", "laser_game", "karting"]  
    }

    query = f"{category} in {city_name}"
    params = {
        "query": query,
        "key": api_key
    }

    response = requests.get(f"https://maps.googleapis.com/maps/api/place/textsearch/json?type={','.join(categories_endpoints[category])}", params=params)

    if response.status_code == 200:
        data = json.loads(response.text)

        results = [place["name"] for place in data.get("results", [])]
        
        cheap_results = [(place["name"], place.get("formatted_address", "")) for place in data.get("results", [])]
        
        random_results = random.sample(cheap_results, min(5, len(cheap_results)))
        return random_results
    else:
        return []

@app.route('/application.html')
def application():
    return render_template('application.html')
    
@app.route('/applicationen.html')
def applicationen():
	return render_template('applicationen.html')

@app.route('/applicationes.html')
def applicationes():
	return render_template('applicationes.html')

@app.route('/faq.html')
def faq():
    return render_template('faq.html')

@app.route('/faqen.html')
def faqen():
    return render_template('faqen.html')  
    
@app.route('/faqes.html')
def faqes():
    return render_template('faqes.html')  
    
@app.route('/point.html')
def point():
    return render_template('point.html')

@app.route('/pointen.html')
def pointen():
    return render_template('pointen.html')
    
@app.route('/pointes.html')
def pointes():
    return render_template('pointes.html')

@app.route('/indexen.html', methods=['GET', 'POST'])
def chatbot_en():
    show_text_input = False
    recommendations = []
    contact_creators_text = None
    report_error_text = None

    if request.method == 'POST':
        user_input = request.form['user_input']

        if user_input == "Contact us":
            contact_creators_text = "Send us an email at : studexplorer@gmail.com"
        elif user_input == "Report an error":
            report_error_text = "Send us an email at : studexplorer@gmail.com"
        elif user_input == "I want to find a cheap place to":
            show_text_input = True
        elif user_input in ["restaurants", "supermarches", "sport", "fastfood", "divertissement"]:
            city = request.form['city']
            
            recommendations = find_category(city, user_input, "#CLÉ API")

    return render_template('indexen.html', show_text_input=show_text_input, recommendations=recommendations, contact_creators_text=contact_creators_text, report_error_text=report_error_text)

@app.route('/indexes.html', methods=['GET', 'POST'])
def chatbot_es():
    show_text_input = False
    recommendations = []
    contact_creators_text = None
    report_error_text = None

    if request.method == 'POST':
        user_input = request.form['user_input']

        if user_input == "Contáctenos":
            contact_creators_text = "Envíenos un correo electrónico a: studexplorer@gmail.com"
        elif user_input == "Reportar un error":
            report_error_text = "Envíenos un correo electrónico a: studexplorer@gmail.com"
        elif user_input == "Quiero encontrar un lugar económico para":
            show_text_input = True
        elif user_input in ["restaurants", "supermarches", "sport", "fastfood", "divertissement"]:
            city = request.form['city']
            
            recommendations = find_category(city, user_input, "#CLÉ API")

    return render_template('indexes.html', show_text_input=show_text_input, recommendations=recommendations, contact_creators_text=contact_creators_text, report_error_text=report_error_text)


@app.route('/index.html', methods=['GET', 'POST'])
def chatbot():
    show_text_input = False
    recommendations = []
    contact_creators_text = None
    report_error_text = None

    if request.method == 'POST':
        user_input = request.form['user_input']

        if user_input == "Je veux contacter tes créateurs":
            contact_creators_text = "Contactez-nous à l'adresse e-mail : studexplorer@gmail.com"
        elif user_input == "Je veux reporter une erreur":
            report_error_text = "Envoyez un e-mail à etudexplorers@gmail.com"
        elif user_input == "Je cherche un lieu":
            show_text_input = True
        elif user_input in ["restaurants", "supermarches", "sport", "fastfood", "divertissement"]:
            city = request.form['city']
            
            recommendations = find_category(city, user_input, "#CLÉ API")

    return render_template('index.html', show_text_input=show_text_input, recommendations=recommendations, contact_creators_text=contact_creators_text, report_error_text=report_error_text)
if __name__ == '__main__':
    app.run(debug=True)