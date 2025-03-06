from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

services = [
    {
        "id": 1,
        "name": "Aircon Servicing",
        "image": "static/img/ac-technician.jpg",
        "description": "Professional removal of built-up jelly-like substances in your air conditioning unit. This sticky residue can reduce efficiency and lead to system failure if not properly cleaned."
    },
    {
        "id": 2,
        "name": "Installation Project",
        "image": "static/images/condenser_dirty.jpg",
        "description": "Deep cleaning of dirty condensers to prevent overheating. Our thorough cleaning process removes dirt, debris, and other contaminants that can cause your system to work harder and consume more energy."
    },
    {
        "id": 3,
        "name": "VRV System",
        "image": "static/images/aircon_clean.jpg",
        "description": "Complete cleaning of your entire aircon system. We clean all components including filters, coils, fins, and drainage systems to ensure optimal performance and air quality."
    },
    {
        "id": 4,
        "name": "Ducting Work",
        "image": "static/images/preventive_maintenance.jpg",
        "description": "Regular maintenance service to prevent breakdowns and extend the life of your air conditioning system. Includes inspection, cleaning, and minor repairs."
    },
    {
        "id": 5,
        "name": "Residential Projects",
        "image": "static/images/chemical_overhaul.jpg",
        "description": "Comprehensive chemical cleaning process that removes stubborn dirt, mold, and bacteria from your system. Improves cooling efficiency and indoor air quality."
    },
    {
        "id": 6,
        "name": "Chemical Overhaul Servicing",
        "image": "static/images/low_gas.jpg",
        "description": "Precise measurement of refrigerant levels to identify leaks or insufficient cooling capacity. Low refrigerant levels can lead to poor cooling performance and system damage."
    },
    {
        "id": 7,
        "name": "Commercial Installation With Ducting Work",
        "image": "static/images/gas_topup.jpg",
        "description": "Professional refrigerant recharging service. We use the correct type and amount of refrigerant to restore your system's cooling efficiency."
    }
    
]

@app.route('/services')
def service_page():
    return render_template('services.html', services=services)

if __name__ == '__main__':
    app.run(debug=True)