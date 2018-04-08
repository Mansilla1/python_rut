# Generador de rut con python

## Uso
```python
import rut

# obtener el digito verificador de un rut en particular
rut.digito_verificador(1) # obtiene el digito verificador del rut "1"

# generara lista de rut
rut.genera_rut(cantidad=10, inicio=10000, csv=False) # genera una lista de 10 rut con inicio en 10000
```

Los ruts a generar son autoincrementables a partir del valor entregado, en el ejemplo se entrega el valor 10000, ese indica el inicio.
