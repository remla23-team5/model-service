import requests
import os

# download the model on-start
def download_model(file_name):
    # create local folder for the downloaded model
    folder_path = './src'
    create_folder(folder_path)

    # download from github
    github_url = 'https://raw.githubusercontent.com/'
    file_url = github_url + 'remla23-team5/model-training/main/models/' + file_name
    response = requests.get(file_url)
    if response.status_code == 200:
        with open(folder_path + '/' + file_name, 'wb') as f:
            f.write(response.content)
        print('Model downloaded successfully.')
    else:
        print('Model download failed.')

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created successfully.")
    else:
        print(f"Folder '{folder_path}' already exists.")

if __name__ == '__main__':
    download_model()