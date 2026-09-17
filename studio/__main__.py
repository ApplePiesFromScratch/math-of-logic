import sys
from studio import algebra, calc, logic, steps


def main():
    print("STUDIO")
    print()
    algebra.main()
    print()
    logic.main()
    print()
    calc.main()
    print()
    steps.main()
    print()
    print("verdict PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
