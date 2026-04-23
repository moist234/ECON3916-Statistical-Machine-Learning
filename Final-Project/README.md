# NBA Player Points Predictor

Predicts NBA player points scored using a Random Forest model trained 
on 2023-24 season game logs.

**Live app:** https://econ3916-statistical-machine-learning-rtovuvd3pksxj5cyzmzbfi.streamlit.app

## Environment Setup

1. Clone the repo:
git clone https://github.com/moist234/ECON3916-Statistical-Machine-Learning.git
cd ECON3916-Statistical-Machine-Learning

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate

3. Install dependencies:
pip install nba_api pandas numpy scikit-learn streamlit joblib matplotlib seaborn

## Data Acquisition

Data is pulled automatically from the NBA API when you run the notebook.
No CSV files needed. Requires an internet connection.

## Run the Notebook

1. Open Final-Project/Final-Project-Starter.ipynb in VS Code or Jupyter
2. Run all cells top to bottom
3. The notebook will download data, engineer features, train models, 
   and save model_small.pkl to the Final-Project/ folder

## Launch Streamlit App Locally

1. Make sure model_small.pkl is in the Final-Project/ folder
2. Run:
cd Final-Project
streamlit run app.py

3. Open http://localhost:8501 in your browser