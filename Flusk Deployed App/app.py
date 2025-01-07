import os
from flask import Flask, redirect, render_template, request, flash, url_for
from PIL import Image
import torchvision.transforms.functional as TF
import CNN
import numpy as np
import torch
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


disease = pd.read_csv('disease.csv' , encoding='cp1252')
supplement = pd.read_csv('supplement.csv',encoding='cp1252')

model = CNN.CNN(39)    
model.load_state_dict(torch.load("model.pt"))
model.eval()

def prediction(image_path):
    image = Image.open(image_path)
    image = image.resize((224, 224))
    input_data = TF.to_tensor(image)
    input_data = input_data.view((-1, 3, 224, 224))
    output = model(input_data)
    output = output.detach().numpy()
    index = np.argmax(output)
    return index

app = Flask(__name__)

app.secret_key = "200034"

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "hafizur.rahman@sec.ac.bd"
EMAIL_PASSWORD = "gdpx eeah nbup kvac"

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'GET':
        return render_template('submit.html')
    else:
        image = request.files['image']
        filename = image.filename
        upload_folder = 'static/uploads'
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        file_path = os.path.join(upload_folder, filename)
        image.save(file_path)
        print(file_path)
        pred = prediction(file_path)
        title = disease['disease_name'][pred]
        description =disease['description'][pred]
        prevent = disease['Possible Steps'][pred]
        print(title," Description: ",description)
        image_url = disease['image_url'][pred]
        supplement_name = supplement['supplement name'][pred]
        supplement_image_url = supplement['supplement image'][pred]
        supplement_buy_link = supplement['buy link'][pred]
        return render_template('submit.html', title = title, desc = description, prevent = prevent, 
                               image_url = image_url, pred = pred,sname = supplement_name, simage = supplement_image_url, 
                               buy_link = supplement_buy_link)
@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')

    if not name or not email or not subject or not message:
        flash("All fields are required!", "danger")
        return redirect(url_for('home', _anchor='contact'))

    # Create the email content
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS
        msg['Subject'] = f"New Message from {name}"

        body = f"""
        Name: {name}
        Email: {email}
        Subject: {subject}
        Message:
        {message}
        """
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        flash("Message sent successfully!", "success")
    except Exception as e:
        flash(f"Failed to send message: {str(e)}", "danger")

    return redirect(url_for('home', _anchor='contact'))

app.run(debug=True)