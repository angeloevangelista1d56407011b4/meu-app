from main import sum

def test_sum():
    expected = 10
    result = sum(2, 8)

    assert(result == expected), "Eh esperado que o resultado seja 10 quano a entrada for 2 e 8"
