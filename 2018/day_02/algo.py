from itertools import combinations

mots_a_comparer = (
        "rateau", "château", "chauffe", "berger", "pomme", "trois",
        "manger", "pompe", "travail", "python", "banane", "django"
        )


def mots_proches(mots):
    """Trouver les mots ayant une seule lettre qui diffère entre eux et situées au même indice."""
    # Boucler sur les paires de mots ayant la même longueur :
    for mot1, mot2 in [pair for pair in combinations(mots, 2) if len(pair[0]) == len(pair[1])]:
        # Trouver les indices des différences :
        differences = [(i, c1, c2) for i, (c1, c2) in enumerate(zip(mot1, mot2)) if c1 != c2]
        if len(differences) == 1:  # Vérifier qu'il n'y ait qu'une seule différence
            index_diff, lettre1, lettre2 = differences[0]  # Répartir éléments de la liste dans des varibles diverses
            lettres_communes = "".join(c1 for c1, c2 in zip(mot1, mot2) if c1 == c2)
            # Consttuction de la chaîne de caractères à retourner :
            return (f"'{mot1}' et '{mot2}' ont pour lettres communes '{lettres_communes}'\n"
                    f"Les lettres qui diffèrent sont '{lettre1}' et '{lettre2}', situées à l'index {index_diff}.")


print(mots_proches(mots_a_comparer))
