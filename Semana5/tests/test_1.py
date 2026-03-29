from semana5.Ejercicio1 import contar_ciclo, contar_recursivo

def test_contar_hasta_n():
    esperado = [1, 2, 3, 4, 5]

    assert contar_ciclo(5) == esperado, (
        "La versión con ciclo no genera correctamente la secuencia."
    )

    assert contar_recursivo(5) == esperado, (
        "La versión recursiva no genera correctamente la secuencia. "
        "Revisa el caso base."
    )
