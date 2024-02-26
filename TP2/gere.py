import json

f = open('db.json')
bd = json.load(f)
f.close()

Objetos= set()

ttl = ""

for musica in bd:

    Objetos.add(musica['curso'])
    Objetos.add(musica['instrumentos'])

    registo =f"""
###  http://rpcw.di.uminho.pt/2024/musica#{musica['Id']}
<http://rpcw.di.uminho.pt/2024/musica#{musica['Id']}> rdf:type owl:NamedIndividual ,
                                                            <http://rpcw.di.uminho.pt/2024/TPC1/Musica> ;
                                                    <http://rpcw.di.uminho.pt/2024/TPC1/temCurso> <http://rpcw.di.uminho.pt/2024/TPC1/{musica['curso'].replace(" ", "_")}> ;
                                                    <http://rpcw.di.uminho.pt/2024/TPC1/temInstrumento> <http://rpcw.di.uminho.pt/2024/TPC1/{musica['instrumentos'].replace(" ", "_")}> ;
                                                    <http://rpcw.di.uminho.pt/2024/TPC1/anoCurso> "{musica['anoCurso']}"^^xsd:int ;
                                                    <http://rpcw.di.uminho.pt/2024/TPC1/dataNascimento> "{musica['dataNascimento']}"^^xsd:dateTime  ;
                                                    <http://rpcw.di.uminho.pt/2024/TPC1/id> "{musica['id']}"^^xsd:string ;
                                                    <http://rpcw.di.uminho.pt/2024/TPC1/nome> "{musica['nome']}"^^xsd:string ;
    """
    ttl += registo

for element in Objetos:
    obj = f"""
###  http://rpcw.di.uminho.pt/2024/musica#{element.replace(" ", "_")}
:{element.replace(" ", "_")} rdf:type owl:NamedIndividual .
"""
    ttl +=obj
    

print(ttl)