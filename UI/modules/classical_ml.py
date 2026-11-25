
import json
import joblib
import pandas as pd


MODEL_PATH = ("/content/drive/MyDrive/data_handling_and_machine_learning/datasets/classical_ml_classification_dataset/InvestIQ_decision_tree_model.pkl")

FEATURES_PATH = ("/content/drive/MyDrive/data_handling_and_machine_learning/datasets/classical_ml_classification_dataset/InvestIQ_classical_ml_features.json")

IMPUTER_PATH = ("/content/drive/MyDrive/data_handling_and_machine_learning/datasets/classical_ml_classification_dataset/InvestIQ_classical_ml_imputer.pkl")

_model = None
_imputer = None
_features = None

def load_artifacts():
    global _model, _imputer, _features

    if _model is None:
        _model = joblib.load(MODEL_PATH)

    if _imputer is None:
        _imputer = joblib.load(IMPUTER_PATH)

    if _features is None:
        with open(FEATURES_PATH, "r", encoding="utf-8") as f:
            _features = json.load(f)

    return _model, _imputer, _features

def predict_positive_return_probability(company_data):
    """
    Predict the probability of a positive 1-year future return.

    company_data must contain the 31 features used during training.
    """

    model, imputer, features = load_artifacts()

    input_data = company_data[features].copy()

    input_imputed = imputer.transform(input_data)

    input_imputed = pd.DataFrame(
        input_imputed,
        columns=features,
        index=input_data.index
    )

    probability = model.predict_proba(input_imputed)[0][1]

    return float(probability)
