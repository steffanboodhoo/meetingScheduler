import utils as utl
#start_timestamp + end_timestamp + weighting
#query for all start times 
#graded down to stamp and a weighting 
'''
{task_id
	{
		'start_time':'#'
		'end_time':'#'
		'weight':'#'
	}
}
'''
def insertUser(email, firstname, lastname):
	params = {}
	params[utl.user_userid] = email
	params[utl.user_firstname] = firstname
	params[utl.user_lastname] = lastname
	db.insert(params, utl.table_user)

def insertEvent(userid, weight, starttime, endtime, name):
	params = {}
	params[utl.event_userid] = userid
	params[utl.event_weight] = weight
	params[utl.event_start_time] = starttime
	params[utl.event_end_time] = endtime
	params[utl.event_name] = name
	db.insert(params, utl.table_event)

def addParticipant(userid, eventid):
	params = {}
	params[utl.participant_userid] = userid
	params[utl.participant_eventid] = eventid
	db.insert(params, utl.table_participant)

# def get_Events(t1, t2, length, guests):
	#query retrieves rows of [userid, start_time, end_time, weight] maybe task_id
	
#Order results by start time
#Assumes you cannot have more than one task running concurrently
def convert_EventVector(eventVector, eventList):

	amt = len(eventVector)
	
	for e in eventList:
		while( eventVector[curr] < e['end_time'] and curr < amt):
			eventVector[curr] = e['weight']
			curr += 1



#creates a blank eventVector with the times and a weighting of 0
def create_EventVector(t1, t2, length):
	eventVector = []
	# amt = (t2 - t1) / (length/2)
	amt = (t2 - t1) / length
	for i in range(amt): # 0 to amt-1
		eventVector.append({ str(t1+(i*l)) : 0})

	return eventVector


if __name__ == '__main__':
	#1447804800 1447891200 3600
	print create_EventVector(1447804800, 1447891200, 3600)

