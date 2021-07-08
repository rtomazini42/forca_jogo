import random
vidas = 8

def jogar():
  print("***JOGANDO FORCA***")
  print("Escolha o nivel:\n1-Fácil\n2-médio\n3-dificil")
  nivel = input("nivel:")
  nivel = int(nivel)
  if(nivel == 1):
    vidas = 10
  if(nivel == 2):
    vidas = 8
  if(nivel == 3):
    vidas = 5
  if(nivel > 3):
    vidas = 3 
  print("Você tem {} vidas".format(vidas))
  banco = open('palavras.txt', 'r')
  palavras = []
  for linha in banco:
      linha = linha.strip()
      palavras.append(linha)
  n_aleatorio = random.randrange(0,len(palavras))
  palavra_secreta = palavras[n_aleatorio].upper()
  letras_acertadas = []
  erros = 0
  enforcou = False
  acertou = False
  ganho = False
  for letra in palavra_secreta:
      letras_acertadas.append('_ ')
  
  def imprimir():
    for l in letras_acertadas:
      print(l, end = '')
      
  imprimir()
  
  while enforcou == False and ganho == False:
    chute = input("\nDigite a letra:\n")
    chute = chute.strip()
    index = 0
    for letra in palavra_secreta:
      if chute.upper() == letra.upper():
        acertou = True
        letras_acertadas[index] = letra
        print('\nletra {} na posição {} \n'.format(letra,(index+1)))
        imprimir()
      index = index + 1    
    if not '_ ' in letras_acertadas:
      print('\n\nVocê ganhou\n\n')
      print('Sua pontuação foi {}'.format(10 - erros))
      break
    if acertou == False:
      erros = erros + 1
      print('Você errou\n')
      print('faltam:' , end=' ')
      print(vidas - erros, end='')
      print(' tentativas\n\n')
      imprimir()
      if erros == vidas:
        print('\nFim de jogo \n\n\n')
        print('a palavra era:')
        print(palavra_secreta, end='\n\n\n')
        enforcou = True
    acertou = False 

      
  banco.close()
if __name__ == '__main__':
  jogar()
