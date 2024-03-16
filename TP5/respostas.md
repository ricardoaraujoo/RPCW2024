Que filmes de uma curta metragem?



Que filmes de ação eu tenho?



Qual o elenco do filme X?

PREFIX schema: <http://schema.org/>
SELECT ?filme (GROUP_CONCAT(?ator; separator=", ") AS ?actors) WHERE {
  ?filme a schema:Movie ;
         dbo:starring ?ator .
} 
GROUP BY ?filme
LIMIT 500

X = Ca-bau-kan

PREFIX schema: <http://schema.org/>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbr: <http://dbpedia.org/resource/>

SELECT DISTINCT ?ator WHERE {
  dbr:Ca-bau-kan a schema:Movie ;
                 dbo:starring ?ator .
} LIMIT 500



Em que filmes atuou o ator X?

X=Lola_Amaria

PREFIX schema: <http://schema.org/>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbr: <http://dbpedia.org/resource/>

SELECT DISTINCT ?filme WHERE {
  dbr:Lola_Amaria a dbo:Person.
  ?filme a schema:Movie .
  ?filme dbo:starring dbr:Lola_Amaria.
} LIMIT 500
