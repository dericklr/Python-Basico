while True:
 n= int(input("Numero: "))
 for i in range(1,11):
  print(n ,"X",i,"=" ,n*i)
 print("-" *15)
 encerra= "e"
 t= input("Aperte qualquer tecla para continuar\nAperte e para encerrar: ")
 if t==encerra:
    print("Programa encerrado!")
    break
   
