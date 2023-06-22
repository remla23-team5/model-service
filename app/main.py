import os

from app import create_app
from utils import download_model

def main(file_name, port):
    download_model(file_name)
    # Get the setiment result
    app = create_app()
    app.run(host="0.0.0.0", port=port, debug=False)

if __name__ == '__main__':
    # Download the model on start
    file_name = 'c2_Classifier_Sentiment_Model'

    port = int(os.environ.get('PORT', 8080))
    
    main(file_name, port)
