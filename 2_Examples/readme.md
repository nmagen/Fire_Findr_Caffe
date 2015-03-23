Examples
===

### ILSVRC12 Example

The first example involves the network architecture from Krizhevsky et el submitted to Advances in Neural Information Processing Systems (NIPS) 2012 (ILSVRC12). The original paper is avablable [here](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks).

The use of this example is that guids one in:

* Reproducing their results from ILSVRC12 on the asdf data set.

* Incorporating your own images to make a classifier specific to your own task.

I will go over the specifics in how this is done to fill in the instrucitons given [here](http://caffe.berkeleyvision.org/gathered/examples/imagenet.html).


**reproducing ILSVRC12**

First download the auxiliary files ```train.txt``` and ```val.txt ``` by running.

```
./get_ilsvrc_aux.sh
```

Register with NIPS and download the images from [here](google.com). Read the data into leveldb files that will be used by caffe. To do this the authors have included a the script ```create_imagenet.sh```. You will need to modify ```RESIZE=false``` to ```RESIZE=true```. Assuming you have the data in ```${caffe_root}/data/ilsvrc12``` you can run.

```
./examples/imagenet/create_imagenet.sh
```

This should create two leveldb files ```ilsvrc12_val_leveldb``` and ```ilsvrc12_val_leveldb```. Create the training set image mean file by running.

```
asdf
```

The network definition is in ```${caffe_root}/models/bvlc_reference_caffenet/train_val.prototxt``` prototxt is the google protocol buffer file format (more info [here]()) (it;s similar to the json format). This file 


include { phase: TRAIN } or include { phase: TEST } 

this file also contain the various learning rates and the decay function....

in addition this file specifies the location of the mean pixel density file and trinan lmdv and val lmdb. 

Finally ```solver.partotxt``` contains information about the optimization method to be used and points to the ```train_val.partotxt``` file. Finally we can train by running.

```
./build/tools/caffe train --solver=models/bvlc_reference_caffenet/solver.prototxt
```

This will run and generate 

Additionally, it will generate a series of checkpoint files which contain the model weights and momentum. Having the checkpoint files allows one to restart at that point in the optimisation if the process gets interrupted (for example if you get kicked off your spot instance). The command to restart a computation is.

```
./build/tools/caffe train --solver=models/bvlc_reference_caffenet/solver.prototxt --snapshot=models/bvlc_reference_caffenet/caffenet_train_10000.solverstate
```

**incorporating your own images**

Setting up it fairly similar to the above with the notable exceptions

* generating the lmdb file

* if you have a different number of output layers

to generate the mdb file you will need to actually understand the script and make some modifications to it....

for changing the number of nodes on the last layer of the neural net. 


**classifying images**

Once you have generated your ```.caffemodel``` file form the above you can classify new unseen images. One of the easiest ways  to do this is by making use the caffe python model. The authors provide a ipython notebook on this. I decided to adapt this into a python program with the added functionality of printing the predicted class name instead just the class number. Take a look at it [here](/class.py)

For example this image:

![jpg](https://raw.githubusercontent.com/JBed/Fire_Findr/master/2_Examples/cat.jpg)

is correctly classifyed as:

```
predicted class: 281
```

### Flickr Style Example

This examples illustrates how caffe can be used to do Transfer Learning (TL). TL is a way to make use of a network trained for one purpose in a different task. The advantage of this is mostly with regards to computational efficiency. I will talk more about the pros and cons of TL in section 3.


here what we do is...




### R-CNN detector Example

R-CNN is a state-of-the-art detector that classifies region proposals by a finetuned Caffe model. For the full details of the R-CNN system and model, refer to its project site and the paper:


![jpg](https://raw.githubusercontent.com/JBed/Fire_Findr/master/2_Examples/fish-bike.jpg)


and detected at 

![jpg](https://raw.githubusercontent.com/JBed/Fire_Findr/master/2_Examples/fish-bike-detected.jpg)

and we're good.

