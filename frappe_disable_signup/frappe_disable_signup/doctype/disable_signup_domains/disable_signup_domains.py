# Copyright (c) 2022, Shrihar Patil and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class DisableSignupDomains(Document):
	def validate(self):
		self.domain = self.domain.lower()
		print("** " * 20, (len(self.domain.split("."))))
		if len(self.domain.split(".")) < 2:
			frappe.throw(f"Invalid domain name {self.domain}")

	# def on_update(self):
	# 	frappe.cache().set_value(self.domain, self.status)
	# 	print(frappe.cache().get_value(self.domain))


def validate(doc, method):
	"""Disable signup for specific domains."""
	print(doc.__dict__)
	domain = frappe.db.get_value(
		"Disable Signup Domains",
		{

			"domain": doc.email.split("@")[1].lower(),
			"status": "Active"
		},
		"domain"
	)
	if domain:
		frappe.throw(f"Not allowed to signup using <b>{domain}</b> domain")