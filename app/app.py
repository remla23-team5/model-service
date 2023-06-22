from pathlib import Path
import joblib
from utils import PATH_TO_MODEL
import pandas as pd

from flask import Flask, jsonify, request
from flask_restx import Api
from lib2.preprocessing import prepare_stopwords, preprocess_data
from flasgger import Swagger

def create_app():
    app = Flask(__name__)
    api = Api(app)
    swagger = Swagger(app)

    @app.route('/predict', methods=['POST'])
    @api.doc(description='Swagger Generating an API documentation.')
    def predict():
        """
        Predicts the sentiment of a review to be positive or negative.
        ---
        parameters:
          - in: body
            name: body
            schema:
              id: review
              type: object
              required:
                - review
              properties:
                review:
                  type: string
                  description: The review to be classified
                  example: This restaurant is great!
        responses:
          200:
            description: "The prediction of sentiment: 'positive' (1) or 'negative' (0)."
        """


        #Fetch the model
        file_name = 'c2_Classifier_Sentiment_Model'
        model = joblib.load(PATH_TO_MODEL + file_name)

        # Ingredients for data preprocess
        ps, all_stopwords = prepare_stopwords()

        # Data preprocess
        input_data = request.get_json()
        review = input_data.get('review')
        reviewPre = preprocess_data(review, ps, all_stopwords)
        reviewDf = pd.DataFrame({'Review': [reviewPre]})

        # Predict
        prediction = int(model.predict(reviewDf))
        
        res = {
            "result": prediction,
            "classifier": "multinomial naive bayes",
            "review": review
        }
        
        return jsonify(res)
    
    return app