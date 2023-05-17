import pickle
import joblib
import pandas as pd

from flask import Flask, jsonify, request
from flask_restx import Api, Resource
from text_preprocessing import prepareStopwords, dataPreprocess
from flasgger import Swagger

from utils import download_model


app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

@app.route('/predict', methods=['POST'])
@api.doc(description='Swagger Generating an API documentation.')
def predict():
    """
    Predict the sentiment of a review.
    ---
    consumes:
      - application/json
    parameters:
        - name: input_data
          in: body
          description: message to be classified.
          required: True
          schema:
            type: object
            required: review
            properties:
                review:
                    type: string
                    example: This is an example of an review.
    responses:
      200:
        description: "The prediction of sentiment: 'positive' or 'negative'."
    """
    #Fetch the model
    file_name = 'c2_Classifier_Sentiment_Model'
    model = joblib.load('./src/' + file_name)

    # Ingredients for data preprocess
    ps, all_stopwords = prepareStopwords()
    cvFile='./src/c1_BoW_Sentiment_Model.pkl'
    cv = pickle.load(open(cvFile, "rb"))

    # Data preprocess
    input_data = request.get_json()
    review = input_data.get('review')
    reviewPre = dataPreprocess(review, ps, all_stopwords)
    reviewDf = pd.DataFrame({'Review': [reviewPre]})

    # Predict
    prediction = int(model.predict(reviewDf))
    
    res = {
        "result": prediction,
        "classifier": "decision tree",
        "review": review
    }
    print(res)
    return jsonify(res)

if __name__ == '__main__':
    # Download the model on start
    file_name = 'c2_Classifier_Sentiment_Model'
    download_model(file_name)
    # Get the setiment result
    app.run(host="0.0.0.0", port=8080, debug=True)
