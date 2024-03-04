Quais as cidades de um determinado distrito?
SELECT ?cityName ?nomeCidade WHERE {
  ?cityName :pertenceDistrito :c7 .
  ?cityName :nome ?nomeCidade.
}

Distribuição de cidades por distrito?
SELECT ?city (COUNT(?cityName) AS ?count) WHERE {
  ?cityName :pertenceDistrito ?city .
}
GROUP BY ?city

Quantas cidades se podem atingir a partir do Porto?
33 (Viana)

Quais as cidades com população acima de um determinado valor?
SELECT ?city WHERE { 
  ?city :população ?populationString .
  BIND(xsd:integer(?populationString) AS ?population)
  FILTER(?population > 270841)
}
LIMIT 100