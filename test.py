def print_pattern(text):
    n = len(text)

    for i in range(n, 0, -1):
        spaces = " " * (n - i)
        mirrored_text = text[:i] + text[:i - 1][::-1]
        line = spaces + mirrored_text
        print(line.center(2 * n - 1))

# Example: Let's use "PYTHON" as the input text
input_text = "25258"
print_pattern(input_text)
