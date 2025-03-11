from flask import Flask, render_template, request, flash, redirect, url_for
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Required for flash messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Format the message
        formatted_message = f"Name: {name}\nPhone: {phone}\nEmail: {email}\n\nMessage:\n{message}"
        
        # Create SendGrid message
        # Note: With free tier, this will show as "via sendgrid.net" in recipient's inbox
        message = Mail(
            from_email=Email("your-verified-sender@yourdomain.com", name=f"{name} (via Contact Form)"),
            to_emails=To("solrflam@gmail.com"),
            subject="New Contact Form Submission from Cool Galaxy Engineering",
            plain_text_content=Content("text/plain", formatted_message)
        )
        
        # Set reply-to to the user's email so replies go directly to them
        message.reply_to = Email(email, name=name)
        
        try:
            # Send email via SendGrid
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            
            if response.status_code >= 200 and response.status_code < 300:
                flash('Thank you for your message! We will get back to you soon.', 'success')
            else:
                flash('There was an error sending your message. Please try again later.', 'danger')
                
        except Exception as e:
            flash('There was an error sending your message. Please try again later.', 'danger')
            print(e)
            
        return redirect(url_for('contact'))
        
    return render_template('contact.html')

services = [
    {
        "id": 1,
        "name": "Installation Projects",
        "image": "static/img/installation works.jpg",
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