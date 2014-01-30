#!/usr/bin/python

import sys

# Loop around the data
# It will be in the format "questionId	type"
# All child nodes for a given question will be present
#
# The task for this reducer is to get a count of all the answers and comments a given question has.
# The reducer will output the question node id for each question that doesn't have an answer or comment.
#
# This map reduce pair would be something similar to the following SQL statement
# select a.node_id from forum_node a where a.node_id not in (select distinct b.abs_parent_id from forum_node b)





class QuestionCount(object):
	questionId=0
	commentCount=0
	answerCount=0

def reducer():
	oldQuestion = None
	# Loop around the data
	questionData = QuestionCount();
	for line in sys.stdin:
	    data_mapped = line.strip().split("\t")
	    if len(data_mapped) != 2:
		# Something has gone wrong. Skip this line.
		continue

	    question, type = data_mapped

	    if oldQuestion and oldQuestion != question:
		#Here we can do all the processing we want to do on a question regarding its count
		#For this case I am interested in getting a list of the questions that don't have
		#any answers or comments
		if questionData.answerCount==0 and questionData.commentCount==0	:
			print oldQuestion #print out the question's node id
		oldQuestion = question;
		questionData = QuestionCount();

	    oldQuestion = question
	    if type == "answer":
		questionData.answerCount += 1
	    elif type == "comment":
		questionData.commentCount += 1
	    elif type == "question":
		questionData.questionId=question
	if oldQuestion != None and questionData.answerCount==0 and questionData.commentCount==0:
	    print oldQuestion #print out the question's node id


reducer()