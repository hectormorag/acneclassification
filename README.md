# Acne Classification VGG16 

Solving the classification problem of identifying acne into four categories: healthy, mild, moderate and severe. Data augmentation and dropout used besides a standard VGG model. After validation, an accuracy of 90% is achieved. 

The first step was performing augmentation on the dataset provided: from 400 images for each category, randomly using zoom, rotations and flip functions, we extended the dataset to 2000 images for each class. The tools needed to do that are under augmentation.py; as an example refer to the images in the augmentation file. 

The second step was training the VGG16 model after the fine tuning. I used tensorboard to keep track of the performance of the model. The final results can be seen in the following plots: 

<p align="center">
  <img src="https://github.com/hectormorag/acneclassification/blob/main/ModelPerformance/EpochAcc.png?raw=true"/>
</p>



![alt text](https://github.com/hectormorag/acneclassification/blob/main/ModelPerformance/EpochLoss.png?raw=true)


