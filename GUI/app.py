import pickle
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re
from flask import Flask, render_template, request

dic = {'Decision Tree': 'model_dec_tree.pkl', 'Linear SVC': 'model_LinearSVC.pkl', 'KNN': 'model_KNN.pkl', 'Logistic Regression': 'model_Logi_Reg.pkl',
       'Multinomial Naive Bayes': 'model_mnnb.pkl', 'Random Forest': 'model_random_forest.pkl', 'SVC': 'model_SVC.pkl'}

file = open('dic_name_4cat.pkl', 'rb')
mapping = pickle.load(file)

class Lemmatizer(object):
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()

    def __call__(self, sentence):
        return [self.lemmatizer.lemmatize(word) for word in sentence.split() if len(word)>2]

def clean_test(temp):
    file = open('vectorizer.pkl', 'rb')
    vectorizer = pickle.load(file)
    data_length = []
    lemmatizer = WordNetLemmatizer()
    cleaned_text = []
    stop_words = set(stopwords.words('english'))  # Load stop words

    sentence = temp.lower()
    sentence = re.sub('https?://[^\s<>"]+|www\.[^\s<>"]+', ' ', sentence)
    sentence = re.sub('[^0-9a-z]', ' ', sentence)
    sentence = " ".join([word for word in sentence.split() if word not in stop_words])  # Remove stop words
    sentence = lemmatizer.lemmatize(sentence)  # Lemmatize words
    data_length.append(len(sentence.split()))  # Split data, measure length of new filtered data
    cleaned_text.append(sentence)
    vect_temp = vectorizer.transform(cleaned_text).toarray()

    return vect_temp


app = Flask(__name__)


@app.route('/')
def index():
    models = ['Decision Tree', 'Linear SVC', 'KNN', 'Logistic Regression', 'Multinomial Naive Bayes', 'Random Forest', 'SVC']
    return render_template('index.html', models=models)

@app.route('/predict', methods=['POST'])
@app.route('/predict', methods=['POST'])
def get_results():
    string = request.form["string"]
    model_name = request.form["model"]

    file = open(dic[model_name], 'rb')
    # dump information to that file
    model = pickle.load(file)

    x = clean_test(string)
    temp = model.predict(x)
    ans = mapping[temp[0]]
    print(ans)
    # Check the personality type and return the appropriate template
    if ans == 'Analysts':
        return render_template('analysts.html')
    elif ans == 'Diplomats':
        return render_template('diplomats.html')
    elif ans == 'Sentinels':
        return render_template('sentinels.html')
    elif ans == 'Explorers':
        return render_template('explorers.html')
    else:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
