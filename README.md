# Impulse Buying Insights
Analysis of psychological traits and consumer behavior for impulse buying

## Project Overview
This project explores psychological and personality factors that influence impulse buying behavior. Using a dataset of 300 participants, the analysis investigates correlations between personality traits, stress levels, gender, and responses to marketing stimuli such as discounts and luxury advertisements. The goal is to practice data analysis, gain insights into consumer behavior, and understand which factors impact purchasing decisions.

## Objective
- Analyze the relationship between personality traits (Big Five) and impulse buying.
- Examine the effect of stress, gender, and marketing campaigns on purchasing behavior.
- Identify clusters of consumers with similar behavioral patterns.
- Practice working with CSV files, pandas, and data visualization in Python.

## Dataset
The dataset contains the following columns:
- `ID` – Participant ID
- `Age` – Participant's age
- `Gender` – Participant's gender (M/F)
- `Big5_Openness` – Openness personality trait
- `Big5_Conscientiousness` – Conscientiousness personality trait
- `Big5_Extraversion` – Extraversion personality trait
- `Big5_Agreeableness` – Agreeableness personality trait
- `Big5_Neuroticism` – Neuroticism personality trait
- `Stress_Level` – Participant's stress level (scale)
- `Impulse_Buying_Score` – Impulse buying score
- `Reaction_Discount (%)` – Response to discounts
- `Reaction_Luxury_Ad (%)` – Response to luxury advertisements

The dataset is stored in `data/psych_marketing_data.csv`.

## Project Structure
<img width="507" height="332" alt="image" src="https://github.com/user-attachments/assets/63a0f5c7-896c-45ac-930b-fa408420138c" />


## How to Run
- Clone the repository:
```git clone https://github.com/<your-username>/ImpulseBuyingInsights.git```
- Install dependencies:
```pip install -r requirements.txt```
- Run the main analysis:
```python scripts/analysis.py```


## Features
- Calculate correlations between impulse buying and personality, stress, gender.
- Form predefined clusters of participants based on traits and stress levels.
- Create custom clusters interactively.
- Generate histograms, scatter plots, and bar charts to visualize results.
- Compare reactions to discounts and luxury ads across clusters.

Author: 
ankasstar
