# Sauvegardé dans: backup/metrics_calculation_v2.0.py
"""
Version originale avant optimisation du 15/01/2024
"""


def calculate_precision(y_true, y_pred):
    """
    Calcule la précision standard.
    Pas de facteur d'ajustement métier.
    """
    true_positives = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 1)
    predicted_positives = sum(1 for p in y_pred if p == 1)

    if predicted_positives == 0:
        return 0.0

    return true_positives / predicted_positives  # Version simple, sans ajustement
