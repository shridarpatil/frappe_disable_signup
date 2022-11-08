# Copyright (c) 2022, Shrihar Patil and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class DisableSignupDomains(Document):
	def validate(self):
		self.domain = self.domain.lower()
		if len(self.domain.split(".")) < 2:
			frappe.throw(f"Invalid domain name {self.domain}")


def validate(doc, method):
	"""Disable signup for specific domains."""
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