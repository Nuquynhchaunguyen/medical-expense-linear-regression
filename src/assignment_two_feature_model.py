from pathlib import Path
import math

import numpy as np
import pandas as pd


# -----------------------------
# 1. Load data
# -----------------------------

DATA_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "insurance-premium-prediction"
    / "insurance.csv"
)

df = pd.read_csv(DATA_PATH)

# Keep only the variables needed for this assignment
df = df[["bmi", "age", "expenses"]].dropna()

bmi = df["bmi"].to_numpy(dtype=float)
age = df["age"].to_numpy(dtype=float)
expenses = df["expenses"].to_numpy(dtype=float)

print("Data loaded successfully")
print("Number of rows:", len(df))
print(df.head())

# -----------------------------
# 2. Evaluation metrics
# -----------------------------

def mse(y_true, y_pred):
    return float(np.mean((y_true - y_pred) ** 2))


def rmse(y_true, y_pred):
    return float(np.sqrt(mse(y_true, y_pred)))


def mae(y_true, y_pred):
    return float(np.mean(np.abs(y_true - y_pred)))


def r2_score(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return float(1 - ss_res / ss_tot)

# -----------------------------
# 3. BMI-only baseline model
# -----------------------------

def fit_single_feature_ols(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean) ** 2)

    w1 = numerator / denominator
    w0 = y_mean - w1 * x_mean

    return float(w0), float(w1)


baseline_w0, baseline_w1 = fit_single_feature_ols(bmi, expenses)

baseline_pred = baseline_w0 + baseline_w1 * bmi

baseline_mse = mse(expenses, baseline_pred)
baseline_rmse = rmse(expenses, baseline_pred)
baseline_mae = mae(expenses, baseline_pred)
baseline_r2 = r2_score(expenses, baseline_pred)

print("\nBMI-only baseline:")
print(f"w0 = {baseline_w0:.2f}")
print(f"w1 = {baseline_w1:.2f}")
print(f"MSE = {baseline_mse:.2f}")
print(f"RMSE = {baseline_rmse:.2f}")
print(f"MAE = {baseline_mae:.2f}")
print(f"R2 = {baseline_r2:.4f}")

# -----------------------------
# 4. Two-feature Normal Equation
# -----------------------------

X = np.column_stack([
    np.ones(len(df)),
    bmi,
    age
])

y = expenses

theta_ne = np.linalg.solve(X.T @ X, X.T @ y)

w0_ne, w1_ne, w2_ne = theta_ne

pred_ne = X @ theta_ne

ne_mse = mse(y, pred_ne)
ne_rmse = rmse(y, pred_ne)
ne_mae = mae(y, pred_ne)
ne_r2 = r2_score(y, pred_ne)

print("\nTwo-feature Normal Equation:")
print(f"w0 = {w0_ne:.2f}")
print(f"w1 (BMI) = {w1_ne:.2f}")
print(f"w2 (Age) = {w2_ne:.2f}")
print(f"MSE = {ne_mse:.2f}")
print(f"RMSE = {ne_rmse:.2f}")
print(f"MAE = {ne_mae:.2f}")
print(f"R2 = {ne_r2:.4f}")

# -----------------------------
# 5. Two-feature Gradient Descent
# -----------------------------

def standardize_feature(x):
    mean = np.mean(x)
    std = np.std(x)
    return (x - mean) / std, float(mean), float(std)


bmi_std, bmi_mean, bmi_std_dev = standardize_feature(bmi)
age_std, age_mean, age_std_dev = standardize_feature(age)

X_std = np.column_stack([
    np.ones(len(df)),
    bmi_std,
    age_std
])

learning_rate = 0.05
epochs = 6000

theta_gd = np.zeros(3)

for epoch in range(epochs):
    pred_std = X_std @ theta_gd
    errors = pred_std - expenses

    gradient = (2 / len(df)) * (X_std.T @ errors)

    theta_gd -= learning_rate * gradient

# Convert Gradient Descent weights back to original units

w1_gd = theta_gd[1] / bmi_std_dev
w2_gd = theta_gd[2] / age_std_dev

w0_gd = (
    theta_gd[0]
    - theta_gd[1] * bmi_mean / bmi_std_dev
    - theta_gd[2] * age_mean / age_std_dev
)

pred_gd = w0_gd + w1_gd * bmi + w2_gd * age

gd_mse = mse(expenses, pred_gd)
gd_rmse = rmse(expenses, pred_gd)
gd_mae = mae(expenses, pred_gd)
gd_r2 = r2_score(expenses, pred_gd)

print("\nTwo-feature Gradient Descent:")
print(f"w0 = {w0_gd:.2f}")
print(f"w1 (BMI) = {w1_gd:.2f}")
print(f"w2 (Age) = {w2_gd:.2f}")
print(f"MSE = {gd_mse:.2f}")
print(f"RMSE = {gd_rmse:.2f}")
print(f"MAE = {gd_mae:.2f}")
print(f"R2 = {gd_r2:.4f}")

# -----------------------------
# 6. Comparison table and CSV export
# -----------------------------

results = pd.DataFrame([
    {
        "model": "BMI-only baseline",
        "w0": baseline_w0,
        "w1_bmi": baseline_w1,
        "w2_age": np.nan,
        "MSE": baseline_mse,
        "RMSE": baseline_rmse,
        "MAE": baseline_mae,
        "R2": baseline_r2,
    },
    {
        "model": "Normal Equation (BMI + Age)",
        "w0": w0_ne,
        "w1_bmi": w1_ne,
        "w2_age": w2_ne,
        "MSE": ne_mse,
        "RMSE": ne_rmse,
        "MAE": ne_mae,
        "R2": ne_r2,
    },
    {
        "model": "Gradient Descent (BMI + Age)",
        "w0": w0_gd,
        "w1_bmi": w1_gd,
        "w2_age": w2_gd,
        "MSE": gd_mse,
        "RMSE": gd_rmse,
        "MAE": gd_mae,
        "R2": gd_r2,
    },
])

print("\nModel comparison:")
print(results.round(4).to_string(index=False))

REPORT_PATH = (
    Path(__file__).resolve().parent.parent
    / "reports"
    / "assignment_results.csv"
)

REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
results.to_csv(REPORT_PATH, index=False)

print(f"\nResults saved to: {REPORT_PATH}")
