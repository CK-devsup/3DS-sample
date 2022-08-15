from flask import Flask, render_template, request, send_file
import pandas
import json
import requests

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/submit', methods=['POST'],)
def home():
    print("Hello!")
    card = request.form["card"]
    amount = request.form["amount"]
    exp = request.form["exp"]
    fname = request.form["firstname"]
    lname = request.form["lastname"]
    street = request.form["street"]
    city = request.form["city"]
    print('lol')
    state = request.form["state"]
    zip = request.form["zip"]
    mobile = request.form["phone"]
    print('lol')
    email = request.form["email"]
#    refid = request.form["x3dsReferenceId"]
#    istatus = request.form["x3dsInitializeStatus"]
    print('lol')
    print(card, amount, exp)
    headers = {
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
        "xEmail": email,
        "xBillMobile": mobile,
        "xBillZip": zip,
        "xBillState": state,
        "xBillCity": city,
        "xBillStreet": street,
        "xBillLastName": lname,
        "xBillFirstName": fname,
        "xcardnum": card,
        "xexp": exp,
        "xkey": "artemisdev9d423588838a438f9036c65c3318140c",
        "xversion": "5.0.0",
        "xsoftwarename": "Nosson",
        "xsoftwareversion": "2.3.5",
        "xcommand": "cc:sale",
        "xamount": amount,
        "xallowduplicate": "True"
        })
    url = "https://x1.cardknox.com/gatewayjson"
    print("Heyo")
    response = requests.request(
                "POST", url, headers=headers, data=payload)
    response = response.json()   
    print(response)
    return json.dumps({'status':'OK', 'response':response})

if __name__ == "__main__":
    application.run(debug=False, host="0.0.0.0", port=8080)