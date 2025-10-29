from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = '0102040a4acaf44928d8cc9253a1d25afa34a54edfc28cbbaaa586e828136712'  # Replace with your secret key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # --- Email setup (replace with your real school email details) ---
        sender = "jezrockoduro@gmail.com"      # your Gmail
        password = "pdtggzibrgkwgrtg"  # use Gmail app password
        receiver = "crownprinceschool5@gmail.com"  # where the form sends messages

        msg = EmailMessage()
        msg['Subject'] = f"New Message from {name}"
        msg['From'] = sender
        msg['To'] = receiver
        msg.set_content(f"From: {name}\nEmail: {email}\n\nMessage:\n{message}")

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(sender, password)
                smtp.send_message(msg)
            flash('Message sent successfully!', 'success')
        except Exception as e:
            print(e)
            flash('Something went wrong. Please try again later.', 'error')

        return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
