def sum(a: int, b: int) -> int:
    return a + b

def main():
    value_01 = int(input("Informe o valor 1: "))
    value_02 = int(input("Informe o valor 2: "))

    result = sum(value_01, value_02)

    print(f"O resultado é {result}")

if __name__ == "__main__":
    main()
