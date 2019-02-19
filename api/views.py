
from flask import Blueprint, jsonify,abort,make_response,request,json 
from api.models.models import User, Incident
from api.models.validators import Validator
from api.models.incidents import IncidentList
from datetime import datetime


appblueprint = Blueprint('api', __name__)
incident = IncidentList()
is_valid = Validator()


@appblueprint.route('/')
def index():
	return 'Welcome to ireporter'

@appblueprint.route('/users', methods = ['POST'])
def register_users():

	if not request.json or not request.get_json()['firstname'] \
	or not request.get_json()['lastname'] or not request.get_json()['othername'] \
	or not request.get_json()['email'] or not request.get_json()['phone_number'] \
	or not request.get_json()['username']:

		return jsonify({"message":"Input field cannot be null"})



	firstname,lastname,othername,email,phone_number,username = \
	request.get_json()['firstname'], request.get_json()['lastname'], \
	request.get_json()['othername'], request.get_json()['email'], \
	request.get_json()['phone_number'], request.get_json()['username']

	user_id = incident.user_id_generator()

	is_admin = False

	registerd = date_today = datetime.now().strftime('%d%m%y %H%M')
	new_user = User(user_id, firstname, lastname, othername, email, phone_number, username, registerd, is_admin)
	incident.add_user(new_user)

	return jsonify({"Status Code": 201, "User": incident.user_list[-1]}),201


@appblueprint.route('/users')
def fetch_all_users():

	return jsonify({"Users":incident.fetch_all_users()}),200


@appblueprint.route('/red-flags')
def fetch_all_incidents():
	return jsonify({"Incidents": incident.fetch_all_incidence()})


@appblueprint.route('/incidents', methods = ['POST'])
def report_incident():

	if not request.json or not request.get_json()['incident_type']  \
	or not request.get_json()['created_by']  \
	or not request.get_json()['Status'] or not request.get_json()['location'] \
	or not request.get_json()['images'] or not request.get_json()['videos'] \
	or not request.get_json()['comment']:

		abort(400)

	incident_type, created_by, status, location, images, videos, comment = \
	request.get_json()['incident_type'], request.get_json()['created_by'], \
	request.get_json()['Status'], request.get_json()['location'], \
	request.get_json()['images'], request.get_json()['videos'], request.get_json()['comment']


	incident_id = incident.incident_id_generator()

	created_on = date_today = datetime.now().strftime('%d%m%y %H%M')

	new_incident = Incident(incident_type, incident_id,created_by, created_on, status, location, images, videos, comment)

	incident.add_incident(new_incident)

	return jsonify({"incident":incident.incident_list[-1]}),201


@appblueprint.route('/red-flags/<int:redflag_id>',methods = ['GET'])
def fetch_specific_red_flag(redflag_id):

	if not incident.fetch_specific_incident(redflag_id):
		return jsonify({"Error": "No incident found"})
	return jsonify({"red_flag": incident.fetch_specific_incident(redflag_id)})

@appblueprint.route('/red-flags/<int:redflag_id>/location',methods = ['PATCH'])
def patch_redflag_location(redflag_id):

	redflag = incident.fetch_specific_incident(redflag_id)

	if redflag:
		location = request.get_json()['location']
		new_location = location
		redflag['location'] = new_location

		return jsonify({"incident": redflag})

	else:
		return jsonify({"Status": 200, "message" : "No ncident found"})



@appblueprint.route('/red-flags/<int:redflag_id>/comment',methods = ['PATCH'])
def patch_redflag_comment(redflag_id):
	redflag = incident.fetch_specific_incident(redflag_id)

	if redflag:
		comment = request.get_json()['comment']
		new_comment = comment
		redflag['comment'] = new_comment

		return jsonify({"incident" : redflag})

	else:
		return jsonify({"Status": 200, "message": "no Incident found"})

@appblueprint.route('/red-flags/<int:redflag_id>', methods = ['DELETE'])
def delete_specific_incident(redflag_id):
	redflag = incident.fetch_specific_incident(redflag_id)

	if redflag:
		incident.incident_list.remove(redflag)

		return jsonify({"message":"incident has been removed "})

	else:
		return jsonify({"Status Code":200, "message" : "no incident found" })

