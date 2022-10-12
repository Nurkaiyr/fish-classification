import streamlit as st
import tensorflow as tf
import requests, io, cv2
import numpy as np

from keras.models import load_model
from PIL import Image

from streamlit_image_select import image_select

def main():
    st.title("🐟 Fish classification Demo App")
    st.subheader("📁 Upload an image of a fish to classify its species")

    # Loading the models
    modelEF = load_model('./model_efficientNet_NEW.h5')
    
    # uploading the image
    file = st.file_uploader("Upload an image here") # type=['jpg', 'png', 'jpeg']
    if not file:
        file = image_select("🖱️ Select pre-loaded image here", ["Images_to_test/Anthias_anthias.jpg", "Images_to_test/Belone_Belone.jpg",
                                                             "Images_to_test/Coris_Julis-3.jpg", "Images_to_test/scomber_japonicus-1722.jpg"],
                        captions=['Anthias_anthias', 'Belone_Belone', 'Coris_Julis', 'Scomber_Japonicus'])
    else:
        image_data = file.getvalue()
        st.image(image_data) # show image

    cv_im = cv2.cvtColor(np.array(Image.open(file)), cv2.COLOR_RGB2BGR) # converting because openCV library works with B-G-R order(Blue-Green-Red)
    IMAGE_SIZE=[224,224]
    internal_image = cv2.resize(cv_im,IMAGE_SIZE) # resizing to 224x224
    internal_image = internal_image.reshape(1,IMAGE_SIZE[0], IMAGE_SIZE[1],3) # changing the dimensions to predict

    # dictionary to map fish species name with number
    dict_class = {'Anthias anthias': 0, 'Atherinomorus lacunosus': 1, 'Belone belone': 2, 'Boops boops': 3, 'Chlorophthalmus agassizi': 4, 'Coris julis': 5, 'Dasyatis centroura': 6, 'Epinephelus caninus': 7, 'Gobius niger': 8, 'Mugil cephalus': 9, 'Phycis phycis': 10, 'Polyprion americanus': 11, 'Pseudocaranx dentex': 12, 'Rhinobatos cemiculus': 13, 'Scomber japonicus': 14, 'Solea solea': 15, 'Squalus acanthias': 16, 'Tetrapturus belone': 17, 'Trachinus draco': 18, 'Trigloporus lastoviza': 19}

    # to show the fish species name instread of number
    labels = [None] * len(dict_class)
    for k, v in dict_class.items():
        labels[v] = k

    # Prediction buttons
    resultEF = st.button('Predict with EfficientNet')

    if resultEF:
        with st.spinner("Calculating results..."):
            p = modelEF.predict(internal_image)
        # p = np.argmax(p) # if you want only 1 prediction
        prediction_probabilities = tf.nn.top_k(p, k=2) # top 2 predictions with confidence
        top_2_scores = prediction_probabilities.values.numpy() # how much model confident 
        dict_class_entries = prediction_probabilities.indices.numpy() # get the relevant number then mapping to show the fish species
        st.metric(labels[dict_class_entries[0][0]], round(top_2_scores[0][0] * 100,2))
        st.metric(labels[dict_class_entries[0][1]], round(top_2_scores[0][1] * 100,2))


if __name__ == '__main__':
    main()