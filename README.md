# 📰 Financial News Sentiment Analysis

This repository provides a comprehensive toolkit for scraping financial news articles, performing natural language processing (NLP) to extract sentiment scores, and analyzing the correlation between news sentiment and market movement. It is designed for researchers, quantitative analysts, and anyone interested in behavioral finance.

## 🔎 Project Overview  
The core purpose of this project is to quantify the emotional tone (positive, negative, neutral) present in financial news and use these insights to gain a predictive edge or better understand market reactions.

The process involves:

1.  **Data Acquisition (scraper.py)**: Fetching real-time or historical news headlines and articles from financial sources.

2.  **Sentiment Scoring (sentiment.py)**: Applying NLP models or specialized financial lexicons to calculate a quantifiable sentiment score for the text.

3.  **Analysis (analysis.ipynb)**: Visualizing sentiment trends and correlating them with corresponding stock price or index fluctuations.---

## 📚 Theoretical Background

**What is Financial Sentiment Analysis?**
Sentiment Analysis (SA), or Opinion Mining, is the computational study of opinions, attitudes, and emotions expressed in text. In finance, SA focuses on quantifying the tone of news or social media related to companies, markets, or economic indicators.

Traditional financial models often rely solely on historical price and volume data, assuming market efficiency. However, Behavioral Finance suggests that investor emotions and sentiment (often driven by news) can lead to market inefficiencies, volatility, and short-term mispricings.

**Methods for Sentiment Scoring**
Sentiment extraction typically employs one of two main approaches:

1.  **Lexicon-Based Approach**: This method uses pre-defined dictionaries (lexicons) where words are manually or statistically assigned a positive, negative, or neutral score. For financial texts, specialized lexicons like the Loughran-McDonald dictionary are preferred over general-purpose ones, as words like "liability" or "tax" are generally negative in finance but neutral elsewhere.

2.  **Machine Learning / Deep Learning Approach**: This involves training models (like Recurrent Neural Networks, such as LSTMs, or modern transformers) on large, pre-labeled datasets of financial text to classify new text as positive, negative, or score its emotional intensity. This approach is highly flexible but requires significant training data.

The resulting sentiment score serves as a crucial non-traditional input for trading strategies and risk modeling.
---

## ✅ Key Features
- **Custom News Scraper**: Efficiently retrieves targeted financial news using scraper.py.

-  **Specialized Sentiment Module**: Utilizes sentiment.py for advanced text processing and sentiment scoring.

-  **Interactive Analysis**: Jupyter notebook for data cleaning, visualization, and sentiment-price correlation.

-  **Testing Suite**: Robust unit tests to ensure the reliability of the sentiment scoring and scraping utilities.
---
##  📂 Repository Structure
```bash
financial-news-sentiment/
├── LICENSE
├── README.md
├── README_NOTEBOOK.md    # Documentation specific to the analysis notebook
├── examples
│   └── run_analysis.py   # Example script to execute the main workflow
├── notebooks
│   └── analysis.ipynb    # Jupyter notebook for deep-dive analysis and visualization
├── requirements.txt      # Project dependencies
├── src
│   ├── scraper.py        # Module for fetching financial news data
│   └── sentiment.py      # Module containing sentiment scoring logic
└── tests
    └── test_sentiment.py # Unit tests for the sentiment module
```

## ⚙️ Installation and Usage 

### 1. Clone the Repository  
```bash
git clone https://github.com/saumyajain2007/financial-news-sentiment.git
cd financial-news-sentiment
```

### 2. Create and Activate Virtual Environment (Recommended)  
```bash
python -m venv venv
source venv/bin/activate   # On Linux/macOS
# .\venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4. Run Example Analysis
Execute the end-to-end example script to fetch data, calculate sentiment, and output results:
```bash
python examples/run_analysis.py
```

### 5. Launch Jupyter Notebook
Execute the end-to-end example script to fetch data, calculate sentiment, and output results:
```bash
jupyter lab notebooks/analysis.ipynb
```

### 6. Unit Testing
Ensure all data utilities and sentiment scoring models are functioning correctly:
```bash
jupyter lab notebooks/analysis.ipynb
```


---

## 📊 Usage  

### Run the Jupyter Notebook  
```bash
jupyter notebook
```
- Open `notebooks/LSTM_Forecasting.ipynb`  
- Run all cells sequentially  
- Modify the target stock ticker, lookback window, and model parameters directly in the notebook  

### Run Unit Tests  
Ensure all data utilities and sentiment scoring models are functioning correctly:
```bash
pytest tests/
```

---
---

## 🤝 Contributing  
Contributions are welcome!  
Please check out the upcoming **CONTRIBUTING.md** for guidelines on submitting pull requests, reporting issues, and suggesting improvements.  

---

## 📜 License  
This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.  
