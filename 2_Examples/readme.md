Examples
===

### ILSVRC12 Example

The frist example involveds the network arcitexture from Krizhevsky et el submitted to Advances in Neural Information Processing Systems (NIPS) 2012 (ILSVRC12). The original paper is avablable [here](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks).

The use of this example is that guids one in:

* Reporduceing their resutles from ILSVRC12 on the asdf data set.

* Incoperateing your own images to make a classifyer specif to your own task.

I will go over the specifics in how this is done to fill in the instrucitons given [here](http://caffe.berkeleyvision.org/gathered/examples/imagenet.html).


**reporduceing ILSVRC12**

First download the auxileray files ```train.txt``` and ```val.txt ``` by running.

```
./get_ilsvrc_aux.sh
```

Now resister wiht NIPS and download the images from [here](google.com). Read the data into leveldb files that will be used by caffe. To do this the authors have included a the script ```create_imagenet.sh```. You will need to modify ```RESIZE=false``` to ```RESIZE=true```. Assuming you have the data in ```${caffe_root}/data/ilsvrc12``` you can run.

```
./examples/imagenet/create_imagenet.sh
```

This should creat two leveldb files ```ilsvrc12_val_leveldb``` and ```ilsvrc12_val_leveldb```. Creat the traning set image mean file by running.

```
asdf
```

The network definition is in ```${caffe_root}/models/bvlc_reference_caffenet/train_val.prototxt``` prototxt is the google protocall buffer file format (more info [here]()) (it;s similar to the json format). This file 

include { phase: TRAIN } or include { phase: TEST } 

this file also contain the various learning rages and the decay fucntion....

in addition this file specifyes the locaiton of the mean pixile density file and trinan lmdv and val lmdb. 

Finally ```solver.partotxt``` contains information about the optimisaiton method to be used and points to the ```train_val.partotxt``` file. Finally we can train by running.

```
./build/tools/caffe train --solver=models/bvlc_reference_caffenet/solver.prototxt
```

This will run and generate 

Additionally, it will genrate a serius of checkpoint files which contain the model weights and momentum. Haveing the check point files allows one to resatart at that point in the optimisation if the process gets interupted (for example if you get kicked off your spot instance).


**incoverating your own images**

get your own images

then move some shit arround....




**classifying images**


### flickr style example

this examples illustrates the concet of transfer learning. TL is a way to use 

I will talk more about hte pros/ and cons of TL in seciton 3





































