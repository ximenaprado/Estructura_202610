from semana5.Ejercicio2 import suma_ciclo, suma_recursiva


def test_suma_numeros_pequenos():
    """
    Caso simple: verifica que ambos métodos calculen bien la suma.
    """
    esperado = 15  # 1 + 2 + 3 + 4 + 5

    assert suma_ciclo(5) == esperado, (
        "La solución con ciclo no calcula correctamente "
        "la suma de los primeros N números."
    )

    assert suma_recursiva(5) == esperado, (
        "La solución recursiva no calcula correctamente "
        "la suma de los primeros N números. "
        "Revisa el caso base y la llamada recursiva."
    )


def test_ambas_soluciones_coinciden():
    """
    Ambas soluciones deben producir el mismo resultado.
    """
    n = 10

    assert suma_ciclo(n) == suma_recursiva(n), (
        "La solución con ciclo y la solución recursiva "
        "no producen el mismo resultado."
    )
