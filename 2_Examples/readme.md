Examples
===

### ILSVRC12 Example


The frist example involveds the network arcitexture from Krizhevsky et el submitted to Advances in Neural Information Processing Systems (NIPS) 2012 (ILSVRC12). The original paper is avablable [here](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks).

The use of this example is that guids one in:

* Reporduceing their resutles from ILSVRC12 on the asdf data set.

* Incoperateing your own images to make a classifyer specif to your own task.

I will go over the specifics in how this is done to fill in the instrucitons give [here](http://caffe.berkeleyvision.org/gathered/examples/imagenet.html).


**reporduceing ILSVRC12**



Now resister wiht NIPS and download the images from [here](google.com). Read the data into leveldb files that will be used by caffe. To do this the authors have included a the script ```create_imagenet.sh```. Assuming you have the data in ```${caffe_root}/data/ilsvrc12``` you can run.

```
./examples/imagenet/create_imagenet.sh
```



**incoverating your own images**

get your own images

then move some shit arround....




**classifying images**


### flickr style example

this examples illustrates the concet of transfer learning. TL is a way to use 

I will talk more about hte pros/ and cons of TL in seciton 3






