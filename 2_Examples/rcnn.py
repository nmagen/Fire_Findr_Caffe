
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

caffe_root = '/opt/caffe/'

import sys
sys.path.insert(0, caffe_root + 'python') #only necessary if you did not update your PYTHON_PATH

import caffe

MODEL_FILE = '/opt/caffe/models/bvlc_reference_caffenet/deploy.prototxt'
PRETRAINED = '/opt/caffe/models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel'

df = pd.read_hdf('_temp/det_output.h5', 'df')

with open('../data/ilsvrc12/det_synset_words.txt') as f:
    labels_df = pd.DataFrame([
        {
            'synset_id': l.strip().split(' ')[0],
            'name': ' '.join(l.strip().split(' ')[1:]).split(',')[0]
        }
        for l in f.readlines()
    ])

labels_df.sort('synset_id')
predictions_df = pd.DataFrame(np.vstack(df.prediction.values), columns=labels_df['name'])

net = caffe.rcnnClassifier(MODEL_FILE, PRETRAINED)

# Find, print, and display the top detections: person and bicycle.
i = predictions_df['person'].argmax()
j = predictions_df['bicycle'].argmax()

# Show top predictions for top detection.
f = pd.Series(df['prediction'].iloc[i], index=labels_df['name'])
print('Top detection:')
print(f.order(ascending=False)[:5])
print('')

# Show top predictions for second-best detection.
f = pd.Series(df['prediction'].iloc[j], index=labels_df['name'])
print('Second-best detection:')
print(f.order(ascending=False)[:5])

# Show top detection in red, second-best top detection in blue.
im = plt.imread('images/fish-bike.jpg')
currentAxis = plt.gca()

det = df.iloc[i]
coords = (det['xmin'], det['ymin']), det['xmax'] - det['xmin'], det['ymax'] - det['ymin']
currentAxis.add_patch(plt.Rectangle(*coords, fill=False, edgecolor='r', linewidth=5))

det = df.iloc[j]
coords = (det['xmin'], det['ymin']), det['xmax'] - det['xmin'], det['ymax'] - det['ymin']
currentAxis.add_patch(plt.Rectangle(*coords, fill=False, edgecolor='b', linewidth=5))
plt.imshow(im)


