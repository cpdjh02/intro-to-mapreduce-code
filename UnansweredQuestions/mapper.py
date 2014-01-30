#!/usr/bin/python


import sys
import csv

#0 id
#1 title
#2 tagnames
#3 author_id
#4 body
#5 node_type
#6 parent_id
#7 abs_parent_id
#8 added_at
#9 score
#10 state_string

#This mapper extracts the question_id and from each node so that the reducer can get counts of
#how many answers and comments a particular question has. The output is in the format:
#questionId	type

def isInteger(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

reader = csv.reader(sys.stdin, delimiter='\t')
for line in reader:
	nodeId = line[0]
	type=line[5]
	questionId = line[7] #abs_parent_id
	if not isInteger(nodeId):
		continue;#bad data
	if type=="question":
		questionId = nodeId
	print questionId,"\t",type
