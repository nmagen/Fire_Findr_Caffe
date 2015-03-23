
import numpy as np
import matplotlib.pyplot as plt

caffe_root = '/opt/caffe/'

import sys
sys.path.insert(0, caffe_root + 'python') #only necessary if you did not update your PYTHON_PATH

import caffe

# Set the right path to your model definition file, pretrained model weights,
# and the image you would like to classify.
MODEL_FILE = '/opt/caffe/models/bvlc_reference_caffenet/deploy.prototxt'
PRETRAINED = '/opt/caffe/models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel'
IMAGE_FILE = 'test1.jpg'


caffe.set_mode_gpu()
net = caffe.Classifier(MODEL_FILE, PRETRAINED,
                       mean=np.load(caffe_root + 'python/caffe/imagenet/ilsvrc_2012_mean.npy').mean(1).mean(1),
                       channel_swap=(2,1,0),
                       raw_scale=255,
                       image_dims=(256, 256))


input_image = caffe.io.load_image(IMAGE_FILE)

# predict takes any number of images, and formats them for the Caffe net automatically
prediction = net.predict([input_image])

print 'predicted class:', prediction[0].argmax()

#look in /opt/caffe/data/ilsvrc12/synset_words.txt for the meaning
#to update...

