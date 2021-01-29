# -*- coding: utf-8 -*-
# @Author: davidhansonc
# @Date:   2021-01-21 09:05:47
# @Last Modified by:   davidhansonc
# @Last Modified time: 2021-01-21 09:43:39
from imageai.Classification import ImageClassification
import os

execution_path=os.getcwd()

prediction = ImageClassification()
prediction.setModelTypeAsResNet50()
prediction.setModelPath(os.path.join(execution_path, "resnet50_imagenet_tf.2.0.h5"))
prediction.loadModel()

predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, \
        "house.jpg"), result_count=5 )
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)