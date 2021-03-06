import json
import os
from dateutil import parser

from SPARQLWrapper import SPARQLWrapper, JSON

# Constants for SPARQL request to DBPedia
sparql = SPARQLWrapper("http://dbpedia.org/sparql")

endpointLimit = 10000
limit = 30000

prefixes = """
prefix dbo: <http://dbpedia.org/ontology/>
prefix dbp: <http://dbpedia.org/property/>

"""

queries = [
"""
select distinct (str(?companyName) as ?companyNameStr) (str(?year) as ?yearStr) (str(?abstract) as ?abstractStr)
    where {
      ?company a dbo:Company ;
         rdfs:label ?companyName ;
         dbo:foundingYear ?year ;
         dbo:abstract ?abstract .
      filter (langMatches(lang(?companyName),'en') && langMatches(lang(?abstract),'en') && strlen(?abstract) > 0)
    }
"""
]


def make_next_query(base, offset):
    return base + " LIMIT " + str(endpointLimit) + " OFFSET " + str(offset)


def perform_query(query):
    sparql.setQuery(prefixes + query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


def perform_iterate_query(query):
    results = []
    current_offset = 0
    while current_offset < limit:
        print("> performing iterate query; current offset is " + str(current_offset))
        results += sparql_results_to_list(perform_query(make_next_query(query, current_offset)))
        current_offset += endpointLimit
    return results


def sparql_results_to_list(results):
    target_json = []
    for result in results["results"]["bindings"]:
        target_json.append({
            "company": result["companyNameStr"]["value"].strip(),
            "year": result["yearStr"]["value"].strip(),
            "abstract": result["abstractStr"]["value"].strip()
        })

    return target_json


def query_dbpedia():
    print("Querying DBPedia endpoint for companies...")
    target_json = []
    for idx, q in enumerate(queries):
        print("performing {0} query...".format(idx + 1))
        nth_result = perform_iterate_query(q)
        target_json += nth_result
        print("got {0} items".format(len(nth_result)))

    print("total items count is {0}; fitering to find only abstracts with company name and foundation year..."
          .format(len(target_json)))

    return target_json


# return only entries which contain company name and foundation year in abstract
def filter_json(raw_json):
    filtered_json = []
    for entry in raw_json:
        try:
            date = parser.parse(entry['year'])
        except ValueError:
            continue
        if entry["company"] in entry["abstract"] and str(date.year) in entry["abstract"]:
            filtered_json.append(entry)

    print("total item count after filtering is {0}".format(len(filtered_json)))
    return filtered_json


def write_to_file(res):
    target_path = "./data"
    target_file = "raw.json"
    print("serializing to {0}/{1} file...".format(target_path, target_file))
    if not os.path.exists(target_path):
        os.makedirs(target_path)

    outfile = open("{0}/{1}".format(target_path, target_file), "w+", encoding='utf8')
    outfile.write(json.dumps(res, indent=4, sort_keys=True))
    outfile.close()

    print("done; ready to annotate")


if __name__ == '__main__':
    data = query_dbpedia()
    filtered_data = filter_json(data)
    write_to_file(data)
