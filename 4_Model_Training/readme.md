Training the Model
=====

### How I trained my model

**Data Preparation**

The data was prepared as described in the ILSVRC12 Example in my 2_Examples folder. in total i used 50K images (split evenly positive and negative) in my training set and 1K in my testing set.


**Network Overview**

As described in the ImageNet [paper](https://github.com/JBed/Fire_Findr/blob/master/4_Model_Training/imagenet.pdf):

> the net contains eight layers with weights; the first five are convolutional and the remaining three are fully-connected. The output of the last fully-connected layer is fed to a 1000-way softmax which produces a distribution over the 1000 class labels. Our network maximizes the multinomial logistic regression objective, which is equivalent to maximizing the average across training cases of the log-probability of the correct label under the prediction distribution.

Since we only have two class labels we will need to modify the `train_val.prototxt` file so that the last fully-connected layer is feeds to a 2-way softmax. I will use stochastic gradient descent to optimise. I will run for 10K iterations


### Results

running took about 16hrs running on the K520 GPU. The last three lines of the system standard output is:

```
Iteration 10000, loss = 3.12675
Iteration 10000, Testing net (#0)
Test net output: accuracy = 0.3835
```


### Analysis of errors

Due to the time constraints I was not able to go over every misclassified test image. From the few misclassified examples I did look I have concluded:

---

**Detecting Multiple objects in a single image is important**

The detection of unwanted fire depends critically on the interaction of multiple objects. In the case of visible fire the model needs to see that something is "burning" and at least partially identify this object. 

for example this image:

![jpg](https://raw.githubusercontent.com/JBed/Fire_Findr/master/4_Model_Training/pot_fire.jpg)

was classified as on fire. What I think happened here is that the model does not understand two things.

1. there is a pot present in this photo 

2. that the significance of a pot above fire is that the fire is useful and not unwanted.

This issue could be remedied by including more image of fire being used in the context of cooking.

I also noticed this photo 

![jpg](https://raw.githubusercontent.com/JBed/Fire_Findr/master/4_Model_Training/pride_fire.jpg)

was classified as fire. which is likely the result of the model over weighting the importance of firetrucks. the model should have understood that fire trucks are not, on their own, importance. This issue could be remedied by including image of firetrucks in parades in the negative training examples.

---

**Knowing which information to ignore is difficult**

Many of the images (of the ones I actually looked at) in the training set were quite busy. Humans are quite good at distinguishing different object in a single image but CNNs are not. For example here:

![jpg](https://raw.githubusercontent.com/JBed/Fire_Findr/master/4_Model_Training/busy.jpg)

was classified as on not fire. What I think happened here is that the busyness of the image caused problems for the classifier. Detecting multiple objects in a single image is known to be very difficult (see [here](http://karpathy.github.io/2014/09/02/what-i-learned-from-competing-against-a-convnet-on-imagenet/)). I'm not sure that adding more training example would necessarily remedy this issue.

---

**Ambiguous Images** 

I also found this image listed as fire.

![jpg](https://raw.githubusercontent.com/JBed/Fire_Findr/master/4_Model_Training/ambiguous.jpg)

I think that this image is interesting because it illustrates a case where it is really not clear to even a human what is going on. The building in the background does not appear to be damaged by fire (it;s possible that this was a false alarme). 

I bring this up because it really is not clear what is going on in this photo. We see people standing around and hoses on the ground but it;s not clear is there is an active fire. This photo represent difficulties in accurately labeling our training set. 

Similar to the issue discussed above with the firetruck in a parade we need to make sure to find instances of firefighters at public events and include them in the training negative set.


---

### Conclusion

From the analysis above some modifications can be made to by training data set and the CNN re-trained. this iterative procedure will undouble improve performance. Unfortunately, there exist some aspect that will not be made better by including more (or more informative) image in the training set such as detecting multiple objects. 



