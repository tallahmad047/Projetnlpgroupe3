from flask import Flask, render_template, request, jsonify
import urllib.request
import json
# fichier2.py

# Importer la variable depuis fichier1
from traitement import prepation,traitement,decode


# Utiliser la variable
#print(ma_variable)


app = Flask(__name__)


@app.route('/')

def index():
    return render_template('index.html')
prepation()
@app.route('/make_api_call', methods=['POST'])
def make_api_call():
    
    text_data = request.data.decode('utf-8') 
    url="https://chichewa-endpoint-1613b162.westus2.inference.ml.azure.com/score"
    api_key='UaohoOhWnVtbMYuX9bZhxsbgvzBcVpmL'
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'chichewa' }
    body=traitement(text_data)

    

    #body = str.encode(json.dumps(json_data))
    req = urllib.request.Request(url, body, headers)
 
    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        
        result=decode(result)
        print("le résultat est "+str(result))
        return str(result)
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
    
        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(error.read().decode("utf8", 'ignore'))



   
        

if __name__ == '__main__':
    app.run(debug=True)
