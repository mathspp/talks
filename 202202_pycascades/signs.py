def sign_standard_if_elif_else(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def sign_conditional_conditional(x):
    return 1 if x > 0 else -1 if x < 0 else 0


def sign_conditional_conditional_2(x):
    return 0 if x == 0 else 1 if x > 0 else -1


def sign_conditional_conditional_falsy(x):
    return 0 if not x else 1 if x > 0 else -1


def sign_if_else_conditional_expression(x):
    if x == 0:
        return 0
    else:
        return 1 if x > 0 else -1


def sign_if0_conditional_expression(x):
    if x == 0:
        return 0

    return 1 if x > 0 else -1


def sign_if0_divide_abs(x):
    if x == 0:
        return 0

    return int(abs(x) // x)  # round(abs(x) // x)


def sign_conditional_dict(x):
    return 0 if x == 0 else {True: 1, False: -1}[x > 0]


def sign_conditional_int_bool(x):
    if x < 0:
        return -1

    return int(bool(x))


def sign_conditional_list(x):
    return 0 if x == 0 else [-1, 1][x > 0]


def sign_list(x):
    return [-1, 0, 1][(x >= 0) + (x > 0)]


def sign_boolean_emoji(x):
    return (x > 0) - (x < 0)


def sign_structural_match(x):
    match x > 0, x < 0:
        case True, False: return 1
        case False, True: return -1
        case False, False: return 0


def sign_match(x):
    match x:
        case x if x > 0: return 1
        case x if x < 0: return -1
        case _: return 0


def sign_canned_if_elif_else(x):
    if x > 0: return 1
    if x < 0: return -1
    return 0


if __name__ == "__main__":
    import timeit
    from functools import partial

    funcs = [
        sign_boolean_emoji,
        sign_canned_if_elif_else,
        sign_conditional_conditional,
        sign_conditional_conditional_2,
        sign_conditional_conditional_falsy,
        sign_conditional_dict,
        sign_conditional_int_bool,
        sign_conditional_list,
        sign_if0_conditional_expression,
        sign_if0_divide_abs,
        sign_if_else_conditional_expression,
        sign_list,
        sign_match,
        sign_standard_if_elif_else,
        sign_structural_match,
    ]

    for func in funcs:
        for x, out in [(10, 1), (4.5, 1), (0, 0), (-2, -1), (-3.14, -1)]:
            assert func(x) == out

    expressions = [
        "f(3.14)",
        "f(-2.78)",
        "f(0)",
        "f(1_000_000_000_000)",
        "f(-1_000_000_000_000)",
    ]

    # Parameters for timeit.repeat.
    num = 1000
    rep = 500

    def repeat(expr, **kwargs):
        return min(
            timeit.repeat(
                expr, number=num, repeat=rep, **kwargs
            )
        )

    timings = {func.__name__: {expr: [] for expr in expressions} for func in funcs}
    # Spread the timings across like this, to make sure that every function/expression
    # combo is timed in the most similar conditions, across the board.
    # Using timeit.repeat with a large number of repetitions would mean that some
    # functions could end up being tested in more favourable CPU conditions than
    # other functions, leading to too many imbalances in the code.
    for _ in range(rep):
        for expr in expressions:
            for func in funcs:
                globals_ = {"f": func}
                timings[func.__name__][expr].append(
                    timeit.timeit(expr, number=num, globals=globals_)
                )

    timings = [
        [min(times[expr]) for expr in expressions] + [func]
        for func, times in timings.items()
    ]
    timings = sorted(timings, key=lambda t: sum(t[:-1]))
    fastest = timings[0][0]

    # Reporting
    try:
        from rich.console import Console
        from rich.table import Table
    except ImportError:
        print("Pretty reporting disabled. `pip install rich`.")
        print(timings)
        import sys
        sys.exit()

    table = Table(title="Timing results.")
    table.add_column("Function", justify="left")
    table.add_column("+f", justify="right")
    table.add_column("-f", justify="right")
    table.add_column("0", justify="right")
    table.add_column("+L", justify="right")
    table.add_column("-L", justify="right")
    # Set the first row
    references = timings[0][:-1]
    table.add_row(timings[0][-1], *["-%" for _ in references])
    # Set all other rows:
    for *times, name in timings[1:]:
        entries = []
        for time, ref in zip(times, references):
            delta = 100 * (time / ref - 1)
            style = "bold green" if delta < 0 else "red"
            entries.append(f"[{style}]{delta:+6.1f}%[/]")
        table.add_row(name, *entries)

    console = Console()
    console.print(table)
