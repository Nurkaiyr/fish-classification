import streamlit as st

st.title("Description of the project")

st.markdown("Github page of the project: [link](https://github.com/Nurkaiyr/fish-classification)")
st.markdown('Used libraries: Tensorflow, Keras, OpenCV, pandas, NumPy, seaborn')

st.subheader('Problem statement')
st.markdown('''
In order to protect the environment and ensure sustainable natural fisheries that can meet the
demands of an ever-increasing human population, it is essential to understand and simulate
how fish react to factors such as climate change, habitat degradation and environmental
changes. Effective monitoring is a crucial foundational step for decision support systems that
help detect issues and organise solutions to protect and restore the environment.
In order to correctly categorise fish species, this research focuses on comprehending several
Deep Learning Algorithms. 
''')
st.subheader('The goal of the project')
st.markdown('''
The main goal of this study is to build a multi-class classification application that can classify fish species by image.

In addition:
- To learn more about deep learning by reading about it and using it.
- To research current computer vision methods and architectures. ''')

st.subheader("Dataset")
st.markdown("The dataset consists of **20 Mediterranean fish species** with _2000_ images for per fish species. Overall, _40 000_ images were produced.")
st.markdown("Following that, it was divided into training and testing sets with a proportion of _85_ and _15_ percent, respectively.")
st.markdown(">The dataset is available at this [link](https://www.kaggle.com/datasets/giannisgeorgiou/fish-species) ") 

st.markdown('''In this work, several models were used for classification task. 
- EfficientNet
- MobileNetV2
- Custom Model 
Due to resource constraints, models were trained only for 10 epochs.
> Please keep in mind that the demo app only includes **EfficientNet**.This is due to the limits of resources. For example, the custom model's file size was 300 MB.''')

st.markdown("All of the _analysis_ and _trainings_ can be seen in [**Fish-Classification.ipynb**](https://github.com/Nurkaiyr/fish-classification/blob/master/Fish-Classification.ipynb) file.")

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
    st.image('https://github.com/Nurkaiyr/fish-classification/blob/master/Plots/MobileNetV2-loss.png?raw=true')

st.header("Custom model")
st.markdown("For the custom model, there were applied several **Convolutional** layers with **ReLU** activation function, \
                followed by **Batch Normalization** layers and **MaxPooling** and **Dropout** layers. \
                In addition, several **Dense**(Fully-connected) layers were added with final output of 20 classes.")
with st.expander("Custom model architecture"):
    st.image('https://github.com/Nurkaiyr/fish-classification/blob/master/Plots/Custom-model-architecture.png?raw=true')
with st.expander("Custom model plots"):
    st.subheader('Accuracy')
    st.image('https://github.com/Nurkaiyr/fish-classification/blob/master/Plots/CustomModel-accuracy.png?raw=true')
    st.subheader('Loss')
    st.image('https://github.com/Nurkaiyr/fish-classification/blob/master/Plots/Custom-model-loss.png?raw=true')
    st.markdown("> Note: This loss plot after addition 10 epochs trainings. Training of this model was saved and continued for another 10 epochs.")