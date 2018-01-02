from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.layers import Input,Dense,Dropout
from keras.applications.vgg16 import preprocess_input
import cv2
import numpy as np
from keras.layers import Convolution2D, Activation, Flatten, MaxPooling2D
from keras.models import Model
from keras.applications.vgg16 import preprocess_input
import h5py
import numpy as np  

n_output = 5 # 输出的具体参数个数,xmin, ymin, xmax, ymax, ten/T

# base_model = VGG19(weights='imagenet')
base_model = VGG16(weights='imagenet', include_top=False)
model = Model(inputs=base_model.input, outputs=base_model.get_layer('block4_pool').output)
width = 224
img_path = 'sop30.jpg'
testimg = cv2.resize(cv2.imread(img_path), (width, width))
# cv2.imshow("IMG", testimg)
# cv2.waitKey(0)
# img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(testimg)# (224,224,3)
# print("1")
# print(x.shape)
x = np.expand_dims(x, axis=0)# (1, 224, 224, 3)
# print("2")
# print(x.shape)
x = preprocess_input(x)# (1, 224, 224, 3) first pic of many
# print("3")
# print(x.shape)
#features = model.predict(x)

# build model
# basic_model = VGG16(weights='imagenet')
# model = Model(inputs=base_model.input, outputs=base_model.get_layer('block4_pool').output)
# model.add(MaxPooling2D(2,2),strides=(2,2))
features = model.predict(x)# (1, 14, 14, 512)
# print(features.shape)

import xmlParse
y = xmlParse.getOutput("sop30.xml")
print(y)

# training model
inputs = Input(features.shape[1:])
X = inputs
X = Dropout(0.5)(X)
X = Dense(n_output, activation='softmax')(X)
model = Model(inputs, X)
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
h = model.fit(features, y, batch_size=1, epochs=1, validation_split=0.1)



'''
model.add(Convolution2D(num_filters, pool_size)
model.add(Flatten())
model.add(Activation('softmax'))
'''