import zipfile
# Data set Link:  https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia
zip_ref = zipfile.ZipFile('')
zip_ref.extractall('/content/chest-xray-pnemonia.zip', 'r')
zip_ref.extractall('/content')
zip_ref.close()