Building the Training Data Set
======

### How to build the data set

I will use flickr as the sorce of my images. The images that i am downlaoding were realased into the public domain under the crative commons lickes (more info [here](https://www.flickr.com/creativecommons/)). Downlaoding images with a given "tag" is fairly straight forward with the pyhton program in this folder (see [here](/flickr_download.py)). The chalanging part is determing how what images to download in order to build an effective training set for our task.


### Discussion: building a good training set.

To under stand what makes a "good" training set we need to think more about what we are actually trying to do. 

Fundamentially we are try to detect things that are on fire that should not be on file. As humans we ahve a pritty good concept of what should and shold not be on fire. This understanding is derived from our life experinces. Building this traning set is our way of letting the algorithm experence things.

Consistant with:

---

**For an image with visable flams the algorithm need to understand that the object on fire is only important sometimes.**

For example houses and cars should never be on fire but matches, lanterns, candels both should be on fire. Simply put object that is "burning" need to be recignized. To acocmplish this I incoperated these words into my asdf:

* positive: house on fire, car on fire, wildfire, brush fire

* negative: match on fire, lantern, candel.

---

**The algorithm needs to understand the importance of smoke.**

For example black smoke is likely form a fire but wite "smoke" is likely just a cloud. This disctincion is further complicated in images where there are no visable flams. in such a case it would be impossible to udnersntant if the sorce of the flams is of concer. I incoperated this into my traning set by using:

* positive: black smoke, fire smoke, 

* negative: couds, white cloud blue sky

Distinguishing smoke from a fire from a normal clound formation can be quire difficult as is shown in the image below.

![jpg](asdf)

---

**The algorithm needs to damage that was uniquly caused by fire**

For example a fire can damage a house but so also can earthquacks and tornados. While fire will likely occure after an earthquack or tornado...

for example distinguishing these two images 



* positive: fire damage

* negative: earthquack damage, tornado damage


---


### Conclusions

by disecting how humans have come to udnerstand what should and shold not be on fire we can begin ot make the traning data inorder to show the alg how to do it. 

hopefully this discuion has shead some light... haha








