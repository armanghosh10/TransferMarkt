import tensorflow as tf
from tensorflow import keras 

#Defining the model architecture
model = keras.Sequential([
    keras.layers.Dense(256, activation='relu', input_shape=(16,)),  
    keras.layers.Dense(32, activation='relu'), 
    keras.layers.Dense(1, activation='linear') 
])
model.compile(optimizer='adam', loss='mean_squared_error')  

#Training the model on the training data
model.fit(x_train, y_train, epochs=50, batch_size=32, validation_split=0.2)

model.summary()
