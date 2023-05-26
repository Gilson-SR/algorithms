def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    counter = 0

    for start, final in permanence_period:
        if not isinstance(start, int) or not isinstance(final, int):
            return None

        if start <= target_time <= final:
            counter += 1

    return counter
