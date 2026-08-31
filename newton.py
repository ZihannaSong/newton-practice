def first_derivative(fun, x, epsilon=0.0001):
    """Estimate the first derivative of fun at x."""
    return (fun(x + epsilon) - fun(x - epsilon)) / (2 * epsilon)


def second_derivative(fun, x, epsilon=0.0001):
    """Estimate the second derivative of fun at x."""
    return (
        fun(x + epsilon)
        - 2 * fun(x)
        + fun(x - epsilon)
    ) / (epsilon ** 2)


def optimize(start, fun, tolerance=0.000001, max_iterations=100):
    """Minimize a one-dimensional function using Newton's method."""
    x_old = start

    for iteration in range(max_iterations):
        first = first_derivative(fun, x_old)
        second = second_derivative(fun, x_old)

        x_new = x_old - first / second

        if abs(x_new - x_old) < tolerance:
            return x_new

        x_old = x_new

    return x_old
