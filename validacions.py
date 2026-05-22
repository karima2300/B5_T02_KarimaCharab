"""
Mòdul de validacions: Funcions per validar diferents tipus de dades.

Aquest mòdul conté funcions per validar emails, telèfons,
DNIs, contrasenyes i altres dades comunes.
"""

import re
from datetime import datetime

def validar_email(email):
    """
    Valida si un email té el format correcte.
    
    Args:
        email (str): Adreça de correu electrònic a validar
        
    Returns:
        bool: True si l'email és vàlid, False en cas contrari
        
    Example:
        >>> validar_email("usuari@example.com")
        True
        >>> validar_email("email_invalid")
        False
    """
    patro = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patro, email))

def validar_telefon(telefon):
    """
    Valida si un número de telèfon té el format correcte.
    Accepta formats amb codi de país o sense.
    
    Args:
        telefon (str): Número de telèfon a validar
        
    Returns:
        bool: True si el telèfon és vàlid, False en cas contrari
        
    Example:
        >>> validar_telefon("612345678")
        True
        >>> validar_telefon("+34612345678")
        True
    """
    # Sense codi de país: 9 dígits
    patro1 = r'^[0-9]{9}$'
    # Amb codi de país: +34 9 dígits
    patro2 = r'^\+\d{1,3}[0-9]{9}$'
    return bool(re.match(patro1, telefon)) or bool(re.match(patro2, telefon))

def validar_dni(dni):
    """
    Valida si un DNI espanyol és correcte.
    
    Args:
        dni (str): DNI a validar (8 números + lletra)
        
    Returns:
        bool: True si el DNI és vàlid, False en cas contrari
        
    Example:
        >>> validar_dni("12345678Z")
        True
    """
    if not re.match(r'^[0-9]{8}[A-Z]$', dni):
        return False
    
    lletres = "TRWAGMYFPDXBNJZSQVHLCKE"
    numero = int(dni[:8])
    lletra_calculada = lletres[numero % 23]
    
    return dni[8] == lletra_calculada

def validar_contrasenya(contrasenya):
    """
    Valida si una contrasenya és prou forta.
    Requereix: mínim 8 caràcters, una majúscula, una minúscula, un número.
    
    Args:
        contrasenya (str): Contrasenya a validar
        
    Returns:
        dict: Diccionari amb el resultat de la validació
        
    Example:
        >>> validar_contrasenya("Password123")
        {'valida': True, 'errors': []}
    """
    errors = []
    
    if len(contrasenya) < 8:
        errors.append("La contrasenya ha de tenir almenys 8 caràcters")
    
    if not re.search(r'[A-Z]', contrasenya):
        errors.append("La contrasenya ha de tenir almenys una majúscula")
    
    if not re.search(r'[a-z]', contrasenya):
        errors.append("La contrasenya ha de tenir almenys una minúscula")
    
    if not re.search(r'[0-9]', contrasenya):
        errors.append("La contrasenya ha de tenir almenys un número")
    
    return {
        'valida': len(errors) == 0,
        'errors': errors
    }

def validar_data(data_str, format_data='%Y-%m-%d'):
    """
    Valida si una data té el format correcte.
    
    Args:
        data_str (str): Data en format string
        format_data (str): Format esperat (default: '%Y-%m-%d')
        
    Returns:
        bool: True si la data és vàlida, False en cas contrari
        
    Example:
        >>> validar_data("2024-12-25")
        True
        >>> validar_data("25/12/2024", "%d/%m/%Y")
        True
    """
    try:
        datetime.strptime(data_str, format_data)
        return True
    except ValueError:
        return False

def validar_codi_postal(codi_postal):
    """
    Valida si un codi postal espanyol és correcte (5 dígits).
    
    Args:
        codi_postal (str): Codi postal a validar
        
    Returns:
        bool: True si el codi postal és vàlid, False en cas contrari
    """
    return bool(re.match(r'^[0-9]{5}$', codi_postal))

class Validador:
    """
    Classe que agrupa tots els mètodes de validació.
    """
    
    @staticmethod
    def validar_tot(dades):
        """
        Valida múltiples camps a la vegada.
        
        Args:
            dades (dict): Diccionari amb les dades a validar
                Claus possibles: email, telefon, dni, contrasenya
            
        Returns:
            dict: Diccionari amb els resultats de cada validació
        """
        resultats = {}
        
        if 'email' in dades:
            resultats['email'] = validar_email(dades['email'])
        
        if 'telefon' in dades:
            resultats['telefon'] = validar_telefon(dades['telefon'])
        
        if 'dni' in dades:
            resultats['dni'] = validar_dni(dades['dni'])
        
        if 'contrasenya' in dades:
            resultats['contrasenya'] = validar_contrasenya(dades['contrasenya'])
        
        return resultats