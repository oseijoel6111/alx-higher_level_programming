#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    count = len(args)

    if count == 0:
        print("0 arguments.")
    else:
        plural = "s" if count > 1 else ""
        print(f"{count} argument{plural}{':' if count > 0 else '.'}")

        for i, arg in enumerate(args):
            print(f"{i + 1}: {arg}")
