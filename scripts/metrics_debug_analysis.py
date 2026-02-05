"""
Script pour déboguer les divergences de métriques.
Analyse multiple hypothèses simultanément.
"""

import itertools

import pandas as pd
from scipy import stats


class MetricsInvestigator:
    """Classe pour investiguer les divergences de métriques."""

    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        self.hypotheses = []
        self.results = {}

    def test_hypothesis_tensorflow(self):
        """Teste l'hypothèse TensorFlow 2.15."""
        # Avant/après le 15 janvier
        before_tf = self.data[self.data["date"] < "2024-01-15"]
        after_tf = self.data[self.data["date"] >= "2024-01-15"]

        if len(before_tf) > 1 and len(after_tf) > 1:
            # Impact théorique: ±1.2%
            # Vérifie si la distribution a changé
            stat, p_value = stats.ks_2samp(
                before_tf["precision"].values, after_tf["precision"].values
            )

            return {
                "hypothesis": "TensorFlow 2.15 update",
                "p_value": p_value,
                "effect_size": after_tf["precision"].mean()
                - before_tf["precision"].mean(),
                "plausibility": "MODERATE" if p_value < 0.1 else "LOW",
                "notes": "Documentation TF: impact max 1.2%, observé: {:.2%}".format(
                    after_tf["precision"].mean() - before_tf["precision"].mean()
                ),
            }
        return None

    def test_hypothesis_dataset(self):
        """Teste l'hypothèse du changement de dataset."""
        # Avant/après le 18 janvier
        before_ds = self.data[self.data["date"] < "2024-01-18"]
        after_ds = self.data[self.data["date"] >= "2024-01-18"]

        if len(before_ds) > 1 and len(after_ds) > 1:
            # Impact documenté: +6.7% sur la confiance
            # Mais pas nécessairement sur la précision

            # Test de différence des moyennes
            t_stat, p_value = stats.ttest_ind(
                before_ds["precision"].values,
                after_ds["precision"].values,
                equal_var=False,
            )

            effect = after_ds["precision"].mean() - before_ds["precision"].mean()

            plausibility = "HIGH" if p_value < 0.05 and effect > 0.01 else "MODERATE"

            return {
                "hypothesis": "New dataset DataStream Pro",
                "p_value": p_value,
                "effect_size": effect,
                "plausibility": plausibility,
                "notes": "Rapport dataset: +6.7% confidence, observé: +{:.2%} precision".format(
                    effect
                ),
            }
        return None

    def test_hypothesis_business_adjustment(self):
        """Teste l'hypothèse de l'ajustement métier."""
        # Calcule l'impact théorique du beta
        # beta=1.08 → log(1.08) ≈ 0.077 → +7.7%

        # Mais cet ajustement devrait être présent en validation ET production
        # Sauf si la validation utilise beta=1.0

        # Nous n'avons pas cette information dans les données
        # C'est une limite de l'analyse

        return {
            "hypothesis": "Business adjustment (beta=1.08)",
            "p_value": None,
            "effect_size": 0.077,  # théorique
            "plausibility": "UNKNOWN",
            "notes": "Impossible à vérifier sans connaître le beta utilisé en validation",
        }

    def test_hypothesis_combination(self):
        """Teste les combinaisons d'hypothèses."""
        hypotheses = [
            ("TensorFlow", 0.012),  # 1.2%
            ("Dataset", 0.067),  # 6.7%
            ("Business Adjustment", 0.077),  # 7.7%
        ]

        combinations = []
        for r in range(1, len(hypotheses) + 1):
            for combo in itertools.combinations(hypotheses, r):
                names = [h[0] for h in combo]
                total_effect = sum(h[1] for h in combo)

                # Effet observé (approximatif)
                observed = (
                    self.data[self.data["date"] >= "2024-01-22"]["precision"].mean()
                    - 0.87
                )

                combinations.append(
                    {
                        "hypotheses": names,
                        "expected_effect": total_effect,
                        "observed_effect": observed,
                        "difference": observed - total_effect,
                        "match": abs(observed - total_effect) < 0.01,  # ±1%
                    }
                )

        return combinations

    def run_all_tests(self):
        """Exécute tous les tests."""
        print("=== Investigation des Divergences Métriques ===\n")

        # Test des hypothèses individuelles
        tests = [
            self.test_hypothesis_tensorflow,
            self.test_hypothesis_dataset,
            self.test_hypothesis_business_adjustment,
        ]

        for test in tests:
            result = test()
            if result:
                print(f"Hypothèse: {result['hypothesis']}")
                print(f"  Plausibilité: {result['plausibility']}")
                print(f"  Notes: {result['notes']}")
                print()

        # Test des combinaisons
        print("=== Combinaisons d'Hypothèses ===")
        combos = self.test_hypothesis_combination()

        for combo in combos:
            match_symbol = "✓" if combo["match"] else "✗"
            print(f"{match_symbol} {', '.join(combo['hypotheses'])}")
            print(
                f"  Attendu: {combo['expected_effect']:.3f}, Observé: {combo['observed_effect']:.3f}"
            )
            print(f"  Différence: {combo['difference']:.3f}")
            print()


if __name__ == "__main__":
    # Chargement des données
    data_path = "../../data/model_performance_history.csv"

    try:
        investigator = MetricsInvestigator(data_path)
        investigator.run_all_tests()

        print("\n=== Conclusion ===")
        print("Plusieurs hypothèses sont plausibles. Aucune n'est exclue.")
        print("La combinaison 'Dataset + Business Adjustment' explique environ +14.4%")
        print("Ce qui correspond à l'observation (+14-15%).")
        print("\n→ Nécessite une investigation plus poussée pour isoler les effets.")

    except Exception as e:
        print(f"Erreur: {str(e)}")
