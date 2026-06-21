import pandas as pd

def test_calcul_commande():
    # Test unitaire : vérifier que la formule de commande est correcte
    prediction_journaliere = 30
    stock_actuel = 50
    # On a besoin de stock pour 7 jours (30 * 7 = 210). On a 50 en stock. On doit commander 160.
    commande = (prediction_journaliere * 7) - stock_actuel
    
    assert commande == 160, "Erreur dans l'algorithme de calcul de la commande !"