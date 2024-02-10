import json

f = open('plantas.json')
bd = json.load(f)
f.close()

Objetos= set()

ttl = ""

for planta in bd:

    Objetos.add(planta['Estado'])
    Objetos.add(planta['Implantação'])
    Objetos.add(planta['Gestor'])
    Objetos.add(planta['Espécie'])

    registo =f"""
###  http://rpcw.di.uminho.pt/2024/Plantas#{planta['Id']}
<http://rpcw.di.uminho.pt/2024/Plantas#{planta['Id']}> rdf:type owl:NamedIndividual ,
                                                            <http://rpcw.di.uminho.pt/2024/TPC1/Planta> ;
                                                    <http://rpcw.di.uminho.pt/2024/TPC1/temEspécie> <http://rpcw.di.uminho.pt/2024/TPC1/{planta['Espécie'].replace(" ", "_")}> ;
                                                    <http://rpcw.di.uminho.pt/2024/TPC1/temEstado> <http://rpcw.di.uminho.pt/2024/TPC1/{planta['Estado']}> ;
                                                    <http://rpcw.di.uminho.pt/2024/TPC1/temGestor> <http://rpcw.di.uminho.pt/2024/TPC1/{planta['Gestor'].replace(" ", "_")}> ;
                                                    <http://rpcw.di.uminho.pt/2024/TPC1/temImplantação> <http://rpcw.di.uminho.pt/2024/TPC1/{planta['Implantação'].replace(" ", "_")}> ;
                                                    <http://rpcw.di.uminho.pt/2024/TPC1/Caldeira> "{planta['Caldeira']}"^^xsd:boolean ;
                                                    <http://rpcw.di.uminho.pt/2024/TPC1/Código_de_rua> {planta['Código de rua']} ;
                                                    <http://rpcw.di.uminho.pt/2024/TPC1/Data_de_Plantação> "{planta['Data de Plantação']}"^^xsd:dateTime ;
                                                    <http://rpcw.di.uminho.pt/2024/TPC1/Data_de_actualização> "{planta['Data de actualização']}"^^xsd:dateTime ;
                                                    <http://rpcw.di.uminho.pt/2024/TPC1/Freguesia> "{planta['Freguesia'].replace(" ", "_")}" ;
                                                    <http://rpcw.di.uminho.pt/2024/TPC1/Rua> "{planta['Rua'].replace(" ", "_")}" ;
                                                    <http://rpcw.di.uminho.pt/2024/TPC1/Id> {planta['Id']} ;
                                                    <http://rpcw.di.uminho.pt/2024/TPC1/Local> "{planta['Local'].replace(" ", "_")}" ;
                                                    <http://rpcw.di.uminho.pt/2024/TPC1/Nome_Científico> "{planta['Nome Científico'].replace(" ", "_")}" ;
                                                    <http://rpcw.di.uminho.pt/2024/TPC1/Número_de_Registo> {planta['Número de Registo']} ;
                                                    <http://rpcw.di.uminho.pt/2024/TPC1/Número_de_intervenções> "{planta['Número de intervenções']}"^^xsd:int ;
                                                    <http://rpcw.di.uminho.pt/2024/TPC1/Origem> "{planta['Origem']}" ;
                                                    <http://rpcw.di.uminho.pt/2024/TPC1/Tutor> "{planta['Tutor']}"^^xsd:boolean .
    """
    ttl += registo

for element in Objetos:
    obj = f"""
###  http://rpcw.di.uminho.pt/2024/Plantas#{element.replace(" ", "_")}
:{element.replace(" ", "_")} rdf:type owl:NamedIndividual .
"""
    ttl +=obj
    

print(ttl)