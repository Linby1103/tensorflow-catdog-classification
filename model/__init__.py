# from .LeNet5 import inference
# from .LeNet5 import losses as Lloss
# from .LeNet5 import trainning as Ltrain
# from .LeNet5 import evaluation as L_eval
# from .LeNet5 import inference
import numpy as np
import os
import cv2
# from .AlexNet import AlexNet
# from .AlexNet import losses as Aloss
# from .AlexNet import trainning as Atrain
# from .AlexNet import evaluation as A_eval
# def load_annotations(annot_path):
#     with open(annot_path, 'r') as f:
#         txt = f.readlines()
#         annotations = [line.strip() for line in txt if len(line.strip().split()[1:]) != 0]
#         print("annotations:\n",annotations)
#     np.random.shuffle(annotations)
#     print("shuffle annotations:\n", annotations)
#     return annotations
# # annot_path="D:/install/yolov3-tensorflow/tensorflow-yolov3/data/dataset/voc_train.txt"
# # annotations=load_annotations(annot_path)
#
#
# def parse_annotation( annotation):
#     line = annotation
#     image_path = line[0]
#     if not os.path.exists(image_path):
#         raise KeyError("%s does not exist ... " % image_path)
#     image = np.array(cv2.imread(image_path))
#     bboxes = np.array([list(map(int, box.split(','))) for box in line[1:]])
#     print("bboes:\n",bboxes)
#
#
# parse_annotation( annotations)