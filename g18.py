import sys
import re
def extract_names():
    names = []
    f = open('baby.html','r')
    a = f.read()
    year_match = re.search(r'Popularity\sin\s(\d\d\d\d)',a)
    if not year_match:
        sys.exit(1)
    year = year_match.group(1)
    names.append(year)
    tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', a)
    names_to_rank =  {}
    for rank_tuple in tuples:
        (rank, boyname, girlname) = rank_tuple
        if boyname not in names_to_rank:
            names_to_rank[boyname] = rank
        if girlname not in names_to_rank:
            names_to_rank[girlname] = rank
    sorted_names = sorted(names_to_rank.keys())
    for name in sorted_names:
        names.append(name + " " + names_to_rank[name])
    return names
print extract_names()    