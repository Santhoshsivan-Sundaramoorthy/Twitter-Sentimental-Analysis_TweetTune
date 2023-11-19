# Twitter Sentiment Analysis Project  TweetTune

Live Demo: https://tweettune.streamlit.app/

## Overview

This project focuses on analyzing the sentiments of tweets collected from the social networking website Twitter. The dataset comprises 1,600,000 tweets extracted using the Twitter API. Each tweet is labeled with its sentiment polarity (0 = negative, 2 = neutral, 4 = positive). The goal of the project is to design a classification model that accurately predicts the polarity of tweets.

## Dataset

The dataset includes the following six fields:

1. **target**: The polarity of the tweet (0 = negative, 2 = neutral, 4 = positive).
2. **ids**: The ID of the tweet.
3. **date**: The date of the tweet (in the format Sat May 16 23:58:44 UTC 2009).
4. **flag**: The query. If there is no query, then this value is NO_QUERY.
5. **user**: The user that tweeted.
6. **text**: The text of the tweet.

## Classification Model

To achieve the goal of predicting tweet polarity, a classification model has been implemented. The model takes into account the textual content of the tweets and utilizes machine learning techniques to classify them into one of the three polarity categories: negative, neutral, or positive.

### Technologies Used

- Python
- Scikit-learn
- Natural Language Processing (NLP) techniques
- [Any other libraries or tools you used]

### Model Training

The model has been trained on a portion of the dataset using a combination of feature engineering, text preprocessing, and a suitable machine learning algorithm. The training process includes:

1. **Data Cleaning**: Handling missing values, removing duplicates, etc.
2. **Text Preprocessing**: Tokenization, stemming, and other NLP techniques to prepare the text data for modeling.
3. **Feature Extraction**: Converting text data into numerical features suitable for machine learning algorithms.
4. **Model Selection**: Choosing an appropriate classification algorithm based on the nature of the problem.
5. **Hyperparameter Tuning**: Optimizing the model's hyperparameters for better performance.

## Evaluation

The model's performance has been evaluated using a separate test set from the dataset. Common evaluation metrics such as accuracy, precision, recall, and F1-score have been used to assess the model's effectiveness in predicting tweet polarity.

## Usage

To use the trained model for predicting tweet polarity, follow the steps outlined in "Model/Model Selection.ipynb". Ensure that you have the necessary dependencies installed.

## Future Improvements

This section can outline potential enhancements or additional steps that could be taken to improve the model's performance or extend the project.

## Contributors

- Santhoshsivan Sundaramoorthy

## License

This project is licensed under the MIT License.
