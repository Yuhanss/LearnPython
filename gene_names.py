#!/usr/bin/python
import fileinput
import re
import json

print "["

for line in fileinput.input(['/home/yuhan/data/Homo_sapiens.GRCh37.75.gtf']):
    gene_name_matches = re.findall('gene_name \"(.*?)\";',line)
    text_in_columns = re.split('\t',line)
    if len(text_in_columns)>4:
       if text_in_columns[2] == "gene":
          if gene_name_matches:
             print json.dumps({"Gene_name":gene_name_matches[0],"Chromosome":text_in_columns[0],"StartPos":text_in_columns[3],"EndPos":text_in_columns[4]})
print "]"
