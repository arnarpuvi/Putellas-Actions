"""
Nom: Arnau Putellas
Data creació: 8/1/2025
Última modificació: 9/1/2025
"""
from biblioteca import *
import pytest
@pytest.mark.parametrize("categoria, res_esperat", [
    ("novel·la",['El Quixot', 'Crim i Càstig']), # Test 1 amb la categoria "novel·la"
    ("ciència-ficció", ['1984'])]) # Test 2 amb la categoria "ciència-ficció"

def test_llibres_per_categoria(categoria, res_esperat):
    """
    Testeija la funció llibres_per_categoria per assegurar-se que retorna els llibres correctes per a cada categoria.
    """
    resultat = llibres_per_categoria(biblioteca, categoria) 
    assert resultat == res_esperat 


@pytest.mark.parametrize("llibre, res_esperat", [
    ("El Senyor dels Anells", [False]), # Test 1 amb el llibre "El Senyor dels Anells"
    ("1984", [True])]) # Test 2 amb el llibre "1984"

def esta_disponible(llibre, res_esperat):
    """
    Testeija la funció esta_disponible per assegurar-se que retorna si el llibre està disponible o no.
    """
    resultat = esta_disponible(biblioteca, llibre)
    assert resultat == res_esperat


@pytest.mark.parametrize("usuari, res_esperat", [
    ("Pere", ['True']), # Test 1 amb l'usuari "Pere"
    ("Joan", ['False'])]) # Test 2 amb l'usuari "Joan"

def usuari_te_prestecs(usuari, res_esperat):
    """
    Testeija la funció usuari_te_prestecs per assegurar-se que retorna si l'usuari té préstecs o no.
    """
    resultat = usuari_te_prestecs(biblioteca, usuari)
    assert resultat == res_esperat


@pytest.mark.parametrize("llibre, res_esperat", [
    ("El Senyor dels Anells", ['67']), # Test 1 amb el llibre "El Senyor dels Anells"
    ("Crim i Càstig", ['63'])]) # Test 2 amb el llibre "Crim i Càstig"

def dies_prestec(llibre, res_esperat):
    """
    Testeija la funció dies_prestec per assegurar-se que retorna els dies de préstec d'un llibre.
    """
    resultat = dies_prestec(biblioteca, llibre)
    assert resultat == res_esperat