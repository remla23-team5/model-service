import pickle
import joblib

from flask import Flask, jsonify, request
from text_preprocessing import prepareStopwords, dataPreprocess
from flasgger import Swagger


app = Flask(__name__)
swagger = Swagger(app)

@app.route('/predict', methods=['POST'])
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
    model = joblib.load('./src/c2_Classifier_Sentiment_Model')

    # Ingredients for data preprocess
    ps, all_stopwords = prepareStopwords()
    cvFile='./src/c1_BoW_Sentiment_Model.pkl'
    cv = pickle.load(open(cvFile, "rb"))

    # Data preprocess
    input_data = request.get_json()
    review = input_data.get('review')
    reviewPre = dataPreprocess(review, ps, all_stopwords)
    processed_input = cv.transform([reviewPre]).toarray()[0]

    # Predict
    prediction = int(model.predict([processed_input])[0])
    
    res = {
        "result": prediction,
        "classifier": "decision tree",
        "review": review
    }
    print(res)
    return jsonify(res)

if __name__ == '__main__':
    # Get the setiment result
    app.run(host="0.0.0.0", port=8080, debug=True)
