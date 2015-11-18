import MySQLdb as mdb
import utils as utl
import sys

def create_user(cur):
	query_str = (" create table if not exists %s("
	"%s varchar(40) ," #user id
	"%s varchar(30),"				  #fname
	"%s varchar(30),"				  #lname
	"primary key(%s)")%(utl.table_user, utl.user_id, utl.user_first_name, utl.user_last_name, utl.user_id)
	cur.execute(query_str)

def create_event(cur):
	query_str = (" create table if not exists %s("
	"%s int not null auto_increment," #event id
	"%s varchar(40) not null,"		  #user id
	"%s int not null,"				  #weight
	"%s int not null,"				  #starttime
	"%s int not null,"				  #endtime
	"%s varchar(30),"                 #name
	# "%s varchar(150),"				  #desc
	"primary key(%s)")%(utl.table_event, utl.event_id, utl.event_userid, utl.event_weight, utl.event_starttime, utl.event_endtime, utl.event_name, utl.event_id)
	cur.execute(query_str)

def create_participant(cur):
	query_str = (" create table if not exists %s("
	"%s varchar(40) not null,"		  #userid
	"%s int not null,"				  #eventid
	"primary key(%s, %s)")%(utl.table_participant, utl.participant_user_id, utl.participant_eventi_d, utl.participant_user_id, utl.participant_event_id)
	cur.execute(query_str)

def creation():
	try:
	    con = mdb.connect(utl.host, utl.dbuser, utl.dbpass, utl.dbname);
	    cur = con.cursor()
	except mdb.Error, e:
	    print "Error %d: %s" % (e.args[0],e.args[1])
	    sys.exit(1)

	create_user(cur)
	create_event(cur)
	create_participant(cur)

	cur.close()

if __name__ == '__main__':
	creation()

def getParticipants(eventid):
	try:
	    con = mdb.connect(utl.host,utl.dbuser, utl.dbpass, utl.dbname);
	    cur = con.cursor(mdb.cursors.DictCursor)
	except mdb.Error, e:
	    print "Error %d: %s" % (e.args[0],e.args[1])
	    sys.exit(1)

	#select userid from participants_tbl where eventid = [id of event]
	query_str = ("select %s from %s where %s = \'%s\'")%(utl.participant_user_id, utl.table_participant, utl.participant_event_id, eventid)
	print query_str
	cur.execute(query_str)
	results = []
	for row in cur:
		results.append(row)
		
	return results

def getSchedules(eventid):
	try:
	    con = mdb.connect(utl.host,utl.dbuser, utl.dbpass, utl.dbname);
	    cur = con.cursor(mdb.cursors.DictCursor)
	except mdb.Error, e:
	    print "Error %d: %s" % (e.args[0],e.args[1])
	    sys.exit(1)

	#select start_time, end_time, userid, event_id from event_tbl where userid in [list of userid's]
	query_str = ("select %s from %s where %s = \'%s\'")%(utl.participant_user_id, utl.table_participant, utl.participant_eventid, event_id)
	print query_str
	cur.execute(query_str)
	results = []
	for row in cur:
		results.append(row)
		
	return results


#params is a dict with the keys being the column names and the values being the actual values
def insert(params,table_name):
	try:
	    con = mdb.connect(utl.host, utl.dbuser, utl.dbpass, utl.dbname);
	    cur = con.cursor()
	except mdb.Error, e:
	    print "Error %d: %s" % (e.args[0],e.args[1])
	    sys.exit(1)

	query_str = ("INSERT INTO %s ("%(table_name))
	values_str = ") VALUES ("
	values = []
	for k_1 in params:
		query_str += "`%s`,"%(k_1)
		values_str += "%s,"
		values.append(params[k_1])
	query_str = query_str[:-1] + values_str[:-1] +")" #remove the last comma from each 
	
	
	
	try:
		cur.execute(query_str,values)
		con.commit()
		con.close()
	except:
		con.rollback()
		print 'did not insert'

