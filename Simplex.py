import numpy as np

def simplex(c, A, b):
    m, n = A.shape

    
    tableau = np.zeros((m + 1, n + 1))
    tableau[:m, :n] = A
    tableau[:m, -1] = b
    tableau[-1, :n] = -c

    while True:
        if np.all(tableau[-1, :-1] >= 0):
            break

        entering = np.argmin(tableau[-1, :-1])

        if np.all(tableau[:-1, entering] <= 0):
            raise Exception("Problem is unbounded.")


        ratios = []
        for i in range(m):
            if tableau[i, entering] > 0:
                ratios.append(tableau[i, -1] / tableau[i, entering])
            else:
                ratios.append(np.inf)

        leaving = np.argmin(ratios)

        pivot = tableau[leaving, entering]
        tableau[leaving, :] /= pivot

        for i in range(m + 1):
            if i != leaving:
                tableau[i, :] -= tableau[i, entering] * tableau[leaving, :]


    solution = np.zeros(n)
    for j in range(n):
        col = tableau[:m, j]
        if np.count_nonzero(col) == 1 and np.isclose(col[np.nonzero(col)[0][0]], 1):
            solution[j] = tableau[np.nonzero(col)[0][0], -1]

    return solution, tableau[-1, -1]

# Example 
if __name__ == "__main__":
    c = np.array([3, 2, 0])
    A = np.array([[2, 1, 1],
                  [1, 2, 1],
                  [1, -1, 0]])
    b = np.array([6, 6, 1])

    solution, optimal_value = simplex(c, A, b)

    print("Optimal solution:", solution)
    print("Optimal value:", optimal_value)

    
