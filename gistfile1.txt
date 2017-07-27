import random

def jogar():
  print("***JOGANDO FORCA***")
  banco = open('palavras.txt', 'r')
  palavras = []
  for linha in banco:
      linha = linha.strip()
      palavras.append(linha)
  n_aleatorio = random.randrange(0,len(palavras))
  palavra_secreta = palavras[n_aleatorio].upper()
  #palavras = ['Torrada','Tucano','LapTop','Python','Brasil']
  #random.shuffle(palavras)
  #palavra_secreta = random.choice(palavras)
  #palavra_secreta = 'Torrada'#.upper()
  letras_acertadas = []
  #acertou = None
  erros = 0
  enforcou = False
  acertou = False
  ganho = False
  for letra in palavra_secreta:
      letras_acertadas.append('_ ')
  #print(letras_acertadas)
  
  def imprimir():
    for l in letras_acertadas:
      print(l, end = '')
      
  imprimir()
  
  while enforcou == False and ganho == False:
    #print('jogando')
    chute = input("\nDigite a letra:\n")
    chute = chute.strip()
    #chute = chute.upper()
    index = 0
    for letra in palavra_secreta:
      if chute.upper() == letra.upper():
        acertou = True
        letras_acertadas[index] = letra
        #print(chute)
        print('\nletra {} na posição {} \n'.format(letra,(index+1)))
        imprimir()
        #for l in letras_acertadas:
        #  print(l, end = '')
      index = index + 1
      
    if not '_ ' in letras_acertadas:
      print('\n\nVocê ganhou\n\n')
      print('Sua pontuação foi {}'.format(10 - erros))
      break
      
      
    if acertou == False:
      erros = erros + 1
      print('Você errou\n')
      print('faltam:')
      print(8 - erros)
      print('tentativas\n\n')
      imprimir()
      #print(letras_acertadas)
      if erros == 8:
        print('\nFim de jogo \n\n\n')
        print('a palavra era:')
        print(palavra_secreta, end='\n\n\n')
        enforcou = True
    acertou = False 
      #if acertou == False:
        #print('voce errou')
      
  banco.close()
if __name__ == '__main__':
  jogar()
