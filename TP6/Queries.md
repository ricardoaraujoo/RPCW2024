1- Quantos filmes existem no repositorio?

PREFIX : <http://rpcw.di.uminho.pt/2024/cinema/>

select (count(?film) as ?nfilmes) where {
  ?film a :Film .
}

2-  Qual a distribuição de filmes por ano de lançamento

PREFIX : <http://rpcw.di.uminho.pt/2024/cinema/>

select ?date (COUNT(?film) as ?count) where {
  ?film a :Film ;
        :releaseDate ?date
} group by ?date

3- Qual a distribuição de filmes por género?

PREFIX : <http://rpcw.di.uminho.pt/2024/cinema/>

select ?genre (count(?film) as ?count) where {
	?film a :Film ;
          :hasGenre ?genre .
} group by ?genre

4- Em que filmes participou o ator "Burt Reynolds"?

PREFIX : <http://rpcw.di.uminho.pt/2024/cinema/>

select ?actor ?film where {
	?film a :Film ;
          :hasActor ?actor .
	?actor :name "Burt Reynolds" .   
}


5- Produz uma lista de realizadores com o seu nome e o número de filmes que realizou

PREFIX : <http://rpcw.di.uminho.pt/2024/cinema/>

select ?director (COUNT(?film) as ?nfilmes) where {
	?film a :Film ;
          :hasDirector ?director.
} group by ?director

6- Qual o título dos livros que aparecem associados aos filmes?
Não há relação de livro e filmes