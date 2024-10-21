# Tic-tac-toe for week 3

# Creative feature: 
# Any size of board

# Creative implementation: 
# Functional programming only using conditionals and lambda
# One line only.

(lambda f: f(f))(lambda f, w=int(input("Input the size of the board: ")):(lambda game:game(game, ['   '] * (w * w), 0))(lambda game, b, t: (print('\n' + '\n'.join(['|' + '|'.join(b[i * w:(i + 1) * w]) + '|' for i in range(w)]) + '\n'),any([all(s == b[i * w] != '   ' for s in b[i * w:(i + 1) * w]) for i in range(w)] + [all(s == b[i] != '   ' for s in b[i::w]) for i in range(w)] + [all(b[i * (w + 1)] == b[0] != '   ' for i in range(w))] + [all(b[(i + 1) * (w - 1)] == b[w - 1] != '   ' for i in range(w))]) and print(f"Player {['X', '0'][t % 2]} wins!") or (t == w * w and print("It's a tie!")) or ((p := [' X ', ' O '][t % 2], i := int(input(f'Player {p}, choose 0-{w * w - 1}: ')),b[i] == '   ' and game(game, b[:i] + [p] + b[i + 1:], t + 1)) or (print('Invalid move!'), game(game, b, t))))))