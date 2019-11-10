import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

datadir = "E:\\PetImages"
categories = ["Dog", "Cat"]

for category in categories:
  path = os.path.join(datadir, category)

  for img in os.listdir(path):
    img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
    plt.imshow(img_array, cmap = "gray")
    plt.show()
    break
  break

img_size = 70
new_array = cv2.resize(img_array, (img_size), (img_size))
plt.imshow(new_array, cmap="gray")
plt.show()

training_data = []


def create_training_data():
    for category in categories:
        path = os.path.join(datadir, category)
        class_num = categories.index(category)

    for img in os.listdir(path):
        try:

            img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
            new_array = cv2.resize(img_array, (img_size), (img_size))
            training_data.append([new_array, class_num])

        except Exception as e:
            pass


create_training_data()