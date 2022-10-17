# 🐟 Fish Classification

# Web Application
> A demonstration is available at: https://fish-classification.streamlitapp.com/
## Used libraries
- Tensorflow, Keras, OpenCV, pandas, NumPy, seaborn

# Problem Statement
In order to protect the environment and ensure sustainable natural fisheries that can meet the
demands of an ever-increasing human population, it is essential to understand and simulate
how fish react to factors such as climate change, habitat degradation and environmental
changes. Effective monitoring is a crucial foundational step for decision support systems that
help detect issues and organise solutions to protect and restore the environment.
In order to correctly categorise fish species, this research focuses on comprehending several
Deep Learning Algorithms. 

# The goal of the project
The main goal of this study is to build a multi-class classification application that can classify fish species by image.

In addition:
- To learn more about deep learning by reading about it and using it.
- To research current computer vision methods and architectures.

# Dataset
The dataset consists of _20 Mediterranean fish species_ with _2000_ images for per fish species.
Overall, _40 000_ images were produced. 

Following that, it was divided into training and testing sets with a proportion of _85_ and _15_ percent, respectively.
<br>
>The dataset is available at this [link](https://www.kaggle.com/datasets/giannisgeorgiou/fish-species) 
<br>

# Analysis
All of the _analysis_ and _trainings_ can be seen in [**Fish-Classification.ipynb**](https://github.com/Nurkaiyr/fish-classification/blob/master/Fish-Classification.ipynb) file.

In this work, several models were used for classification task.
- EfficientNet
- MobileNetV2
- Custom Model

Due to resource constraints, models were trained only for 10 epochs.
> Please keep in mind that the demo app only includes **EfficientNet**.This is due to the limits of resources. For example, the custom model's file size was 300 MB.

# EfficientNet
The accuracy on the validation was 0.98
![EfficientNet model accuracy plot](https://github.com/Nurkaiyr/fish-classification/blob/master/Plots/EfficientNet-accuracy.png?raw=true)

# MobileNetV2
The accuracy on the validation was 0.93
![MobileNetV2 model accuracy plot](https://github.com/Nurkaiyr/fish-classification/blob/master/Plots/MobileNetV2-accuracy.png?raw=true)

# Custom model
Initially, the accuracy on the validation was 0.58
After that, the model was trained for more 10 epochs to see if we could get better results.
Then, the accuracy on the validation increased to 0.86
![Custom model accuracy plot](https://github.com/Nurkaiyr/fish-classification/blob/master/Plots/CustomModel-accuracy.png?raw=true)