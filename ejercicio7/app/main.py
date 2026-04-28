"""
Función que calcula el descuento de un precio
"""

def calcular_precio_final(precio, descuento):
    """
    Args:
        precio(float): Precio que se indica
        descuento(int): descuento en porcentaje
    
    Returns:
        float: precio final con el descuento
    """
    precioFinal = precio * (descuento/100)
    return precioFinal