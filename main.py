from flask import Flask, request, jsonify
import pickle
from model_files.ml_model import predict_mpg


app = Flask('mpg_prediction')

# @app.route('/', methods=['GET'])
# def test():
#     return 'Pinging Model Application'



@app.route('/', methods=['POST'])
def predict():
    vehicle = request.get_json()
    print(vehicle)
    with open('./model_files/model.bin', 'rb') as f_in:
        model = pickle.load(f_in)
        f_in.close()
    predictions = predict_mpg(vehicle, model)
    result = {
        'mpg_prediction': list(predictions)
    }
    return jsonify(result)


# @app.route('/ping', methods=['GET'])
# def ping():
#     return "Pinging Model!!"

# Commented code below while deploying.
# if __name__ == '__main__':
#     app.run(debug=True, host='localhost', port=9696)