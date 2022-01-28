import os
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
# import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences
from process import process
from predict import predict

app = Flask(__name__)
api = Api(app)

# if not os.path.isfile('iris-model.model'):
#     train_model()


class MakePrediction(Resource):
    @staticmethod
    def post():
        posted_data = request.get_json()
        codeInput = posted_data['codeInput']
        code = process([codeInput])

        if code == []:
            return jsonify({
                'suggestion': ''
            })
        else:
            in_sents, out_sents = list(), list()
            for i in range(len(code)):
                in_, out = predict(posted_data['codeInput'], code[[i]])
                in_sents.append(in_)
                out_sents.append(out)

            return jsonify({
                'rawInput': posted_data['codeInput'],
                'processedInput': in_sents[0],
                'suggestion': out_sents[0]
            })


api.add_resource(MakePrediction, '/predict')


if __name__ == '__main__':
    # app.run(debug=True)
    # app.run(host='127.0.0.1', port=8080)
    app.run(host='0.0.0.0', port=8080)
