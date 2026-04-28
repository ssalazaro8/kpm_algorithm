def compute_failure_function(pattern):

    if pattern == "":
        raise ValueError("The pattern cannot be empty.")

    failure = [0] * len(pattern)
    t = 0  # current prefix length

    for i in range(1, len(pattern)):

        # move back if mismatch
        while t > 0 and pattern[i] != pattern[t]:
            t = failure[t - 1]

        # increase if match
        if pattern[i] == pattern[t]:
            t += 1

        failure[i] = t

    return failure