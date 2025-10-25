# NVIDIA Stock Analysis

Understanding market behavior through data exploration and technical analysis

---

## Why This Project Exists

I've always been curious about how financial markets work, especially for tech companies driving major innovations. NVIDIA caught my attention not just because of their role in AI and gaming, but because their stock price tells an interesting story about market sentiment toward emerging technologies

This project started as a way to learn data analysis with real-world financial data. Instead of working with clean academic datasets, I wanted to wrestle with actual market data 

The goal was never to build a trading system or predict the future. Markets are way too complex for that, this is about understanding patterns, learning technical analysis concepts, and building solid data analysis skills

## What is Inside

The project pulls historical NVIDIA stock data and explores it from multiple angles. I calculate common technical indicators that traders use such as moving averages, relative strength index, MACD, and others. Then I visualize these patterns to see what stories the data tells

There are two main notebooks here. The first does exploratory analysis, looking at price movements, volatility patterns, and trading volume behavior. The second digs into technical indicators and examines correlations between different metrics

All the data comes from Yahoo Finance public API, so everything here uses freely available information. No special access, no proprietary data, just what anyone can pull from the internet

## Technical Stack

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

Everything runs in Jupyter notebooks for interactive exploration, with modular code in the src directory that can be reused across different analyses

## Getting It Running

First, make sure you have Python 3.8 or later installed. Clone this repository to your local machine

Set up a virtual environment to keep dependencies isolated:
```bash
python3 -m venv venv
source venv/bin/activate  # On Mac/Linux
```

Install the required packages:
```bash
pip install -r requirements.txt
```

For a quick overview, run the main script:
```bash
python3 main.py
```

For detailed analysis, launch Jupyter and explore the notebooks:
```bash
jupyter notebook
```

The notebooks in the `notebooks` directory contain the full analysis with visualizations and explanations

## Project Organization
```
nvidia-stock-analysis/
├── src/                    # Core functionality
│   ├── data_fetcher.py    # Pulls data from Yahoo Finance
│   └── features.py        # Calculates technical indicators
├── notebooks/              # Analysis and visualizations
│   ├── 01_data_exploration.ipynb
│   └── 02_stock_analysis.ipynb
├── main.py                # Quick analysis script
├── requirements.txt       # Python dependencies
└── README.md             # You are here
```

## Important Disclaimers

This is a learning project by a student, not financial advice. I'm not a financial advisor, and nothing here should influence your investment decisions

Stock markets are inherently risky. Past performance doesn't predict future results. If you're making investment decisions, consult with qualified financial professionals and do your own thorough research.

All data used is publicly available from Yahoo Finance. No proprietary or insider information is used anywhere in this analysis.

## Future Possibilities

Some ideas for extending this project:
1. Compare NVIDIA with competitors like AMD and Intel
2. Analyze correlation with broader indices like NASDAQ
3. Add interactive dashboards using Streamlit or Plotly Dash
4. Explore longer historical periods (10+ years)
5. Study the impact of major events (product launches, earnings reports)

But for now, this serves its purpose as a solid foundation in financial data analysis

## Acknowledgments

Data provided by Yahoo Finance through the yfinance library. Thanks to the open source community for building and maintaining these tools.

Inspiration came from various online courses, finance blogs, etc
