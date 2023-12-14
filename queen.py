# Importar as bibliotecas necessárias
import tkinter as tk
from tkinter import messagebox

# Função para verificar se é seguro colocar uma rainha em uma posição específica
def is_safe(board, row, col):
    for i in range(col):
        # Verifica se há uma rainha na mesma linha ou diagonal
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

# Função para resolver o problema das N Rainhas usando backtracking
def solve_n_queens(n, board, col, solutions):
    if col >= n:
        solutions.append(board[:])  # Adiciona a solução válida à lista de soluções
        return True

    res = False
    for row in range(n):
        if is_safe(board, row, col):
            board[col] = row
            res = solve_n_queens(n, board, col + 1, solutions) or res
            board[col] = -1  # Resetar para -1 quando backtracking
    return res

# Função para desenhar o tabuleiro com as rainhas
def draw_queens(canvas, n, board):
    canvas.delete("all")  # Limpar o canvas antes de desenhar

    # Configurações do tabuleiro
    square_size = 300 // 8  # Tamanho do tabuleiro 8x8
    colors = ["red", "green", "blue", "teal", "orange", "purple", "brown", "black"] #As cores das rainhas

    # Desenha o tabuleiro 8x8
    for row in range(8):
        for col in range(8):
            x1, y1 = col * square_size, row * square_size
            x2, y2 = x1 + square_size, y1 + square_size
            color = "white" if (row + col) % 2 == 0 else "lightgray"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    # Desenha as rainhas com cores diferentes
    for col, row in enumerate(board[:n]):
        if row != -1:
            x1, y1 = col * square_size, row * square_size
            x2, y2 = x1 + square_size, y1 + square_size
            queen_color = colors[col % len(colors)]  # Alterna cores para cada rainha
            canvas.create_text(x1 + square_size // 2, y1 + square_size // 2, text="♛", fill=queen_color, font=('Arial', square_size // 2))

# Função para encontrar todas as soluções do problema das N Rainhas
def n_queens(n):
    solutions = []
    solve_n_queens(8, [-1] * 8, 0, solutions)  # Resolver para um tabuleiro 8x8
    return solutions

# Função para mostrar a solução na interface gráfica
def show_solution(canvas):
    try:
        n = int(entry.get())  # Obtém o número de rainhas digitado pelo usuário
        if n <= 0 or n > 8:
            messagebox.showinfo("Info", "Por favor, escolha um número válido de rainhas (1 a 8).")
            return

        solutions = n_queens(n)  # Encontra as soluções para o problema
        if not solutions:
            messagebox.showinfo("Info", "Não há solução para o tabuleiro de tamanho " + str(n))
        else:
            for solution in solutions:
                draw_queens(canvas, n, solution)  # Desenha a solução no canvas
                root.update()
                root.after(500)  # Delay para mostrar cada solução por 500 milissegundos
    except ValueError:
        messagebox.showinfo("Info", "Por favor, insira um número válido.")

# Interface gráfica
root = tk.Tk()
root.title("Problema das N Rainhas")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label = tk.Label(frame, text="Digite o número de rainhas (1 a 8):")
label.pack()

entry = tk.Entry(frame)
entry.pack()

canvas = tk.Canvas(root, width=300, height=300, bg='white')
canvas.pack()

solve_button = tk.Button(frame, text="Mostrar Solução", command=lambda: show_solution(canvas))
solve_button.pack()

root.mainloop()
