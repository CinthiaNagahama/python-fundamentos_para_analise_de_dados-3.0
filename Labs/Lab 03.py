# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import os
import random

# Board (tabuleiro)
board = ['''
>>>>>>>>>>Hangman<<<<<<<<<<
+---+
|   |
    |
    |
    |
    |
=========''', '''
>>>>>>>>>>Hangman<<<<<<<<<<
+---+
|   |
O   |
    |
    |
    |
=========''', '''
>>>>>>>>>>Hangman<<<<<<<<<<
+---+
|   |
O   |
|   |
    |
    |
=========''', '''
>>>>>>>>>>Hangman<<<<<<<<<<
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''
>>>>>>>>>>Hangman<<<<<<<<<<
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''
>>>>>>>>>>Hangman<<<<<<<<<<
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''
>>>>>>>>>>Hangman<<<<<<<<<<
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:
  # Método Construtor
  def __init__(self, word):
    self.word = word
    self.correct_guessed_letters = set()
    self.wrong_guessed_letters = set()

  # Método para adivinhar a letra
  def guess(self, letter):
    if letter in self.word:
      self.correct_guessed_letters.add(letter)
    else:
      self.wrong_guessed_letters.add(letter)

	# Método para verificar se o jogo terminou
  def hangman_over(self):
    return len(self.wrong_guessed_letters) >= 6

	# Método para verificar se o jogador venceu
  def hangman_won(self):
    return sorted(set(self.word)) == sorted(self.correct_guessed_letters)   

	# Método para não mostrar a letra no board
  def hide_word(self):
    aux = ""

    for letter in self.word:
      if letter in self.correct_guessed_letters:
        aux += letter
      else:
        aux += "_"
    return aux

	# Método para checar o status do game e imprimir o board na tela
  def print_game_status(self):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(board[len(self.wrong_guessed_letters)])
    print("\nPalavra: ", self.hide_word())
    print("\nLetras erradas:\n", *self.wrong_guessed_letters)
    print("\nLetras corretas:\n", *self.correct_guessed_letters)

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
  with open("palavras.txt", "r") as file:
    words = file.readlines()

  return random.choice(words).strip()

# Função Main - Execução do Programa
def main():

	# Objeto
  game = Hangman(rand_word())

  # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
  while(not game.hangman_over() and not game.hangman_won()):
    # Verifica o status do jogo
    game.print_game_status()
    game.guess(input("Digite uma letra: "))

  game.print_game_status()
	# De acordo com o status, imprime mensagem na tela para o usuário
  if game.hangman_won():
    print ('\nParabéns! Você venceu!!')
  else:
    print ('\nGame over! Você perdeu.')
    print ('A palavra era ' + game.word)
		
  print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()