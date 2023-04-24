# MBTI-Personality-Prediction

The project aims to predict personality types of individuals using Natural Language Processing (NLP) techniques and Machine Learning (ML) algorithms. The dataset used for training and testing the model is the Myers-Briggs Type Indicator (MBTI) dataset which contains a collection of posts from individuals in the PersonalityCafe forum, along with their corresponding personality types based on the MBTI framework.

The project report can be read [here](https://docs.google.com/document/d/1sAeiX7H6zs6d5ZiD7Q1SZ--Dh7ajJi5Ro2JBH2GCIZI/edit?usp=sharing)

## Data Preprocessing

The dataset was preprocessed by performing the following steps:

1) Converting all text to lowercase
2) Removing URLs, mentions, special characters, and stop words
3) Stemming and lemmatization
4) Vectorizing the text using the Term Frequency-Inverse Document Frequency (TF-IDF) technique

### Handling Imbalanced Data

The MBTI dataset was imbalanced, with some personality types having a significantly smaller number of samples than others. To handle this, undersampling, oversampling, and SMOTe techniques were used to balance the data.

## Model Training

Three different models were trained on the preprocessed dataset:
1) Linear SVC
2) SVC
3) KNN
4) Random Forest
5) Multinomial Naive Bayes
6) Logistic Regression

## GUI

A simple web-based graphical user interface (GUI) was built using Flask, which allows users to input a text sample and receive a predicted personality type based on the trained models.
```
pip install -r requirements.txt
```
Then run the following command:
```
python app.py
```
## Kaggle Notebook

A [Kaggle notebook](https://github.com/MOAzeemKhan/MBTI-Personality-Prediction/blob/main/4personality-prediction-using-nlp-ml.ipynb) was created to provide a step-by-step guide for the project. It includes the code, visualizations, and explanations of the various techniques used.

## Credits

This project was created by:
1) [Mohammed Azeem Khan](https://www.linkedin.com/in/mohammed-azeem-khan/)
2) [Rishabh Kinhikar](https://www.linkedin.com/in/rishabh-kinhikar-61130113a/)
3) [Omkar Iyer](https://www.linkedin.com/in/orbia343/)
4) [Achintya Kamath](https://www.linkedin.com/in/achintya-kamath-97231b245/)

The dataset used in this project was obtained from Kaggle and can be found [here](https://www.kaggle.com/datasets/datasnaek/mbti-type).

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/MOAzeemKhan/MBTI-Personality-Prediction/blob/main/license) file for details.
