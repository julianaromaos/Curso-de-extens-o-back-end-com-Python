votos={
    "CandidatoA" :"",
    "CandidatoB": ""
}
candA=0
candB= 0
for i in range(5):
    nome=input("Em qual candidato irá votar?")
    if nome =="CandidatoA":
        candA +=1
    if nome=="CandidatoB":
        candB +=1
votos["CandidatoA"]= candA

votos["CandidatoB"]=candB
print(votos.items())
