from src.failure_function import compute_failure_function

def kmp_search(text, pattern):

    if text == "":
        raise ValueError("The text cannot be empty.")

    if pattern == "":
        raise ValueError("The pattern cannot be empty.")

    failure = compute_failure_function(pattern)
    s = 0  # number of matched characters

    for i in range(len(text)):

        # fallback using failure function
        while s > 0 and text[i] != pattern[s]:
            s = failure[s - 1]

        # advance if match
        if text[i] == pattern[s]:
            s += 1

        # full match found
        if s == len(pattern):
            return True

    return False


def print_kmp_result(text, pattern):
    found = kmp_search(text, pattern)

    print("\nText:   ", text)
    print("Pattern:", pattern)

    if found:
        print("Result: YES, the pattern is a substring.\n")
    else:
        print("Result: NO, the pattern is not a substring.\n")