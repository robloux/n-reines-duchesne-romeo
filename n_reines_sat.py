import sys
from itertools import combinations
from pysat.solvers import Glucose3


def var(i, j, n):
    return i * n + j + 1


def au_plus_un(cases, n):
    return [[-var(*a, n), -var(*b, n)] for a, b in combinations(cases, 2)]


def cnf(n):
    clauses = []
    for k in range(n):
        clauses += au_plus_un([(k, j) for j in range(n)], n)
        clauses += au_plus_un([(i, k) for i in range(n)], n)
        clauses.append([var(k, j, n) for j in range(n)])
    for d in range(-n + 1, n):
        clauses += au_plus_un([(i, i - d) for i in range(n) if 0 <= i - d < n], n)
        clauses += au_plus_un([(i, d + n - 1 - i) for i in range(n) if 0 <= d + n - 1 - i < n], n)
    return clauses


n = int(sys.argv[1]) if len(sys.argv) > 1 else 8
with Glucose3(bootstrap_with=cnf(n)) as s:
    if s.solve():
        m = set(s.get_model())
        for i in range(n):
            print(" ".join("Q" if var(i, j, n) in m else "." for j in range(n)))
    else:
        print("Aucune solution")


# a faire encore
# - mettre les commentaires dans le code, c'est demande dans l'enonce
# - tester n = 1 et si on met n'importe quoi comme valeur
# - envoyer le lien github avant le 18 decembre
# - verifier qu'on a bien 92 solutions pour n = 8
# - ecrire les formules avec les symboles, genre Q(a) -> non Q(b) puis la version cnf
# - faire un readme et un requirements.txt avec python-sat
# - mesurer le temps pour n = 8, 16, 32
# - garder les resultats pour n = 4 et n = 8 comme exemples
# - expliquer pourquoi au moins une reine par ligne + au plus une = n reines
