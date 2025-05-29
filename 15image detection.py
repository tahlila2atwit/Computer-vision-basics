#import 

import os
import numpy as np
from sklearn import svm 
from skimage.io import imread
from skimage.transform import resize

# load all pza images

bp = r"C:\Users\lilha\Desktop\CommaPrep"
categories = ['pizza', 'hamburger']

data = [] # empty - image info
labels = [] # p or b goes here

for cat in categories: # goes thru every image in the folder
    
    folder = os.path.join(bp,cat) #build the full file name path

    for file in os.listdir(folder): # for every image in that folder
        try:
            img_path = os.path.join(folder,file) #get full file path
            img = imread(img_path) #read image
            re = resize(img,(100,100)) #resize it
            data.append(re.flatten())# flatten and save it
            labels.append(cat) #save wether its p or b

        except:
            print(f"skipped {file}")




# after images are collected - train

# take labels and turn them into numbers 1 & 0
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
labels = le.fit_transform(labels)


# split data into 2 chunks
# learn from train, test from test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data,labels, test_size= .2)


# create the model - teach it using the training
# images and labels
from sklearn import svm
model = svm.SVC(kernel='linear')
model.fit(X_train, y_train)

# guess whats in the test images
# 1 or 0 - p or b
preds = model.predict(X_test)


# compare models guesses (preds) to real anwrs (y_test)
import matplotlib.pyplot as plt  # Import matplotlib for plotting
from sklearn.metrics import accuracy_score
print("accuracy:", accuracy_score(y_test,preds))



# Interactive training loop
print("\nStarting interactive training session...")
print("Help improve the model by correcting its mistakes!")

def on_click(event):
    global X_train, y_train, preds
    
    if event.inaxes is not None:
        # Get button clicked
        if event.ydata < 50:  # Bottom buttons area
            if event.xdata < fig.get_size_inches()[0]*fig.dpi/2:
                user_input = 'b'  # Left button - burger
            else:
                user_input = 'p'  # Right button - pizza
                
            # If model was wrong and user provided correction
            if user_input != predicted_label:
                # Add this example to training data
                X_train = np.vstack((X_train, X_test[idx]))
                y_train = np.append(y_train, le.transform([user_input]))
                
                # Retrain model with new data
                print("Retraining model with new example...")
                model.fit(X_train, y_train)
                
                # Update predictions
                preds = model.predict(X_test)
                print("New accuracy:", accuracy_score(y_test, preds))
            
            plt.close()

while True:
    # Get a random test image
    idx = np.random.randint(0, len(X_test))
    img_data = X_test[idx].reshape(100, 100, 3)
    true_label = le.inverse_transform([y_test[idx]])[0]
    predicted_label = le.inverse_transform([preds[idx]])[0]

    # Create figure and display image
    fig, ax = plt.subplots(figsize=(6, 7))
    ax.imshow(img_data)
    ax.set_title(f"Model predicts: {predicted_label}")
    ax.axis('off')
    
    # Add buttons at bottom
    burger_btn = plt.axes([0.2, 0.05, 0.2, 0.075])
    pizza_btn = plt.axes([0.6, 0.05, 0.2, 0.075])
    plt.text(0.3, 0.0625, 'Burger', ha='center', va='center')
    plt.text(0.7, 0.0625, 'Pizza', ha='center', va='center')
    
    # Connect click event
    fig.canvas.mpl_connect('button_press_event', on_click)
    
    plt.show()
    
    # Check if window was closed
    if not plt.get_fignums():
        break

print("\nInteractive training session ended.")
