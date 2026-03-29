from Semana5.ejercicio2 import suma_ciclo, suma_recursiva

def test_suma_numeros():
    assert suma_ciclo(5) == 15, (
        "La suma usando ciclo es incorrecta."
    )
    assert suma_recursiva(5) == 15, (
        "La suma recursiva es incorrecta. "
        "Verifique el caso base."
    )

def test_resultados_iguales():
    assert suma_ciclo(10) == suma_recursiva(10), (
        "Ambas soluciones deben entregar el mismo resultado."
    )
