def update_mastery(old, correct, confidence):
    lr = 0.1  # learning rate

    if correct:
        delta = lr * (confidence / 5)
    else:
        delta = -lr * (confidence / 5)

    new = old + delta
    return max(0.0, min(1.0, new))