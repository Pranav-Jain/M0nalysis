from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
import csv
import numpy as np
import matplotlib.pyplot as plt
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import normalize
from sklearn.ensemble import RandomForestRegressor


def rfr(X_train, X_test, y_train, y_test):
    clf = RandomForestRegressor(min_samples_split=2, min_samples_leaf=1,n_jobs=3)
    clf.fit(X_train, y_train)

    # print("Random Forest Model Trained")

    # pred = clf.predict(X_test)
    # print(classification_report(y_test, pred))
    print(clf.feature_importances_)
    print("Accuracy : ")
    print(clf.score(X_test, y_test))
    # pickle.dump(clf, open('rf.sav', 'wb+'))
    # print("Model Saved")


if __name__ == '__main__':

    names = ['male','female','Uttarakhand','Rajasthan','UP','Bihar','Assam','Jharkhand','Orissa','Chhattisgarh','MP']

    for j in names:
        data = []
        labels= []

        with open('data/'+j+'.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if(line_count!=0):
                    # string = row[1]
                    # print(len(row))
                    d=[]
                    # print(row)
                    for i in range(len(row)):
                        if(i!=0):
                            if(row[i]=='' or row[i]==' '):
                                d.append(0)
                            else:
                                # print(float(row[i]))
                                d.append(float(row[i]))
                    data.append(d)
                    if(row[0]=='' or row[0]==' '):
                        labels.append(50)
                    else:
                        labels.append(int(float(row[0])))
                line_count+=1

        X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2)
        # print("Data Split Done....\n")

        X_train = normalize(X_train)
        X_test = normalize(X_test)

        # np.save('X_train', X_train)
        # np.save('X_test', X_test)
        # np.save('y_train', y_train)
        # np.save('y_test', y_test)


        print("\n"+j)
        rfr(X_train, X_test, y_train, y_test)


