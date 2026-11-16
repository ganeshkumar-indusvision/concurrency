def a():
    print("a start")
    b()
    print("a end")          # ❌ never runs

def b():
    print("b start")
    raise ValueError("boom")
    print("b end")          # ❌ never runs

def main():
    print("main start")
    # try:
    a()
    print("after a")    # ❌ never runs
    # except ValueError as e:
        # print("caught:", e) # ✅ runs
    print("main continues") # ✅ runs

main()