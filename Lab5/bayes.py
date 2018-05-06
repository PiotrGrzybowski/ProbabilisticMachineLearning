import pandas as pd
import numpy as np

import scipy
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score


def load_file(filename):
    return pd.read_csv(filename)


def split_data(data, ratio):
    shuffle(data)
    index = int(data.shape[0]*ratio)
    print(index)
    return data.iloc[:index], data.iloc[index:]


def shuffle(data):
    return data.sample(frac=1).reset_index(drop=True)


def calc_attribute_probabilities_cont(class_data):
    return {column: [class_data[column].mean(), class_data[column].std()] for column in class_data}


def predict(parameters, data):
    class_probabilities = np.zeros((data.shape[0], len(parameters)))
    for key in parameters:
        probability_matrix = np.zeros((data.shape[0], len(data.columns)))
        i = 0
        for column in data.columns:
            probability_matrix[:, i] = [scipy.stats.norm(parameters[key][column][0],
                                                         parameters[key][column][1]).pdf(elem) for elem in data[column]]
            i += 1
        probability_values = np.sum(np.log(probability_matrix), axis=1)
        class_probabilities[:, key] = probability_values
    print(class_probabilities)
    return class_probabilities.argmax(1)


def print_metrics(actual, predicted):
    print('Accuracy: ' + str(accuracy_score(actual, predicted)))
    print('Precision: ' + str(precision_score(actual, predicted, average="macro")))
    print('Recall: ' + str(recall_score(actual, predicted, average="macro")))
    print('F-score: ' + str(f1_score(actual, predicted, average="macro")))


label_col = 'Type'
data = load_file('diabets.data')
data = shuffle(data)
train, test = train_test_split(data, test_size=0.2)

model_parameters = {category: calc_attribute_probabilities_cont(data.loc[data[label_col] == category].drop(label_col, axis=1)) for category in data[label_col].unique()}

print(model_parameters)

test_y = test[label_col]
test = test.drop(label_col, axis=1)

prediction = predict(model_parameters, test)
# print(sum(prediction == test_y.as_matrix())/prediction.shape[0])

print("MANUAL")
print_metrics(prediction, test_y.as_matrix())

gnb = GaussianNB()
y_pred = gnb.fit(train.drop(label_col, axis=1), train[label_col]).predict(test)
# print(sum(y_pred == test_y.as_matrix())/prediction.shape[0])

print("AUTOMATIC")
print_metrics(y_pred, test_y.as_matrix())
