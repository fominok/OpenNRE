import hashlib
from SPARQLWrapper import SPARQLWrapper, JSON
from collections import namedtuple
from nltk.tokenize import sent_tokenize

Hit = namedtuple('Hit', 'abstract year')


def get_hits():
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery("""
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        select distinct ?x ?abstract ?year where {
            ?x dbo:type <http://dbpedia.org/resource/Public_company> .
            ?x dbo:foundingYear ?year .
            ?x dbo:abstract ?abstract .
            FILTER (langMatches(lang(?abstract),"en"))
        } limit 10
        """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    hits = []
    for r in results['results']['bindings']:
        hit = Hit(abstract=r['abstract']['value'], year=r['year']['value'])
        hits.append(hit)

    return hits


# def build_data_entry(sent, val):
#     res = {
#         "head": {
#             "type": "UNK",
#             "word": "audits",
#             "id": "c54379fa058a9ad836b60a32f9ceb5bd"
#         },
#         "tail": {
#             "type": "UNK",
#             "word": "waste",
#             "id": "cb15e32f389b7af9b285a63ca1044651"
#         },
#         "relation": "Message-Topic",
#         "sentence": "The most common audits were about waste and recycling."
#     }

#     idh = hashlib.md5(item['e1'].encode('utf8')).hexdigest()


if __name__ == '__main__':
    print(get_hits())
