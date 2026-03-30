from Semana5.ejercicio7 import ahorro_total_ciclo, ahorro_total_recursivo

def test_ahorro_total():
    ahorros = [200, 300, 150, 350]
    esperado = 1000
    assert ahorro_total_ciclo(ahorros) == esperado, (
        "La solución con ciclo no calcula correctamente el ahorro total."
    )
    assert ahorro_total_recursivo(ahorros) == esperado, (
        "La solución recursiva es incorrecta. "
        "Revise cómo se acumulan los valores de la lista."
    )

def test_ambas_soluciones_iguales():
    ahorros = [100, 100, 100]
    assert ahorro_total_ciclo(ahorros) == ahorro_total_recursivo(ahorros), (
        "Ambas soluciones deben producir el mismo resultado."
    )
