import pandas as pd
import numpy as np


def format_output(x):
    x[:, 0] = np.rint(np.maximum(0, x[:, 0]))
    x[:, 1] = np.rint(np.maximum(0, x[:, 1]))
    x[:, 2] = np.rint(np.maximum(0, x[:, 2]))
    x[:, 3] = np.rint(np.maximum(0, x[:, 3]))
    x[:, 4] = np.rint(np.maximum(0, x[:, 4]))
    x[:, 5] = np.maximum(0, x[:, 5])
    x[:, 6] = np.maximum(0, x[:, 6])
    x[:, 7] = np.rint(np.maximum(0, x[:, 7]))
    x[:, 8] = (x[:, 8]>=0.5)
    return x

def format_output_db(db):
    return db.astype({"Pregnancies": int, "Glucose": int, "BloodPressure": int, "SkinThickness": int, "Insulin": int, "BMI": float, "DiabetesPedigreeFunction": float, "Age": int, "Outcome": int})
