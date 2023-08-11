A = str(input("Voçê deseja cifrar ou decifrar uma mensagem? "))
A = A.lower()
Alfabeto = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWXYZàáãâéêóôõíúçÀÁÃÂÉÊÓÔÕÍÚÇ'
#Se o usuário decidiu codificar uma mensagem#
if A == 'cifrar':
    B = int(input("Digite 1 para criar um arquivo ou 2 para usar um arquivo existente "))
     #Se o usuário decidiu criar uma arquivo#
    if B == 1:
      Texto = str(input("Informe a mensagem a ser cifrada "))   
      #Definir a deslocação#   
      Deslocamento = int(input("Informe a rotação que voçê deseja implementar "))
      #Função para cifrar#  
      def cifrar(Texto):
        Cifra = ''
        for c in Texto:
          if c in Alfabeto:
            c_index = Alfabeto.index(c)
            Cifra += Alfabeto[(c_index + Deslocamento) % len(Alfabeto)]
          else:
            Cifra += c  
       #Criando um arquivo cifrado#
          with open('Cifrado.txt', 'w') as OP1:
           OP1.write(Cifra)
        print("O arquivo Cifrado.txt contendo sua mensagem codificada foi criado!")
      cifrar(Texto)
    #Se o usuário decidiu usar um arquivo existente#
    elif B == 2:
      print("Renomeie seu arquivo para 'Mensagem.txt'!")
      Texto = ''
      with open('Mensagem.txt','r') as OP2:
        Texto = OP2.read()
      #Definir a deslocação#   
      Deslocamento = int(input("Informe a rotação que voçê deseja implementar "))
      #Função para cifrar#   
      def cifrar(Texto):
        Cifra = ''
        for c in Texto:
          if c in Alfabeto:
            c_index = Alfabeto.index(c)
            Cifra += Alfabeto[(c_index + Deslocamento) % len(Alfabeto)]
          else:
            Cifra += c  
         #Criando um arquivo cifrado#
          with open('Cifrado.txt', 'w') as OP1:
           OP1.write(Cifra)
        print("O arquivo Cifrado.txt contendo sua mensagem codificada foi criado!")
      cifrar(Texto)     
    else:
      print("Comando não identificado")    
    #caso o usúario decida descifrar#   
elif A == 'decifrar':
  print('Certifique-se de que o arquivo a ser descriptografado está nomeado como "Cifrado.txt"')
  Texto = ''
  with open('Cifrado.txt','r') as OP3:
        Texto = OP3.read()
        #Definir a deslocação#   
        cont = int(input("Informe a quantidade de tentativas que voçê deseja realizar (OBS : as tentativas serão realizadas do 0 até o número inserido) "))
        Deslocamento = 0
        decifra = ''
        Sep = []
        def decifrar(Texto):
            global decifra
            for c in Texto:
             if c in Alfabeto:
                c_index = Alfabeto.index(c)
                decifra += Alfabeto[(c_index - Deslocamento) % len(Alfabeto)]      
             else:
                decifra += c 
          #Adicionando à lista para efetuar a separação#  
            Sep.append(decifra)
            decifra = ''
        while Deslocamento <= cont:
             decifrar(Texto)
             Deslocamento = Deslocamento + 1 
         #Trasformando a lista em string#  
             SepA = " - ".join(Sep)
             

            #Criando um arquivo decifrado#
             with open('Decifrado.txt', 'w') as OP4:
              OP4.write(SepA)            
        decifrar(Texto)
        print("Um arquivo chamado 'Decifrado.txt' foi criado com as tentativas de deslocamento ")  
else:
  print("Comando não identificado! Tente usar 'cifrar' ou 'decifrar' ")
