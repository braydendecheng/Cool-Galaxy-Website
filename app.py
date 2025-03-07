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
        "name": "Installation Projects",
        "image": "static\img\installation works.jpg",
        "description": "Our expert team handles the installation of various air conditioning systems, ensuring optimal performance and energy efficiency for your space."

    },
    {
        "id": 2,
        "name": "VRV Systems",
        "image": "static/img/VRV Systems.jpg",
        "description": "We offer advanced Variable Refrigerant Volume (VRV) systems that provide flexible and energy-efficient climate control suitable for diverse environments."
    },
    {
        "id": 3,
        "name": "Ducting Work",
        "image": "static/img/Ducting Work.jpg",
        "description": "Our specialists are proficient in designing and installing ducting systems that facilitate efficient air distribution while maintaining aesthetic appeal."
    },
    {
        "id": 4,
        "name": "Servicing and Maintenance",
        "image": "static/img/ac-technician.jpg",
        "description": "We provide regular maintenance and servicing to ensure your air conditioning systems operate at peak performance, prolonging their lifespan and enhancing energy efficiency."
    }
    
]

@app.route('/services')
def service_page():
    return render_template('services.html', services=services)

if __name__ == '__main__':
    app.run(debug=True)