import pandas
import re
from sklearn.tree import DecisionTreeClassifier

#Loading titanic train dataset
dataset = pandas.read_csv('titanic_train.csv', engine='python')

#Filling missing age with mean value
dataset.fillna(dataset['Age'].mean(), inplace=True)
#Replacing Sex property with 0 - male and 1 - female
dataset['SexN'] = dataset['Sex'].replace({'male': 0, 'female': 1})
dataset['Family'] = dataset['SibSp'] + dataset['Parch']
#Creating column PortN and mapping it with numbers 0 - C, Q - 1, S - 2
dataset['PortN'] = dataset['Embarked'].replace({'C': 0, 'Q': 1, 'S': 2})
#Filling missing Port properties with mean value
dataset.fillna(dataset['PortN'].mean(), inplace=True)

#Doing same things for train test
testData = pandas.read_csv('titanic_test.csv', engine='python')
testData.fillna(testData['Age'].mean(), inplace=True)
testData['SexN'] = testData['Sex'].replace({'male': 0, 'female': 1})
testData['Family'] = testData['SibSp'] + testData['Parch']
testData['PortN'] = testData['Embarked'].replace({'C': 0, 'Q': 1, 'S': 2})
testData.fillna(testData['PortN'].mean(), inplace=True)

#creating decision tree model
model = DecisionTreeClassifier(max_depth=7)

#feeding train data to model
model.fit(trainData[['Pclass', 'Age', 'Parch', 'Fare', 'SexN', 'Family', 'PortN']], trainData['Survived'])
#creating predictions from test data
predictions = model.predict(testData[['Pclass', 'Age', 'Parch', 'Fare', 'SexN', 'Family', 'PortN']])

#Creating dataframe from test data passenger ids and our predictions
submission = pandas.DataFrame({'PassengerId': testData['PassengerId'], 'Survived': predictions})
#writing predictions to csv file
submission.to_csv("submission.csv", index=False)
