from flask import Flask, render_template, request, jsonify
import urllib.request
import json
from urllib.parse import urlencode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/make_api_call', methods=['GET'])
def make_api_call():
    url = "https://chichewa-endpoint-1613b162.westus2.inference.ml.azure.com/score"
    api_key = 'UaohoOhWnVtbMYuX9bZhxsbgvzBcVpmL'

    # Données à envoyer en tant que paramètres dans la requête GET
    input_data = {
        "feature1": "value1",
        "feature2": "value2",
        # Ajoutez autant de paramètres que nécessaire
    }

    # Ajouter les données à l'URL
    url += '?' + urlencode(input_data)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + api_key,
        'azureml-model-deployment': 'chichewa'
    }

    # Envoyer la requête GET
    req = urllib.request.Request(url, headers=headers)

    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        print("Réponse du service endpoint :", result.decode("utf-8"))
        return jsonify({"result": result.decode("utf-8")})
    except urllib.error.HTTPError as error:
        print("Erreur lors de la requête. Code statut :", error.code)
        print("Contenu de la réponse :", error.read().decode("utf-8"))
        return jsonify({"error": error.read().decode("utf-8")}), error.code

if __name__ == '__main__':
    app.run(debug=True)
