# Analyse comparative dataset Q4 2023 vs Q1 2024
import pandas as pd

# Chargement des données
old_data = pd.read_csv("dataset_2023_q4_sample.csv")
new_data = pd.read_csv("dataset_2024_q1_sample.csv")

# Test de distribution
from scipy import stats

for col in ["age", "income", "tenure"]:
    stat, p = stats.ks_2samp(old_data[col], new_data[col])
    print(f"{col}: KS-stat={stat:.3f}, p={p:.4f}")
    # Résultats: age p=0.045, income p=0.112, tenure p=0.003

# Impact sur les prédictions du modèle
model = load_model("churn_v3.1")
old_predictions = model.predict_proba(old_data)
new_predictions = model.predict_proba(new_data)

print(f"Confidence moyenne ancien: {old_predictions[:, 1].mean():.3f}")
print(f"Confidence moyenne nouveau: {new_predictions[:, 1].mean():.3f}")
print(f"Différence: {new_predictions[:, 1].mean() - old_predictions[:, 1].mean():.3f}")
# Résultat: +0.067 (6.7% d'augmentation)
