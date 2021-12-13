popA, popB, anos = int(input("")), int(input("")), 0
taxaB = 0.03
taxaA = 0.02
while (popB <= popA):
      popA = popA + (popA * taxaA)
      popB = popB + (popB * taxaB)
      anos+=1
print(format(anos))
                                     
    
                            
