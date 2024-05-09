#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

dir(hidden_4)
in_order = sorted(dir(hidden_4))
for name in in_order:
    if (name[0] != "_" and name[0][0] != "_"):
        print("{}".format(name))
    else:
        continue
