#Felipe Gabriel de Marchi Corsi | SC3037347
pinos_caidos = list(map(int, input().split()))
pontos_totais = 0
#Rodadas 1 a 9 - Regulares
i = 0
for j in range(9):
  if pinos_caidos[i] == 10:
    print("X", "_", "|", end=' ')
    pontos_totais += 10 + pinos_caidos[i + 1] + pinos_caidos[i + 2]
    i += 1
  elif pinos_caidos[i] + pinos_caidos[i + 1] == 10:
    print(pinos_caidos[i], "/", "|", end=' ')
    pontos_totais += pinos_caidos[i] + pinos_caidos[i + 1] + pinos_caidos[i + 2]
    i += 2
  else:
    print(pinos_caidos[i], pinos_caidos[i + 1], "|", end=' ')
    pontos_totais += pinos_caidos[i] + pinos_caidos[i + 1]
    i += 2

#Rodada 10 - Irregular
if pinos_caidos[i] == 10:
  print("X", end=' ')
  pontos_totais += 10
  if pinos_caidos[i + 1] == 10:
    print("X", end=' ')
    pontos_totais += 10
  else:
    print(pinos_caidos[i + 1], end=' ')
    pontos_totais += pinos_caidos[i + 1]
  if pinos_caidos[i + 2] == 10:
    print("X")
    pontos_totais += 10
  else:
    print(pinos_caidos[i + 2])
    pontos_totais += pinos_caidos[i + 2]
  
elif pinos_caidos[i] + pinos_caidos[i + 1] == 10:
  print(pinos_caidos[i], "/", end=' ')
  pontos_totais += pinos_caidos[i] + pinos_caidos[i + 1]
  if pinos_caidos[i + 2] == 10:
    print("X")
    pontos_totais += 10
  else:
    print(pinos_caidos[i + 2])
    pontos_totais += pinos_caidos[i + 2]
else:
  print(pinos_caidos[i], pinos_caidos[i + 1])
  pontos_totais += pinos_caidos[i] + pinos_caidos[i + 1]
print(pontos_totais)