import MySQLdb as mdb
import utils as utl


def create_user(cur):
	query_str = (" create table if not exists %s("
	"%s int not null auto_increment," #user id
	"%s varchar(30),"				  #fname
	"%s varchar(30),"				  #lname
	"primary key(%s)")%(utl.table_user, utl.user_id, utl.user_firstname, utl.user_lastname, utl.user_id)
	cur.execute(query_str)

def create_event(cur):
	query_str = (" create table if not exists %s("
	"%s int not null auto_increment," #event id
	"%s int not null,"				  #user id
	"%s int not null,"				  #weight
	"%s int not null,"				  #starttime
	"%s int not null,"				  #endtime
	"%s varchar(30),"                 #name
	"%s varchar(150),"				  #desc
	"primary key(%s)")%(utl.table_event, utl.event_id, utl.event_userid, utl.event_weight, utl.event_starttime, utl.event_endtime, utl.event_name, utl.event_desc, utl.event_id)
	cur.execute(query_str)

def create_participant(cur):
	query_str = (" create table if not exists %s("
	"%s int not null,"				  #userid
	"%s int not null,"				  #eventid
	"primary key(%s, %s)")%(utl.table_participant, utl.participant_userid, utl.participant_eventid, utl.participant_userid, utl.participant_eventid)
	cur.execute(query_str)

def creation():
	try:
	    con = mdb.connect(utl.host, utl.dbuser, utl.dbpass, utl.dbname);
	    cur = con.cursor()
	except mdb.error, e:
	    print "error %d: %s" % (e.args[0],e.args[1])
	    sys.exit(1)

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
	query_str = ("select %s from %s where %s = \'%s\'")%(utl.participant_userid, utl.table_participant, utl.participant_eventid, eventid)
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
	query_str = ("select %s from %s where %s = \'%s\'")%(utl.participant_userid, utl.table_participant, utl.participant_eventid, eventid)
	print query_str
	cur.execute(query_str)
	results = []
	for row in cur:
		results.append(row)
		
	return results