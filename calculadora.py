"""
Mòdul calculadora: Proporciona funcions matemàtiques bàsiques.

Aquest mòdul conté funcions per realitzar operacions aritmètiques
com ara suma, resta, multiplicació, divisió i potència.
"""

def sumar(a, b):
    """
    Retorna la suma de dos números.
    
    Args:
        a (float): Primer número
        b (float): Segon número
        
    Returns:
        float: La suma de a i b
        
    Example:
        >>> sumar(5, 3)
        8
    """
    return a + b

def restar(a, b):
    """
    Retorna la resta de dos números.
    
    Args:
        a (float): Primer número
        b (float): Segon número
        
    Returns:
        float: La resta de a i b (a - b)
        
    Example:
        >>> restar(10, 4)
        6
    """
    return a - b

def multiplicar(a, b):
    """
    Retorna la multiplicació de dos números.
    
    Args:
        a (float): Primer número
        b (float): Segon número
        
    Returns:
        float: El producte de a i b
        
    Example:
        >>> multiplicar(4, 5)
        20
    """
    return a * b

def dividir(a, b):
    """
    Retorna la divisió de dos números.
    
    Args:
        a (float): Numerador
        b (float): Denominador
        
    Returns:
        float: La divisió de a entre b
        
    Raises:
        ValueError: Si b és zero
        
    Example:
        >>> dividir(10, 2)
        5.0
    """
    if b == 0:
        raise ValueError("No es pot dividir per zero")
    return a / b

def potencia(base, exponent):
    """
    Retorna la potència d'un número.
    
    Args:
        base (float): Número base
        exponent (float): Exponent
        
    Returns:
        float: base elevat a exponent
        
    Example:
        >>> potencia(2, 3)
        8
    """
    return base ** exponent

class Calculadora:
    """
    Classe Calculadora que encapsula les operacions matemàtiques.
    
    Attributes:
        historial (list): Llista que emmagatzema les operacions realitzades
    """
    
    def __init__(self):
        """
        Inicialitza una nova calculadora amb l'historial buit.
        """
        self.historial = []
    
    def afegir_operacio(self, operacio, resultat):
        """
        Afegeix una operació a l'historial.
        
        Args:
            operacio (str): Descripció de l'operació realitzada
            resultat (float): Resultat de l'operació
        """
        self.historial.append({
            'operacio': operacio,
            'resultat': resultat
        })
    
    def mostrar_historial(self):
        """
        Retorna l'historial complet d'operacions.
        
        Returns:
            list: Llista de diccionaris amb l'historial d'operacions
        """
        return self.historial
    
    def netejar_historial(self):
        """
        Neteja tot l'historial d'operacions.
        """
        self.historial = []