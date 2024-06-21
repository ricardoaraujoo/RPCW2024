import json

with open("aval-alunos.json", encoding="utf-8") as f:
    try:
        bd = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
        raise

ttl = """@prefix : <http://rpcw.di.uminho.pt/2024/avaliacao/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <http://rpcw.di.uminho.pt/2024/avaliacao/> .

<http://rpcw.di.uminho.pt/2024/avaliacao> rdf:type owl:Ontology .

#################################################################
#    Object Properties
#################################################################

###  http://rpcw.di.uminho.pt/2024/avaliacao#temTPC
:temTPC rdf:type owl:ObjectProperty ;
        rdfs:domain :Aluno ;
        rdfs:range :TPC .


###  http://rpcw.di.uminho.pt/2024/avaliacao#temExame
:temExame rdf:type owl:ObjectProperty ;
                rdfs:subPropertyOf owl:topObjectProperty ;
                rdfs:domain :Aluno ;
                rdfs:range :Exame .


#################################################################
#    Data properties
#################################################################

###  http://rpcw.di.uminho.pt/2024/avaliacao#tp
:tp rdf:type owl:DatatypeProperty ;
        rdfs:domain :Aluno ;
        rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/avaliacao#projeto
:projeto rdf:type owl:DatatypeProperty ;
        rdfs:domain :Aluno ;
        rdfs:range xsd:int .


###  http://rpcw.di.uminho.pt/2024/avaliacao#idAluno
:idAluno rdf:type owl:DatatypeProperty ;
                rdfs:domain :Aluno ;
                rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/avaliacao#nomeAluno
:nomeAluno rdf:type owl:DatatypeProperty ;
        rdfs:domain :Aluno ;
        rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/avaliacao#curso
:curso rdf:type owl:DatatypeProperty ;
        rdfs:domain :Aluno ;
        rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/avaliacao#nota
:nota rdf:type owl:DatatypeProperty ;
        rdfs:domain :Exames ;
        rdfs:range xsd:float .


###  http://rpcw.di.uminho.pt/2024/avaliacao#exameNormal
:exameNormal rdf:type owl:DatatypeProperty ;
        rdfs:domain :Exames ;
        rdfs:range xsd:int .


###  http://rpcw.di.uminho.pt/2024/avaliacao#exameRecurso
:exameRecurso rdf:type owl:DatatypeProperty ;
        rdfs:domain :Exames ;
        rdfs:range xsd:int .


###  http://rpcw.di.uminho.pt/2024/avaliacao#exameEspecial
:exameEspecial rdf:type owl:DatatypeProperty ;
        rdfs:domain :Exames ;
        rdfs:range xsd:int .


#################################################################
#    Classes
#################################################################

###  http://rpcw.di.uminho.pt/2024/avaliacao#Aluno
:Aluno rdf:type owl:Class .


###  http://rpcw.di.uminho.pt/2024/avaliacao#TPC
:TPC rdf:type owl:Class .


###  http://rpcw.di.uminho.pt/2024/avaliacao#Exames
:Exames rdf:type owl:Class .


#################################################################
#    Individuals
#################################################################

"""


for aluno in bd["alunos"]:
    ttl+=f"""

###  http://rpcw.di.uminho.pt/2024/avaliacao#{aluno["idAluno"]}
:{aluno["idAluno"]} rdf:type owl:NamedIndividual ;
        :idAluno "{aluno["idAluno"]}" ;
        :nome "{aluno["nome"]}" ;
        :curso "{aluno["curso"]}" ;
        :projeto {aluno["projeto"]} ;
        """
    for tpc in aluno["tpc"]:
        ttl+=f""":temTPC :{tpc['tp']}_{aluno['idAluno']} ;
        """
    if "exames" in aluno:
        exames = aluno["exames"]
        ttl += f""":temExame :exames_{aluno["idAluno"]} .

"""

for aluno in bd["alunos"]:
    for tpc in aluno["tpc"]:
        ttl+=f"""

### http://rpcw.di.uminho.pt/2024/avaliacao#{tpc['tp']}_{aluno["idAluno"]}
:{tpc['tp']}_{aluno["idAluno"]} rdf:type owl:NamedIndividual ;
    :tp "{tpc['tp']}" ;
    :nota {tpc['nota']} .
"""

for aluno in bd["alunos"]:
    ttl += f"""

###  http://rpcw.di.uminho.pt/2024/avaliacao#exames_{aluno["idAluno"]}
:exames_{aluno["idAluno"]} rdf:type owl:NamedIndividual ;
    """
    for i, exame in enumerate(aluno["exames"]):
        if exame == "normal":
            ttl += f":exameNormal {aluno['exames'].get(exame)} "
        if exame == "especial":
            ttl += f":exameEspecial {aluno['exames'].get(exame)} "
        if exame == "recurso":
            ttl += f":exameRecurso {aluno['exames'].get(exame)} "
        if i < len(aluno["exames"])-1:
            ttl += ";\n\t"
    ttl += f""".
"""


# Salve o conteúdo TTL em um arquivo
with open("avaliacao01.ttl", "w", encoding="utf-8") as output_file:
    output_file.write(ttl)

print("Conteúdo guardado.")

