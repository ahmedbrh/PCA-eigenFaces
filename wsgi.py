from flask import Flask
from flask import request
from sklearn.datasets import fetch_lfw_people
from sklearn.model_selection import train_test_split
from flask import send_file
from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image 
import io
import pickle
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route("/getImage")
def hello_world():
    img = request.args.get('img', default = 0, type = int)
    people = fetch_lfw_people(min_faces_per_person = 70, resize = 0.4)
    X = people.data
    Y = people.target
    X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size = 0.25, random_state = 42)
    X = X_train
    imaj=np.array(X[img],dtype=np.int64).reshape((50,37))
    img = Image.fromarray(imaj.astype(np.uint8))
    file_object = io.BytesIO()
    img.save(file_object, 'jpeg')
    file_object.seek(0)
    return send_file(file_object, mimetype='image/jpeg')

@app.route("/compressImage")
def hello_world2():
    img = request.args.get('img', default = 0, type = int)
    nbEig = request.args.get('nbEig', default = 0, type = int)
    eigVecValue = pickle.load( open( "eigvector-value.pkl", "rb" ) )
    ui = [eigVecValue[i][0] for i in range(nbEig)]   
    people = fetch_lfw_people(min_faces_per_person = 70, resize = 0.4)
    X = people.data
    visageMoyen = np.zeros(50*37) 
    for image in X:
        visageMoyen = np.add(image,visageMoyen)
    visageMoyen = np.divide(visageMoyen,len(X))
    weights=np.dot(ui,X[img]-visageMoyen)
    yp = np.zeros((1850))
    for i in range(len(weights)):
        yp = np.add(yp,weights[i]*ui[i])
    yp+=visageMoyen
    imaj=np.array(yp,dtype=np.int64).reshape((50,37))
    img = Image.fromarray(imaj.astype(np.uint8))
    file_object = io.BytesIO()
    img.save(file_object, 'jpeg')
    file_object.seek(0)
    return send_file(file_object, mimetype='image/jpeg')
    
@app.route("/getUnseenImage")
def hello_world3():
    img = request.args.get('img', default = 0, type = int)
    people = fetch_lfw_people(min_faces_per_person = 70, resize = 0.4)
    X = people.data
    Y = people.target
    X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size = 0.25, random_state = 42)
    X = X_test
    imaj=np.array(X[img],dtype=np.int64).reshape((50,37))
    img = Image.fromarray(imaj.astype(np.uint8))
    file_object = io.BytesIO()
    img.save(file_object, 'jpeg')
    file_object.seek(0)
    return send_file(file_object, mimetype='image/jpeg')
@app.route("/getClass", methods=["GET"])
def hello_world4():
    img = request.args.get('img', default = 0, type = int)
    W = [] 
    with open('images weights.pkl', 'rb') as f:
        W = pickle.load(f)
    people = fetch_lfw_people(min_faces_per_person = 70, resize = 0.4)
    X = people.data
    Y = people.target
    X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size = 0.25, random_state = 42)
    X = X_train
    classId = KNN(img,10,W,y_train)
    names = people.target_names
    return str(classId)+" : "+names[classId]

def KNN(imgIndex,K,W,Y):
    tab=[]
    for i in range(len(W)):
        dist = ((W[imgIndex] -W[i])**2).mean(axis=None)
        tab.append({"dist":dist, "class":Y[i]})
    tab = sorted(tab,key=lambda x : x["dist"]) 
    compteurs=[0,0,0,0,0,0,0]
    for i in range(K):
        compteurs[tab[i]["class"]]+=1
    res=0
    biggest=-1111
    for i in range(len(compteurs)):
        if(compteurs[i]>biggest):
                biggest = compteurs[i]
                res=i
    print(compteurs)
    return res