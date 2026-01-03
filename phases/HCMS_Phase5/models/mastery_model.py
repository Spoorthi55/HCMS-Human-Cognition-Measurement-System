def compute_mastery(accuracy, attempts):
    """
    Mastery is not raw accuracy.
    Low attempts + correct ≠ mastery.
    """

    if attempts == 0:
        return 0.3  # lucky guess risk

    mastery = (accuracy * 0.7) + (min(attempts / 5, 1) * 0.3)
    return round(mastery, 2)
