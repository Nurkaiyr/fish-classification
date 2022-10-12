# 🐟 Fish Classification

> Demo: https://bit.ly/fish-classification

The dataset consists of _20 Mediterranean fish species_ with _2000_ images for per fish species.
Overall, _40 000_ images were produced. 

Following that, it was divided into training and testing sets with a proportion of _85_ and _15_ percent, respectively.
<br>
>Dataset is available at this [link](https://www.kaggle.com/datasets/giannisgeorgiou/fish-species) 
<br>

All _analysis_ and _trainings_ are able to view in [**Fish-Classification.ipynb**](https://github.com/Nurkaiyr/fish-classification/blob/master/Fish-Classification.ipynb) file.

In this work, several models were used for classification task.
- EfficientNet
- MobileNetV2
- Custom Model

Due to resource constraints model were trained only for 10 epochs.
> Note: only **EfficientNet** is on demo app. This is due to the limits of resources. For example, custom model's file size were 300 MB.

## EfficientNet
Accuracy on the validation was 0.98

## MobileNetV2
Accuracy on the validation was 0.93

## Custom model
Accuracy on the validation was 0.58

After that, model was trained for more 10 epochs to see if we could get better results.
Accuracy on the validation was 0.86