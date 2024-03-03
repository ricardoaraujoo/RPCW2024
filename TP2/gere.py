import json

def main():

    f = open('db.json')
    bd = json.load(f)
    f.close()


    ttl=""
    ttl += criaInstrumentos(bd['instrumentos'],ttl)
    ttl += criaCursos(bd['cursos'],ttl)
    ttl += criaAlunos(bd['alunos'],ttl)

    with open('output.ttl', 'w', encoding='utf-8') as output_file:
        output_file.write(ttl)
    
    concat_ttl_files('musica.ttl', 'output.ttl', 'final.ttl')

def concat_ttl_files(file1_path, file2_path, output_file_path):
    with open(file1_path, 'r', encoding='utf-8') as file1:
        file1_content = file1.read()

    with open(file2_path, 'r', encoding='utf-8') as file2:
        file2_content = file2.read()

    concatenated_content = file1_content + file2_content

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(concatenated_content)

def criaInstrumentos(data,ttl):
    for inst in data:   
        registo = f"""
###  http://rpcw.di.uminho.pt/2024/musica#{inst['#text'].replace(" ", "_")}
:{inst['#text'].replace(" ", "_")} rdf:type owl:NamedIndividual ,
          :Instrumento ;
          :designacaoInstrumento "{inst['#text'].replace(" ", "_")}" ;
          :idInstrumento "{inst['id']}" .
"""
        ttl += registo
    return ttl

def criaCursos(data,ttl):
    for curso in data:   
        registo = f"""
###  http://rpcw.di.uminho.pt/2024/musica#{curso['id']}
:{curso['id']} rdf:type owl:NamedIndividual ,
     :Curso ;
     :temInstrumentoCurso :{curso['instrumento']['#text'].replace(" ", "_")} ;
     :designacao "{curso['designacao'].replace(" ", "_")}" ;
     :duracao "{curso['duracao']}"^^xsd:int ;
     :idCurso "{curso['id']}" .
"""
        ttl += registo
    return ttl

def criaAlunos(data,ttl):
    for aluno in data:   
        registo = f"""
###  http://rpcw.di.uminho.pt/2024/musica#{aluno['id']}
:{aluno['id']} rdf:type owl:NamedIndividual ,
       :Musica ;
       :temCurso :{aluno['curso']} ;
       :temInstrumento :{aluno['instrumento'].replace(" ", "_")} ;
       :anoCurso "{aluno['anoCurso']}"^^xsd:int ;
       :dataNascimento "{aluno['dataNasc']}"^^xsd:dateTime ;
       :id "{aluno['id']}" ;
       :nome "{aluno['nome'].replace(" ", "_")}" .
"""
        ttl += registo
    return ttl

if __name__ == "__main__":
    main()