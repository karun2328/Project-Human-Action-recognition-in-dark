import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
# load the saved modelpy
model = load_model('C:/Users/karun/OneDrive/Desktop/Project/CODE/model-bw')
# define the test data directory
test_dir = 'C:/Users/karun/OneDrive/Desktop/Project/CODE/images/test'
# create an instance of the ImageDataGenerator class
test_datagen = ImageDataGenerator(rescale = 1./255)
# create the test data generator
test_set = test_datagen.flow_from_directory(test_dir, target_size = (64, 64), batch_size = 32, class_mode = 'categorical')
# evaluate the model on the test data
accuracy = model.evaluate(test_set)[1]
print('Accuracy:', accuracy)
