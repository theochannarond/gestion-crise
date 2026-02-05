"""
Script pour vérifier la cohérence des métriques entre différentes implémentations.
"""

import os
import sys

import numpy as np
import pandas as pd
from scipy import stats

# Ajout du chemin pour importer le module de calcul
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def analyze_metric_discrepancy(validation_metrics, production_metrics, dates):
    """
    Analyse la divergence entre métriques validation et production.

    Returns:
        dict: Résultats de l'analyse statistique
    """
    if len(validation_metrics) != len(production_metrics):
        raise ValueError("Les tableaux doivent avoir la même longueur")

    discrepancies = production_metrics - validation_metrics

    # Test statistique: la divergence est-elle significative?
    t_stat, p_value = stats.ttest_1samp(discrepancies, 0.0)

    # Test de normalité des divergences (si assez de points)
    if len(discrepancies) > 3:
        try:
            shapiro_stat, shapiro_p = stats.shapiro(discrepancies)
            is_normal = shapiro_p > 0.05
        except:
            is_normal = None
            shapiro_p = None
    else:
        is_normal = None
        shapiro_p = None

    # Calcul des intervalles de confiance
    mean_diff = np.mean(discrepancies)
    std_diff = np.std(discrepancies, ddof=1)
    n = len(discrepancies)

    if n > 1:
        ci_low = mean_diff - 1.96 * std_diff / np.sqrt(n)
        ci_high = mean_diff + 1.96 * std_diff / np.sqrt(n)
    else:
        ci_low = ci_high = None

    return {
        "mean_discrepancy": mean_diff,
        "std_discrepancy": std_diff,
        "n_observations": n,
        "t_statistic": t_stat,
        "p_value": p_value,
        "is_significant": p_value < 0.05,
        "is_normal_distribution": is_normal,
        "shapiro_p_value": shapiro_p,
        "confidence_interval_95": (ci_low, ci_high) if ci_low is not None else None,
        "max_discrepancy": np.max(np.abs(discrepancies))
        if len(discrepancies) > 0
        else 0,
    }


def load_and_preprocess_data(filepath):
    """Charge et prétraite les données de comparaison."""
    df = pd.read_csv(filepath)

    # Conversion des dates
    df["date"] = pd.to_datetime(df["date"])

    # Filtre pour le modèle churn_v3 et métrique precision
    precision_data = df[
        (df["model"] == "churn_v3") & (df["metric"] == "precision")
    ].copy()

    # Tri par date
    precision_data = precision_data.sort_values("date")

    return precision_data


def run_consistency_checks():
    """Exécute les vérifications de cohérence."""
    print("=== Vérification Cohérence Métriques ===\n")

    try:
        # Chargement des données
        data_path = os.path.join("..", "..", "data", "detailed_metrics_comparison.csv")
        precision_data = load_and_preprocess_data(data_path)

        if len(precision_data) == 0:
            print("Aucune donnée de précision trouvée pour churn_v3")
            return

        print(
            f"Données analysées : {len(precision_data)} points de {precision_data['date'].min().date()} à {precision_data['date'].max().date()}\n"
        )

        # Analyse statistique
        results = analyze_metric_discrepancy(
            precision_data["validation_value"].values,
            precision_data["production_value"].values,
            precision_data["date"].values,
        )

        # Affichage des résultats
        print("Résultats de l'analyse :")
        print(f"  Écart moyen : {results['mean_discrepancy']:.4f}")
        print(f"  Écart-type : {results['std_discrepancy']:.4f}")
        print(f"  p-value : {results['p_value']:.6f}")

        if results["is_significant"]:
            print("  → Écart STATISTIQUEMENT SIGNIFICATIF (p < 0.05)")
        else:
            print("  → Écart non significatif statistiquement")

        if results["confidence_interval_95"]:
            ci_low, ci_high = results["confidence_interval_95"]
            print(f"  Intervalle de confiance 95% : [{ci_low:.4f}, {ci_high:.4f}]")

        print(f"  Maximum absolu : {results['max_discrepancy']:.4f}")

        # Analyse temporelle
        print("\n=== Analyse Temporelle ===")

        # Avant/Après 18 janvier (nouveau dataset)
        cutoff_date = pd.Timestamp("2024-01-18")
        before = precision_data[precision_data["date"] < cutoff_date]
        after = precision_data[precision_data["date"] >= cutoff_date]

        if len(before) > 0 and len(after) > 0:
            mean_before = before["difference"].mean()
            mean_after = after["difference"].mean()

            print(f"Avant 18/01 (n={len(before)}) : écart moyen = {mean_before:.4f}")
            print(f"Après 18/01 (n={len(after)}) : écart moyen = {mean_after:.4f}")
            print(f"Changement : {mean_after - mean_before:.4f}")

            # Test de différence des moyennes
            if len(before) > 1 and len(after) > 1:
                t_stat, p_val = stats.ttest_ind(
                    before["difference"].values,
                    after["difference"].values,
                    equal_var=False,
                )
                print(f"Test de différence : p = {p_val:.4f}")
                if p_val < 0.05:
                    print("  → Différence SIGNIFICATIVE après le 18/01")

        # Recommandations
        print("\n=== Recommandations ===")
        if results["is_significant"]:
            print("1. Investiguer la cause de la divergence significative")
            print("2. Vérifier la cohérence des pipelines validation/production")
            print("3. Examiner les différences de préprocessing")
        else:
            print("1. Surveiller la tendance (peut être un faux négatif)")
            print("2. Vérifier la puissance statistique (taille d'échantillon)")

    except FileNotFoundError:
        print(f"Fichier non trouvé : {data_path}")
    except Exception as e:
        print(f"Erreur lors de l'analyse : {str(e)}")


if __name__ == "__main__":
    run_consistency_checks()
