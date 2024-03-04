import json

def main():

    f = open('mapa-virtual.json')
    bd = json.load(f)
    f.close()


    ttl=""
    ttl += criaCidades(bd['cidades'],ttl)
    ttl += criaLigacoes(bd['ligacoes'],ttl)

    with open('output.ttl', 'w', encoding='utf-8') as output_file:
        output_file.write(ttl)
    
    concat_ttl_files('mapa.ttl', 'output.ttl', 'final.ttl')

def concat_ttl_files(file1_path, file2_path, output_file_path):
    with open(file1_path, 'r', encoding='utf-8') as file1:
        file1_content = file1.read()

    with open(file2_path, 'r', encoding='utf-8') as file2:
        file2_content = file2.read()

    concatenated_content = file1_content + file2_content

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(concatenated_content)



def criaCidades(data,ttl):
    for cid in data:   
        registo = f"""
###  http://rpcw.di.uminho.pt/2024/mapa#{cid['id']}
:{cid['id']} rdf:type owl:NamedIndividual ,
             :cidade ; 
    :pertenceDistrito :{cid['distrito'].replace(" ", "_")} ;
    :descrição "{cid['descrição'].replace(" ", "_")}" ;
    :id "{cid['id']}" ;
    :nome "{cid['nome'].replace(" ", "_")}" ;
    :população "{cid['população']}" .
"""
        ttl += registo
    return ttl

def criaLigacoes(data,ttl):
    for lig in data:   
        registo = f"""
###  http://rpcw.di.uminho.pt/2024/mapa#{lig['id']}
:{lig['id']} rdf:type owl:NamedIndividual ,
              :ligacao ;
     :temCidadeDestino :{lig['destino']} ;
     :temCidadeOrigem :{lig['origem']} ;
     :distancia "{lig['distância']}"^^xsd:float ;
     :idLigacao "{lig['id']}" .
"""
        ttl += registo
    return ttl

if __name__ == "__main__":
    main()