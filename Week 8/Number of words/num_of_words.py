import sys, functools
print(
    len(
        set(
            functools.reduce(
                lambda x, y: x + y,
                map(
                    lambda x: x.split(),
                    sys.stdin
                )
            )
        )
    )
)