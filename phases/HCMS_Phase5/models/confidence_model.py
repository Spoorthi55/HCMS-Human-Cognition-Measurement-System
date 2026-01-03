def confidence_alignment(confidence, accuracy):
    """
    Measures mismatch between perceived confidence and actual performance.
    """

    alignment = 1 - abs(confidence - accuracy)
    return round(max(alignment, 0), 2)
