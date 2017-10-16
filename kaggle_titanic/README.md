# Survival predictions for kaggle titanic survival competition

Titanic competition can be found on following link: [Kaggle titanic competition](https://www.kaggle.com/c/titanic)

## Data manipulation
Steps i have done to extract data from the kaggle train set:
 - Replaced Sex column with integer values
 - Filled missing Age values with Age mean values
 - Created Family column by adding SibSp and Parch columns
 - Created PortN column where i replaced Embarked column values with integer values

Further improvement
 - Extract title from the Name column
 - Replace Age not with general mean value but with mean value of gender and title

## Algorithms overview

### Decision tree
With this machine learning algorithm i have achieved score of 0.77033 which ranked me 5355 of 8500+ teams