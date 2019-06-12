from math import log2, sqrt
import operator


def tokenize(document: str) -> list:
    """Function turns text into a list of tokens. 
    Each word is turned to lowercase and stripped of dots, commas, question and exclamation marks."""
    return [word.strip('"?!,.') for word in document.lower().strip().split()]


def idf_matrix(documents: dict) -> dict:
    """Function creates a matrix in the form of a dictionary containing information which words occurred in which documents.
    """
    # init dictionary
    print('begin creating idf_matrix')
    d = {
        'doc_count': len(documents.keys()),
        'doc_vector_lengths': {},
        'words': {},
        'docs': {}
    }

    # make an entry for each word 
    # noting in which document it appeared and how many times
    # additionally make a list of unique words per each document
    for idx, doc in enumerate(documents, 1):
        if idx % 1000 == 0: print('processing document no:', idx)
        t = tokenize(documents[doc])
        d['docs'][doc] = set(t)
        for element in t:
            if d['words'].get(element) is None:
                d['words'][element] = {'occurences': {doc: 1}, 'total': 1}
            elif d['words'].get(element).get('occurences').get(doc) is None:
                d['words'][element]['occurences'][doc] = 1
                d['words'][element]['total'] += 1
            else:
                d['words'][element]['occurences'][doc] += 1
                d['words'][element]['total'] += 1

    # temp variable
    dc = d['doc_count']

    # calculate logarithm of inverse document frequency per word
    print('calculating logarithms')
    for word in d['words']:
        idf = dc/d['words'][word]['total']
        d['words'][word]['idf_logarithm'] = log2(idf)

    # calculate vector length for each document
    print('calculating vector length')
    for idx, doc in enumerate(d['docs'], 1):
        if idx % 1000 == 0: print('processing document no', idx)
        d['doc_vector_lengths'][doc] = sqrt(sum(
            [
                (d['words'][x]['idf_logarithm']*d['words'][x]['occurences'][doc])**2 
                for x in d['docs'][doc]
                if d['words'][x]['occurences'].get(doc) is not None
            ]
        ))
    print('finished preparing the dataset')

    return d


def search(q: str, idf_matrix: dict) -> list:
    """Function searches for text in documents comparing similarity between them."""
    tq = tokenize(q)
    q_matrix = {}

    print('searching for query:', q)
    print('counting words')
    for t in tq:
        if q_matrix.get(t) is not None:
            q_matrix[t]['count'] += 1
        else:
            q_matrix[t] = {'count': 1, 'log': None}

    print('calculating logarithms for each word')
    for word in q_matrix:
        q_matrix[word]['log'] = (
            (q_matrix[word]['count'] * idf_matrix['words'][word]['idf_logarithm'])
            /
            idf_matrix['words'][word]['total']
        ) if idf_matrix['words'].get(word) else 0

    print('calculating vector length of query')
    q_vector_length = sqrt(sum(
        [q_matrix[x]['log']**2 for x in q_matrix]
    ))

    print('comparing query vector to vector of every document')
    comparison_vector_lengths = {}
    for doc in idf_matrix['docs']:
        temp = []
        for word in q_matrix:
            q_log = q_matrix[word]['log']
            if (
                idf_matrix['words'].get(word) is not None
                and 
                idf_matrix['words'][word]['occurences'].get(doc) is not None
            ):
                idf_log = idf_matrix['words'][word]['idf_logarithm'] * idf_matrix['words'][word]['occurences'][doc]
            else:
                idf_log = 0
            temp.append(q_log * idf_log)
        comparison_vector_lengths[doc] = sum(temp) / (q_vector_length * idf_matrix['doc_vector_lengths'][doc])
    # pprint(idf_matrix['doc_vector_lengths'])
    # pprint(comparison_vector_lengths)

    # return list of document ids sorted by similarity score
    return sorted(comparison_vector_lengths.items(), key=operator.itemgetter(1), reverse=True)


if __name__ == "__main__":
    # from pprint import pprint

    d = {
        'd1': 'Litwo ojczyzno moja tyś jest jak zdrowie.',
        'd2': 'Ala ma kota. Kot ma Alę.',
        'd3': 'Ala, jak zdrowie?',
        'd4': 'test test test'
    }

    q = 'Moja Ala ma ładnego kota.'

    # print(tokenize(d1))
    # pprint(idf_matrix(a=d1, b=d2, c=d3, d=d4))

    baza = idf_matrix(d)
    print(search(q, baza))

