import matplotlib.pyplot as plt 
import numpy as np

def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col): #Verifica se é seguro colocar uma rainha no tabuleiro, verifica se não há outra rainha na mesma linha, mesma coluna ou na diagonal.
            return False
    return True

def solve_n_queens(n, board, col, solutions, max_solutions): #Encontra todas as configurações possíveis do tabuleiro, respeitando as regras do jogo
    if len(solutions) >= max_solutions:
        return

    if col >= n:
        solutions.append(board[:])
        return

    for row in range(n):
        if is_safe(board, row, col):
            board[col] = row
            solve_n_queens(n, board, col + 1, solutions, max_solutions)
            board[col] = -1  # Reset o backtracking

def nQueen(n, max_solutions):
    solutions = []
    solve_n_queens(n, [-1] * n, 0, solutions, max_solutions) # Máximo de soluções a serem exibidas, porque são muitas e a visualização do mat, não fica legal.
    return solutions

def plot_solution(n):
    max_solutions = 3  # Máximo de soluções a serem exibidas
    solutions = nQueen(n, max_solutions)
    if not solutions:
        print("Não há soluções para N =", n)
        return

    for idx, sol in enumerate(solutions, start=1):
        chessboard = np.zeros((n, n))
        for col, row in enumerate(sol):
            chessboard[row][col] = 1

        plt.subplot(len(solutions), 1, idx)
        plt.imshow(chessboard, cmap='binary')

        # Adicionar linhas e colunas do tabuleiro
        plt.grid(True, which='both', linestyle='-', linewidth=1, color='black')
        plt.xticks(np.arange(-0.5, n, 1), [])
        plt.yticks(np.arange(-0.5, n, 1), [])
        plt.xlim(-0.5, n-0.5)
        plt.ylim(n-0.5, -0.5)

        plt.title(f"Solução {idx}")
    
    plt.tight_layout()
    plt.show()

while True:
    n = input("Digite o número de rainhas (1 to 20) ou digite 'sair' para sair: ")
    if n.lower() == 'sair':
        break

    if n.isdigit():
        n = int(n)
        if 1 <= n <= 20:
            plot_solution(n)
        else:
            print("Por favor, escolha um número válido de rainhas (1 to 20).")
    else:
        print("Escolha errada! Por favor, escolha um número válido ou digite 'sair' para sair.")
