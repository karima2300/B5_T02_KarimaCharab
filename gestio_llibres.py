"""
Mòdul de gestió de llibres: Permet gestionar una col·lecció de llibres.

Aquest mòdul proporciona classes i funcions per gestionar
una biblioteca de llibres amb operacions CRUD.
"""

class Llibre:
    """
    Classe que representa un llibre.
    
    Attributes:
        titol (str): Títol del llibre
        autor (str): Autor del llibre
        any (int): Any de publicació
        isbn (str): Codi ISBN del llibre
        disponible (bool): Indica si el llibre està disponible
    """
    
    def __init__(self, titol, autor, any, isbn):
        """
        Inicialitza un nou llibre.
        
        Args:
            titol (str): Títol del llibre
            autor (str): Autor del llibre
            any (int): Any de publicació
            isbn (str): Codi ISBN del llibre
        """
        self.titol = titol
        self.autor = autor
        self.any = any
        self.isbn = isbn
        self.disponible = True
    
    def __str__(self):
        """
        Retorna una representació en string del llibre.
        
        Returns:
            str: Representació del llibre
        """
        return f"{self.titol} - {self.autor} ({self.any})"
    
    def prestar(self):
        """
        Marca el llibre com a prestat.
        
        Returns:
            bool: True si s'ha pogut prestar, False si no estava disponible
        """
        if self.disponible:
            self.disponible = False
            return True
        return False
    
    def retornar(self):
        """
        Marca el llibre com a disponible.
        """
        self.disponible = True
    
    def obtenir_info(self):
        """
        Obté tota la informació del llibre.
        
        Returns:
            dict: Diccionari amb les dades del llibre
        """
        return {
            'titol': self.titol,
            'autor': self.autor,
            'any': self.any,
            'isbn': self.isbn,
            'disponible': self.disponible
        }


class Biblioteca:
    """
    Classe que representa una biblioteca amb col·lecció de llibres.
    
    Attributes:
        nom (str): Nom de la biblioteca
        llibres (list): Llista de llibres de la biblioteca
    """
    
    def __init__(self, nom):
        """
        Inicialitza una nova biblioteca.
        
        Args:
            nom (str): Nom de la biblioteca
        """
        self.nom = nom
        self.llibres = []
    
    def afegir_llibre(self, llibre):
        """
        Afegeix un llibre a la biblioteca.
        
        Args:
            llibre (Llibre): Llibre a afegir
            
        Returns:
            bool: True si s'ha afegit correctament
        """
        self.llibres.append(llibre)
        return True
    
    def eliminar_llibre(self, isbn):
        """
        Elimina un llibre per ISBN.
        
        Args:
            isbn (str): ISBN del llibre a eliminar
            
        Returns:
            bool: True si s'ha eliminat, False si no s'ha trobat
        """
        for llibre in self.llibres:
            if llibre.isbn == isbn:
                self.llibres.remove(llibre)
                return True
        return False
    
    def cercar_per_titol(self, titol):
        """
        Cerca llibres per títol.
        
        Args:
            titol (str): Títol a cercar
            
        Returns:
            list: Llista de llibres que coincideixen
        """
        resultats = []
        for llibre in self.llibres:
            if titol.lower() in llibre.titol.lower():
                resultats.append(llibre)
        return resultats
    
    def cercar_per_autor(self, autor):
        """
        Cerca llibres per autor.
        
        Args:
            autor (str): Autor a cercar
            
        Returns:
            list: Llista de llibres de l'autor
        """
        resultats = []
        for llibre in self.llibres:
            if autor.lower() in llibre.autor.lower():
                resultats.append(llibre)
        return resultats
    
    def llistar_llibres_disponibles(self):
        """
        Llista tots els llibres disponibles.
        
        Returns:
            list: Llista de llibres disponibles
        """
        return [llibre for llibre in self.llibres if llibre.disponible]
    
    def obtenir_total_llibres(self):
        """
        Retorna el nombre total de llibres.
        
        Returns:
            int: Nombre de llibres a la biblioteca
        """
        return len(self.llibres)
