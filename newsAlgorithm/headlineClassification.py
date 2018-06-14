import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import PassiveAggressiveClassifier
import matplotlib.pyplot as plt
import itertools
from sklearn import metrics
from sklearn.model_selection import train_test_split

engine = create_engine('postgresql://willlewis@localhost:5432/willlewis')
df = pd.read_sql_query('select * from "newsAlgorithm_headline_dataset"',con=engine)

#df = df.set_index('Unnamed: 0')
y = df.status

df = df.drop('status', axis=1)

X_train, X_test, y_train, y_test = train_test_split(df['headline'], y, test_size=0.33, random_state=53)

user_headline = ['Donald Trump eats chinese cat']

count_vectorizer = CountVectorizer(stop_words='english')
count_train = count_vectorizer.fit_transform(X_train)
count_test = count_vectorizer.transform(X_test)

tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
tfidf_train = tfidf_vectorizer.fit_transform(X_train)
tfidf_test = tfidf_vectorizer.transform(X_test)
tfidf_test_headline = tfidf_vectorizer.transform(user_headline)

tfidf_vectorizer.get_feature_names()[-10:]
count_vectorizer.get_feature_names()[:10]


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    See full source and example:
    http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html

    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


clf = MultinomialNB()

clf.fit(tfidf_train, y_train)
pred = clf.predict(tfidf_test)
prediction = clf.predict(tfidf_test_headline)
prediction_score = clf.predict_proba(tfidf_test_headline)
score = metrics.accuracy_score(y_test, pred)
print("clf.fit(tfidf_train, y_train)")
print("accuracy:   %0.3f" % score)
print("--------")
cm = metrics.confusion_matrix(y_test, pred, labels=['FAKE', 'REAL'])
plot_confusion_matrix(cm, classes=['FAKE', 'REAL'])


print('Here is the prediction...')
print(prediction)
print(prediction_score)