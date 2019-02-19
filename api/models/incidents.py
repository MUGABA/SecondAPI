
from api.models.models import User, Incident

from datetime import datetime


class IncidentList:

	def __init__(self):
		self.incident_list = []

		self.user_list = []

	def  fetch_all_incidence(self):
		return self.incident_list

	def fetch_all_users(self):
		return self.user_list

	def add_incident(self,incident):
		new_incident = incident.__dict__
		self.incident_list.append(new_incident)

	def add_user(self,user):

		new_user =  user.__dict__
		self.user_list.append(new_user)

	def retreave_incidents(self):
		return [incidents.__dict__ for incidents in incident_list]

	def retreave_users(self):
		return [users.__dict__ for users in user_list]


	def incident_id_generator(self):
		if len(self.incident_list) == 0:
			return 1
		else:
			return len(self.incident_list) + 1


	def user_id_generator(self):
		if len(self.user_list) == 0:
			return 1
		else:
			return len(self.user_list) + 1


	def fetch_specific_incident(self, id):
		specific_incident = [incident for incident in self.incident_list if incident['incident_id'] == id]

		try:
			return specific_incident[0]

		except IndexError:
			return




