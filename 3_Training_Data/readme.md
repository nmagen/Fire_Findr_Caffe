Building the Training Data Set
======

### How to build the data set

I will use flickr as the sorce of my images. The images that i am downlaoding were realased into the public domain under the crative commons lickes (more info [here](https://www.flickr.com/creativecommons/)). Downlaoding images with a given "tag" is fairly straight forward with the pyhton program in this folder (see [here](/flickr_download.py)). The chalanging part is determing how what images to download in order to build an effective training set for our task.


### Discussion: building a good training set.

To under stand what makes a "good" training set we need to think more about what we are actually trying to do. 

Fundamentially we are try to detect things that are on fire that should not be on file. As humans we ahve a pritty good concept of what should and shold not be on fire. This understanding is derived from our life experinces. Building this traning set is our way of letting the algorithm experence things.

Consistant with this:

--

**for an image with visable flams the alg need to understand that the object on fire is only important sometimes.**

For example houres and cars should never be on fire but but matches and lantern both should be on fire.

I incoperated this into my 


---

**The algorithm needs to understand the importance of smoke.**

For example black smoke is likely form a fire but wite "smoke" is likely just a cloud.

This disctincion is further complicated in images where there are no visable flams. in such a case it would be impossible to udnersntant if the sorce of the flams is of concer.

---

(3) fire fighters and fire trucks (and different countrys)




---
Additionally, in an immage with both visible flams the alg need to also 

Images where

 but white clounds




(4) fire in the past tense...



by disecting how humans have come to udnerstand what should and shold not be on fire we can begin ot make the traning data inorder to show the alg how to do it. 









