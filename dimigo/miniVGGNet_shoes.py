from imutils import paths
from aspectawarepreprocessor import AspectAwarePreprocessor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np

imagePaths = list(paths.list_images("./shoes"))

data = []
labels = []

aap = AspectAwarePreprocessor(100, 100)

#get label and data
# data -> numpy array(64, 64, 3) label -> string
for imagePath in imagePaths:
    print(imagePath)
    image = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
    image_s = aap.preprocess(image)
    data.append(image_s)
    label = imagePath.split(os.path.sep)[-2]
    labels.append(label)
    #rint(label)
    
#list nariable - > numpy array
data = np.array(data)
print(data.shape)
labels = np.array(labels)

# nomalizing
data = data.astype("float")/255

#train data test data split
(trainX, testX, trainY, testY) = train_test_split(data, labels, test_size=0.25, random_state=42, shuffle=True)
#print(trainX.shape)

lb = LabelBinarizer()
trainY = lb.fit_transform(trainY)
testY = lb.fit_transform(testY)

#opt = SGD(lr=0.01, decay =0.01/40, momentum=0.9, nesterov=True)
opt = SGD(lr=0.01)

aug = ImageDataGenerator(rotation_range=30, width_shift_range=0.1,
	height_shift_range=0.1, shear_range=0.2, zoom_range=0.2,
	horizontal_flip=True, fill_mode="nearest")


model = Sequential()
# 1 CONV
model.add(Conv2D(32, (3,3), padding="same", input_shape=(100, 100, 1)))
model.add(Activation("relu"))
model.add(BatchNormalization(axis=-1))
model.add(Conv2D(32, (3,3), padding="same"))
model.add(Activation("relu"))
model.add(BatchNormalization(axis=-1))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

# 2 CONV
model.add(Conv2D(64, (3,3), padding="same"))
model.add(Activation("relu"))
model.add(BatchNormalization(axis=-1))
model.add(Conv2D(64, (3,3), padding="same"))
model.add(Activation("relu"))
model.add(BatchNormalization(axis=-1))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

# FC
model.add(Flatten())
model.add(Dense(512))
model.add(Activation("relu"))
model.add(BatchNormalization())
model.add(Dropout(0.5))

# Class
model.add(Dense(5))
model.add(Activation("softmax"))
'''
# model architechture

model = Sequential()

# Input layer 1

model.add(Conv2D(128, kernel_size=(7, 7),
                 activation='relu',
                 input_shape=(100,100, 1)))
model.add(MaxPooling2D(pool_size=(3,3)))

# layer 2
model.add(Conv2D(256, (7, 7), activation='relu'))

model.add(MaxPooling2D(pool_size=(3, 3)))

model.add(Dropout(0.25))

# flattening layer
model.add(Flatten())

# Dense layer
model.add(Dense(512, activation='relu'))

model.add(Dropout(0.5))

# Dense output layer
model.add(Dense(5, activation='softmax'))

'''
# Model compile 
model.compile(loss="categorical_crossentropy",optimizer=opt, metrics=["accuracy"])

'''
H = model.fit_generator(aug.flow(trainX, trainY, batch_size=32),
	validation_data=(testX, testY), steps_per_epoch=len(trainX) // 32,
	epochs=30, verbose=1)
'''

H = model.fit(trainX, trainY, validation_data=(testX, testY),
              batch_size=32, epochs=100, verbose=1)


model.save("vgg_shoes.h5")

plt.style.use("ggplot")
plt.figure()
plt.plot(np.arange(0, 100), H.history["loss"], label="train_loss")
plt.plot(np.arange(0, 100), H.history["val_loss"], label="val_loss")
plt.plot(np.arange(0, 100), H.history["accuracy"], label="train_acc")
plt.plot(np.arange(0, 100), H.history["val_accuracy"], label="val_acc")
plt.title("Training Loss and Accuracy on CIFAR-10")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend()
plt.savefig("vgg.png")
plt.show()
