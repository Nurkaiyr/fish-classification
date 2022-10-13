import streamlit as st

st.title("Description of the project")

st.markdown("Github page of the project: [link](https://github.com/Nurkaiyr/fish-classification)")
st.markdown("The dataset consists of **20 Mediterranean fish species** with _2000_ images for per fish species. Overall, _40 000_ images were produced.")
st.markdown("Following that, it was divided into training and testing sets with a proportion of _85_ and _15_ percent, respectively.")
st.markdown(">Dataset is available at this [link](https://www.kaggle.com/datasets/giannisgeorgiou/fish-species) ") 

st.markdown('''In this work, several models were used for classification task. 
- EfficientNet
- MobileNetV2
- Custom Model 
Due to resource constraints model were trained only for 10 epochs. 
> Note: only **EfficientNet** is on demo app. This is due to the limits of resources. For example, custom model's file size were 300 MB.''')

st.markdown("All _analysis_ and _trainings_ are able to view in [**Fish-Classification.ipynb**](https://github.com/Nurkaiyr/fish-classification/blob/master/Fish-Classification.ipynb) file.")

st.header('EfficientNet')
with st.expander("EfficientNet model plots"):
    st.subheader('Accuracy')
    st.image('https://github.com/Nurkaiyr/fish-classification/blob/master/Plots/EfficientNet-accuracy.png?raw=true')
    st.subheader('Loss')
    st.image('https://github.com/Nurkaiyr/fish-classification/blob/master/Plots/EfficientNet-loss.png?raw=true')

st.header('MobileNet')
with st.expander("MobileNet model plots"):
    st.subheader('Accuracy')
    st.image('https://github.com/Nurkaiyr/fish-classification/blob/master/Plots/MobileNetV2-accuracy.png?raw=true')
    st.subheader('Loss')
    st.image('https://github.com/Nurkaiyr/fish-classification/blob/master/Plots/Custom-model-loss.png?raw=true')

st.header("Custom model")
st.markdown("For the custom model, there were applied several **Convolutional** layers with **ReLU** activation function, \
                followed by **Batch Normalization** layers and **MaxPooling** and **Dropout** layers. \
                In addition, several **Dense**(Fully-connected) layers were added with final output of 20 classes.")
with st.expander("Custom model architecture"):
    st.image('https://i.ibb.co/vv87dLh/custom-model-20-h5.png')
with st.expander("Custom model plots"):
    st.subheader('Accuracy')
    st.image('https://github.com/Nurkaiyr/fish-classification/blob/master/Plots/CustomModel-accuracy.png?raw=true')
    st.subheader('Loss')
    st.image('https://github.com/Nurkaiyr/fish-classification/blob/master/Plots/MobileNetV2-loss.png?raw=true')