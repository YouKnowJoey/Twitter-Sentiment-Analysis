# 🐦 Twitter-Sentiment-Analysis
>This project applies Natural Language Processing (NLP) techniques to extract and classify the emotional tone of social media text data. We will analyze sentiment of tweets sourced from X (formerly Twitter) using machine learning (ML). It leverages the Sentiment140 dataset, imported via Hugging Face Datasets, as the training and testing source. Real-time tweets are retrieved using the Tweepy library with authenticated access to the Twitter API.
>
>The goal is to evaluate the performance of various classification models including Logistic Regression, Random Forest, and others to determine which performs best for sentiment classification tasks.
>
>**The reproducibility of this project will be in the form of conda 'environment.yml'.**

_**The IMPORTANT FILE that preprocesses and evaluates models is 'nlp_sentiment_pipline.ipynb'**_

## ⚙️ Reproduce Results
In the command line execute:
1. 'conda env create -f environment.yml'
2. 'conda activate twitter-sentiment'

_**Advice: Python Kernel is easily installed with VS Code**_

## 📂 Data Source & Description

This project uses the [Sentiment140 dataset](https://huggingface.co/datasets/stanfordnlp/sentiment140) hosted on Hugging Face Datasets.

### Dataset Details:
- **Source**: Hugging Face Datasets → [`stanfordnlp/sentiment140`](https://huggingface.co/datasets/stanfordnlp/sentiment140)
- **Size**: 1.6 million tweets
- **Labels**:
  - `0`: Negative sentiment
  - `2`: Neutral sentiment (often excluded in binary classification tasks)
  - `4`: Positive sentiment

## 📊 Concluding Results

| Model                     | Best Params                                                              | F1-Score | Accuracy |
|--------------------------|---------------------------------------------------------------------------|----------|----------|
| **Logistic Regression**  | `{'C': 1, 'solver': 'saga'}`                                              | 0.78     | 0.77     |
| **Multinomial Naive Bayes** | `{'alpha': 6.0, 'class_prior': None, 'fit_prior': False}`              | 0.76     | 0.76     |
| **Support Vector Machine (SVM)** | `{'C': 0.1, 'dual': False, 'max_iter': 1000, 'penalty': 'l1'}`   | 0.78     | 0.77     |

### 🔍 Sample Classified Tweets (15 Live Twitter Samples)

#### ✅ Positive Sentiment Tweets:
- "Welcome first meeting White House FIFA task force..."
- "🇺🇸 Steve Witkoff officially sworn Oval Office..."
- "RT Evening Parade longstanding tradition Marine..."
- "Country blessed negotiator skill experience..."
- "RT Thank President Trump inviting White House..."
- "Great honor Prime Minister U day ago big elect..."
- "RT Don’t need energy transition need energy ad..."
- "RT Energy price 🇺🇸"
- "RT Thanks hardworking partner canceling wastef..."
- "RT Message clear DHS enforce law put safety Am..."
- "RT 🏆 Award show like 📸 scene SmallBusinessWeek..."
- "President Trump Vance FIFA President Gianni In..."

#### ❌ Negative Sentiment Tweets:
- "RT Sgt Brian Lieberman ran toward gunfire save..."
- "RT Even know air traffic control problem isn’t..."
- "RT Played political game expense air traffic c..."

## 🚀 Aspirational Improvements
- Introduce Non-linear ML models (i.e.Generalized Additive Models (GAMs), Local Regression (LOESS), or Splines)
- Use different Vectorization methods (i.e. Word2Vec or GloVe) in place of TF-IDF matrices

## 📚 Citations
- Go, A., Bhayani, R. and Huang, L., 2009. Twitter sentiment classification using distant supervision. CS224N Project Report, Stanford, 1(2009), p.12.
- [@vprusso](https://github.com/vprusso/youtube_tutorials/tree/master/twitter_python/part_5_sentiment_analysis_tweet_data). twitter_python. Notes: "Tweepy APIv1 tutorial". 
