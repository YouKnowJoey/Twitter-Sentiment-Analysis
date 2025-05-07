# Twitter-Sentiment-Analysis
>This project applies Natural Language Processing (NLP) techniques to extract and classify the emotional tone of social media text data. We will analyze sentiment of tweets sourced from X (formerly Twitter) using machine learning (ML). It leverages the Sentiment140 dataset, imported via Hugging Face Datasets, as the training and testing source. Real-time tweets are retrieved using the Tweepy library with authenticated access to the Twitter API.
>
>The goal is to evaluate the performance of various classification models including Logistic Regression, Random Forest, and others to determine which performs best for sentiment classification tasks.
>
>**The reproducibility of this project will be in the form of conda 'environment.yml'.**

_**The IMPORTANT FILE that preprocesses and evaluates models is 'nlp_sentiment_pipline.ipynb'**_

## Reproduce Results
In the command line execute:
1. 'conda env create -f environment.yml'
2. 'conda activate twitter-sentiment'

_**Advice: Python Kernel is easily installed with VS Code**_

## Aspirational Improvements
- Introduce Non-linear ML models (i.e.Generalized Additive Models (GAMs), Local Regression (LOESS), or Splines)
- Use different Vectorization methods (i.e. Word2Vec or GloVe) in place of TF-IDF matrices

## Citations
- Go, A., Bhayani, R. and Huang, L., 2009. Twitter sentiment classification using distant supervision. CS224N Project Report, Stanford, 1(2009), p.12.
- [@vprusso](https://github.com/vprusso/youtube_tutorials/tree/master/twitter_python/part_5_sentiment_analysis_tweet_data). twitter_python. Notes: "Tweepy APIv1 tutorial". 
