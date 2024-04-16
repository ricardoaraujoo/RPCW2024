from rdflib import OWL, Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import FOAF, XSD
import pprint
import json


f = open("cinema_copy.json", "r", encoding='utf-8')
bd = json.load(f)
f.close()

g = Graph()
g.parse("cinema.ttl", format="ttl")

cinema = Namespace("http://rpcw.di.uminho.pt/2024/cinema/")

for entrada in bd:
    g.add((URIRef(f"{cinema}{entrada['name'][0]}"), RDF.type, OWL.NamedIndividual))
    g.add((URIRef(f"{cinema}{entrada['name'][0]}"), RDF.type, cinema.Film))
    g.add((URIRef(f"{cinema}{entrada['name'][0]}"), cinema.title,  URIRef(f"entrada['name'][0]")))
    for d in entrada['director']:
        g.add((URIRef(f"{cinema}{d}"), RDF.type, OWL.NamedIndividual))
        g.add((URIRef(f"{cinema}{d}"), RDF.type, cinema.Director))
        g.add((URIRef(f"{cinema}{entrada['name'][0]}"), cinema.hasDirector, URIRef(f"{cinema}{d}")))
    for d in entrada['writer']:
        g.add((URIRef(f"{cinema}{d}"), RDF.type, OWL.NamedIndividual))
        g.add((URIRef(f"{cinema}{d}"), RDF.type, cinema.Writer))
        g.add((URIRef(f"{cinema}{entrada['name'][0]}"), cinema.hasWriter, URIRef(f"{cinema}{d}")))
    for d in entrada['musicComposer']:
        g.add((URIRef(f"{cinema}{d}"), RDF.type, OWL.NamedIndividual))
        g.add((URIRef(f"{cinema}{d}"), RDF.type, cinema.Musician))
        g.add((URIRef(f"{cinema}{entrada['name'][0]}"), cinema.hasComposer, URIRef(f"{cinema}{d}")))
    for d in entrada['actors']:
        g.add((URIRef(f"{cinema}{d}"), RDF.type, OWL.NamedIndividual))
        g.add((URIRef(f"{cinema}{d}"), RDF.type, cinema.Actor))
        g.add((URIRef(f"{cinema}{entrada['name'][0]}"), cinema.hasActor, URIRef(f"{cinema}{d}")))


print(len(g))
print(g.serialize())
