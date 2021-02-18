#-*- coding:utf-8 -*-

def Votação():
    TotalVotos = 0.0
    Total_A = 0.0
    Total_B = 0.0
    
    i = 1
    while(i>0 and i<1000):
        print("Digite a quantidade de votos do candidato A: ")
        cand_A = float (input ())
        print("Digite a quantidade de votos do candidato B: ")
        cand_B = float (input ())
        
        Total_A = Total_A + cand_A
        Total_B = Total_B + cand_B
        TotalVotos = Total_A + Total_B
        
        perc_A = Total_A / TotalVotos * 100
        perc_B = Total_B / TotalVotos * 100
        
        print("")
        print("")
        
        print("Total de Votos do Candidato A: %.0f" % Total_A)
        print("Porcentagem de votos do Candidato A: %.2f%%" % perc_A)
                
        print("Total de Votos do Candidato B: %.0f" % Total_B)
        print("Porcentagem de votos do Candidato B: %.2f%%" % perc_B)
        
        print("Votos Totais: %.0f" % TotalVotos)
        
        print("")
        print("")
        
        print("Digite 1 para continuar ou 0 para sair: ")
        i = int(input())
        
        
    print("Total de Votos do Candidato A: %.0f" % Total_A)
    print("Porcentagem de votos do Candidato A: %.2f%%" % perc_A)
                
    print("Total de Votos do Candidato B: %.0f" % Total_B)
    print("Porcentagem de votos do Candidato B: %.2f%%" % perc_B)
        
    print("Votos Totais: %.0f" % TotalVotos)  

Votação()    
     
        
        
        
        
        
    
        

        