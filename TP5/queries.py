import json
import requests

# Define the DBpedia SPARQL endpoint
sparql_endpoint = "http://dbpedia.org/sparql"

# Define the SPARQL query
sparql_query = """
PREFIX schema: <http://schema.org/>
SELECT DISTINCT ?filme ?direct ?writer ?musicComp ?ator ?name WHERE {
  ?filme a schema:Movie ;
  dbo:director ?direct ;
 dbo:musicComposer ?musicComp ;
dbo:writer ?writer;
dbp:name ?name;
 dbo:starring ?ator .
FILTER (LANG(?name) = 'en') .
} LIMIT 500
"""

# Define the headers
headers = {
    "Accept": "application/sparql-results+json"
}

# Define the parameters
params = {
    "query": sparql_query,
    "format": "json"
}

# Send the SPARQL query using requests
response = requests.get(sparql_endpoint, params=params, headers=headers)


# Check if the request was successful
if response.status_code == 200:
    results = response.json()
    filmes = {}
    for result in results["results"]["bindings"]:
        film_uri = result['filme']['value']
        if film_uri not in filmes:
            filmes[film_uri] = {
                "name": [],
                "director": [],
                "writer": [],
                "musicComposer": [],
                "actors": [],
                "uri": film_uri
            }
        filmes[film_uri]["director"].append(result['direct']['value'])
        filmes[film_uri]["writer"].append(result['writer']['value'])
        filmes[film_uri]["actors"].append(result['ator']['value'])
        filmes[film_uri]["name"].append(result['name']['value'])
        filmes[film_uri]["musicComposer"].append(result['musicComp']['value'])

    resultado = []
    # Remove duplicates
    for film in filmes.values():
        film["director"] = list(set(film["director"]))
        film["writer"] = list(set(film["writer"]))
        film["actors"] = list(set(film["actors"]))
        film["name"] = list(set(film["name"]))
        film["musicComposer"] = list(set(film["musicComposer"]))
        resultado.append({
            "name": film["name"],
            "director": film["director"],
            "writer": film["writer"],
            "musicComposer": film["musicComposer"],
            "actors": film["actors"],
            "uri": film["uri"]
        })
        
    f = open("cinema.json", "w", encoding='utf-8')
    json.dump(resultado, f, indent=4)
    f.close()

else:
    print("Error:", response.status_code)
    print(response.text)