# Testanto o ABC(Abstract Basic Classes)
from collections.abc import MutableSequence

class MinhaListinhaMutavel(MutableSequence):
    pass

objetoValidado = MinhaListinhaMutavel()
print(objetoValidado)