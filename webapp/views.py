from django.shortcuts import render, redirect

from django.core.files.storage import FileSystemStorage

from django.http import HttpResponseRedirect
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
import json
from tensorflow import Graph
import numpy as np

img_height, img_width=200,200
with open('./models/imagenet_classes.json', 'r') as f:
    labelInfo=f.read()
labelInfo=json.loads(labelInfo)
model_graph = Graph()
with model_graph.as_default():
    gpuoptions = tf.compat.v1.GPUOptions(allow_growth=True)
    tf_session = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(gpu_options=gpuoptions))
    with tf_session.as_default():
        model = load_model("./models/Heritage1.h5")
# Create your views here.
def index(request):
    context = {'a' : 1}
    return render(request, 'index.html', context)



def predictImage(request):

    fileObj = request.FILES['filepath']
    fs = FileSystemStorage()
    filePathName = fs.save(fileObj.name, fileObj)
    filePathName = fs.url(filePathName)
    testimage='.'+filePathName
    img = image.load_img(testimage, target_size=(img_height, img_width))
    x = image.img_to_array(img)
    x=x/225
    x=x.reshape(1,img_height, img_width, 3)
    with model_graph.as_default():
        with tf_session.as_default():
            predi=model.predict(x)
    predictedLabel = labelInfo[str(np.argmax(predi[0]))]
    

    context = {'filePathName':filePathName, 'predictedLabel': predictedLabel}
    if predictedLabel=="psoraisis":
        return render(request, "test.html", context=None)
    # return render(request, 'index.html', context)

def testlabel(request):
    return render(request, "test.html", context=None)
