# Acne Classification VGG16 

Solving the classification problem of identifying acne into four categories: healthy, mild, moderate and severe. Data augmentation and dropout used besides a standard VGG model. After validation, an accuracy of 90% is achieved. 

The first step was performing augmentation on the dataset provided: from 400 images for each category, randomly using zoom, roations and flip functions, we extended the dataset to 2000 images for each class. The tools needed to do that are under augmentation.py; as an example refer to the following figure. 
