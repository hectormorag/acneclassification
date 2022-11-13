# Acne Classification VGG16 

Solving the classification problem of identifying acne into four categories: healthy, mild, moderate and severe. Data augmentation and dropout used besides a standard VGG model. After validation, an accuracy of 90% is achieved. 

The first step was performing augmentation on the dataset provided: from 400 images for each category, randomly using zoom, rotations and flip functions, we extended the dataset to 2000 images for each class. The tools needed to do that are under augmentation.py; as an example refer to the images in the augmentation file. 

The second step was training the VGG16 model after the fine tuning. I used tensorboard to keep track of the performance of the model. The final results can be seen in the following plots: 

<p align="center">
  <img src="https://github.com/hectormorag/acneclassification/blob/main/ModelPerformance/EpochAcc.png?raw=true"/>
</p>

<p align="center">
  <img src="https://github.com/hectormorag/acneclassification/blob/main/ModelPerformance/EpochLoss.png?raw=true"/>
</p>

As we can see, the model is slightly overffited passing the three epochs, but it's still useful as prototype; I didn't train the model further, given that each epoch takes 50 minutes to traing. The confussion matrix of this model is presented in the following figure: 


<p align="center">
  <img src="https://github.com/hectormorag/acneclassification/blob/main/ModelPerformance/ConfussionMatrix.png"/>
</p>

As we can see, the model performs really well on the "Healthy" and "Severe" classes, with a bigger index error on "Moderate" and "Severe". Looking at some of the images in the test data, one would feel compelled to agree with the algorithm on how difficult it's do distinghuis between those two cases. 


