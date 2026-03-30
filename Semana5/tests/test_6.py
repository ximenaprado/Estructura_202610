from Semana5.ejercicio6 import total_ventas_ciclo, total_ventas_recursivo

def test_total_ventas():
    ventas = [1000, 2500, 1800, 3200]
    esperado = 8500
    assert total_ventas_ciclo(ventas) == esperado, (
        "La solución con ciclo no calcula correctamente el total de ventas."
    )
    assert total_ventas_recursivo(ventas) == esperado, (
        "La solución recursiva no suma correctamente los valores. "
        "Revise el caso base y la reducción de la lista."
    )

def test_resultados_coinciden():
    ventas = [500, 700, 800]
    assert total_ventas_ciclo(ventas) == total_ventas_recursivo(ventas), (
        "Ambas soluciones deben entregar el mismo total de ventas."
    )
