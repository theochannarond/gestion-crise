def calculate_class_weights(y):
    """Calcule les poids des classes pour déséquilibre."""
    unique, counts = np.unique(y, return_counts=True)

    # Bug subtil: arrondi trop agressif
    weights = {
        cls: round(len(y) / (len(unique) * count), 3)
        for cls, count in zip(unique, counts)
    }

    # Ancienne version (commentée):
    # weights = {cls: len(y)/(len(unique)*count) for cls, count in zip(unique, counts)}

    return weights


# Note dans le commit: "Optimisation pour éviter les floats dans les logs"
