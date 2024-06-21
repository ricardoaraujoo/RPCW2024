import xml.etree.ElementTree as ET

f = open("biblia.xml")
bd = ET.parse(f)
f.close()

root = bd.getroot()

people = {}
ttl = ""

for p in root.iter('p'):
    # id: sex
    people[p[0].text] = p.find('sex').text
    
for p in root.iter('p'):
    id = p[0].text
    name = p.find('namegiven').text
    
    parents = p.findall('parent')
    mother, dad = "", ""
    
    for parent in parents:
        parent_id = parent.attrib['ref']
        if people[parent_id] == 'F':
            mother = parent_id
        else:
            dad = parent_id
    
    register = f"""
###  http://rpcw.di.uminho.pt/2024/familia#{id}
    :{id} rdf:type owl:NamedIndividual ,
                 :Pessoa ;
           :nome "{name}" .
"""
    if dad != "":
        register += f"    :{id} :temdad :{dad} .\n"
    if mother != "":
        register += f"    :{id} :temmother :{mother} .\n"
    
    
    ttl += register
            
f = open("familia.ttl", "a")
f.write(ttl)
f.close()