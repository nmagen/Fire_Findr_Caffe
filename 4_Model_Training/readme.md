Training the Model
=====

### How I trained my model

The data was prepared in the way described in...


**Loss fucntion**

A loss function specifies the goal of learning by mapping parameter settings (i.e., the current network weights) to a scalar value specifying the “badness” of these parameter settings. Hence, the goal of learning is to find a setting of the weights that minimizes the loss function.

**Solver**

to opt the loss fucntion I used SGD.


### Resultes

asdf


### Analysis of errors

Due to the time contrsins I was not able to go over every miss classifyed example. From the few missclassifyed examples I did look at and from review relavant literature I have concluded:

---

**detecting Multiple objects in a single immage is diffuclt**

The detection of unwanted fire depends critically on the interation of multiple objects. In the case of visable fire the model needs to see that somehting is "burning" and at least partially identiy this object. 


this is known to be diff....

---

**fine details are improtance**

In the case of just visable smoke the model needs to understand how the details of the smoke distinguish it from just a cloud


this is known to be diff...



---

**the big picture is important***

for distingusing fire damage from damage caused by earthquacks or tornados the model need to not focus on the specifiys of how things are lay (as this random)

insead needs to look at the big picture such as black-ness that is uniquly caused 


---


the chalange for our model is to excell at each of these tasks... whihc is difficult.



### conclusions

-> As mentioned the conclusiton of the building the training set... training is a process....


-> Even with mroe time to iterativly improve our training set (and therefor classifyer) there are still fundametal issure that remin. 



-> overall fire is multi facited in nature this muti-fasitiness make it;s detection difficult.

or soemthing like this...





