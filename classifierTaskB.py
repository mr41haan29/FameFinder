import pandas as pd
import sklearn.tree as skTree
import sklearn.model_selection as skModelSelection
import sklearn.metrics as metrics
import matplotlib.pyplot as plt
 

taskB = pd.read_csv("C:\\Users\Owner\Desktop\\taskB.csv")

features = ["battingR", "battingH",	"batting2B", "batting3B", "battingHR", "battingSO",	"pitchingWins",	"pitchingLosses", "pitchingHR", "pitchingSHO", "pitchingRunsAllowed", "fieldingPO", "fieldingAssists", "fieldingZR"]
classifier = ["class"]

xtrain, xtest, ytrain, ytest = skModelSelection.train_test_split(taskB[features], taskB[classifier], test_size=0.2, random_state=1)

clf = skTree.DecisionTreeClassifier()
clf = clf.fit(xtrain, ytrain)

y_pred = clf.predict(xtest)


print("accuracy original: " , metrics.accuracy_score(ytest, y_pred))
clf.max_depth = 3
clf.min_samples_split = 100
clf.min_samples_leaf = 25
clf = clf.fit(xtrain, ytrain)
y_pred = clf.predict(xtest)

print("accuracy new: " , metrics.accuracy_score(ytest, y_pred))
print("confusion matrix: \n", metrics.confusion_matrix(ytest, y_pred))

# skTree.plot_tree(clf)
# plt.show()


