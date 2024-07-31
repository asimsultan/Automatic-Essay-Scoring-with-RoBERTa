
# Automatic Essay Scoring with RoBERTa

Welcome to the Automatic Essay Scoring with RoBERTa project! This project focuses on scoring essays using the RoBERTa model.

## Introduction

Automatic essay scoring involves evaluating and scoring essays based on their content. In this project, we leverage the power of RoBERTa to perform essay scoring using a dataset of essays and their scores.

## Dataset

For this project, we will use a custom dataset of essays and their scores. You can create your own dataset and place it in the `data/essay_scoring_data.csv` file.

## Project Overview

### Prerequisites

- Python 3.6 or higher
- PyTorch
- Hugging Face Transformers
- Datasets
- Scikit-learn

### Installation

To set up the project, follow these steps:

```bash
# Clone this repository and navigate to the project directory:
git clone https://github.com/your-username/roberta_essay_scoring.git
cd roberta_essay_scoring

# Install the required packages:
pip install -r requirements.txt

# Ensure your data includes essays and their scores. Place these files in the data/ directory.
# The data should be in a CSV file with two columns: text and score.

# To fine-tune the RoBERTa model for essay scoring, run the following command:
python scripts/train.py --data_path data/essay_scoring_data.csv

# To evaluate the performance of the fine-tuned model, run:
python scripts/evaluate.py --model_path models/ --data_path data/essay_scoring_data.csv
