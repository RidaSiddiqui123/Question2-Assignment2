#-------------------------------------------------------------------------
# AUTHOR: Rida Siddiqui
# FILENAME: decision_tree2.py
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2 - Question 2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:
    dbTraining = []
    X = []
    Y = []

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    # so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    # X =
    Age = {
        "Young": 1,
        "Presbyopic": 2,
        "Prepresbyopic": 3
    }
    Spectacle_Prescription = {
        "Myope": 1,
        "Hypermetrope": 2
    }
    Astigmatism = {
        "Yes": 1,
        "No": 2
    }
    Tear_Production_Rate = {
        "Normal": 1,
        "Reduced": 2
    }

    for row in dbTraining:
        X.append([Age[row[0]], Spectacle_Prescription[row[1]], Astigmatism[row[2]], Tear_Production_Rate[row[3]]])

    #transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> addd your Python code here
    # Y =
    label = {
        "Yes": 1,
        "No": 2
    }
    for row in dbTraining:
        Y.append(label[row[4]])

    #loop your training and test tasks 10 times here
    Accuracy = []

    for i in range (10):
       TP = 0
       TN = 0
       FP = 0
       FN = 0
       #fitting the decision tree to the data setting max_depth=3
       clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
       clf = clf.fit(X, Y)

       #read the test data and add this data to dbTest
       #--> add your Python code here
       # dbTest =
       dbTest = []
       with open('contact_lens_test.csv', 'r') as csvfile:
           reader = csv.reader(csvfile)
           for i, row in enumerate(reader):
               if i > 0:  # skipping the header
                   dbTest.append(row)

       testData = []
       testClass = []
       i = 0

       for row in dbTest:
           testData.append([Age[row[0]], Spectacle_Prescription[row[1]], Astigmatism[row[2]], Tear_Production_Rate[row[3]]])
           testClass.append(label[row[4]])
           #print("testData ", testData)
           #transform the features of the test instances to numbers following the same strategy done during training,
           #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
           #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
           #--> add your Python code here


           #print("test data ", testData[i])
           class_predicted = clf.predict([testData[i]])[0]
           #print("class_predicted", class_predicted)

           #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
           #--> add your Python code here

           if class_predicted == 1 and testClass[i] == 2:
             FP+=1
           elif class_predicted == 2 and testClass[i] == 1:
             FN+=1
           elif class_predicted == 2 and testClass[i] == 2:
             TN+=1
           else:
             TP+=1
           i += 1
       Accuracy.append((TP + TN)/(TP + TN + FP + FN))

        #find the lowest accuracy of this model during the 10 runs (training and test set)
        #--> add your Python code here

    #print the lowest accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here
    print("Final accuracy when training on " + ds + ": ", min(Accuracy))




