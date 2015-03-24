Training the Model
=====

### How I trained my model

**Data Preparation**

The data was prepared as described in the ILSVRC12 Example in my 2_Examples folder.


**Network overview**

As described in the ImageNet [paper](https://github.com/JBed/Fire_Findr/blob/master/4_Model_Training/imagenet.pdf):

> the net contains eight layers with weights; the first five are convolutional and the remaining three are fully-connected. The output of the last fully-connected layer is fed to a 1000-way softmax which produces a distribution over the 1000 class labels. Our network maximizes the multinomial logistic regression objective, which is equivalent to maximizing the average across training cases of the log-probability of the correct label under the prediction distribution.

Since we only have two class labels we will need to modify the `train_val.prototxt` file so that the last fully-connected layer is feeds to a 2-way softmax. I will use stochastic gradient descent to optimise.



### Results




### Analysis of errors

Due to the time constraints I was not able to go over every misclassified example. From the few misclassified examples I did look I have concluded:


---

**Detecting Multiple objects in a single image is difficult**

The detection of unwanted fire depends critically on the interaction of multiple objects. In the case of visible fire the model needs to see that something is "burning" and at least partially identify this object. 

for example this image:

![jpg](https://raw.githubusercontent.com/JBed/Fire_Findr/master/4_Model_Training/pot_fire.jpg)

was classified as on fire. What I think happened here is that the model does not understand two things.

1. there is also a pot present in this photo 

2. that the significance of this pot is that it is meant for cooking.

I also noticed this photo 

![jpg](https://raw.githubusercontent.com/JBed/Fire_Findr/master/4_Model_Training/pride_fire.jpg)

was classified as fire. which is likely the result of the model over weighting the importance of firetrucks. the model should have understood that firetrucks are related to fire but not caused by fire.

---

**Knowing which information to ignore is difficult**

many of the images (of the ones I actually looked at) in the training set were quite busy.

for example here:

![jpg](https://raw.githubusercontent.com/JBed/Fire_Findr/master/4_Model_Training/busy.jpg)

was classified as on not fire. What I think happened here is that the 


---

**Ambiguous Images** 

I also found this image listed as fire.

![jpg](https://raw.githubusercontent.com/JBed/Fire_Findr/master/4_Model_Training/ambiguous.jpg)

I bring this up because it really is not clear what is going on in this photo. We see people standing around and hoses on the ground but it;s not clear is there is an active fire. This photo represent difficulties in accurately labeling our training set. 

---








