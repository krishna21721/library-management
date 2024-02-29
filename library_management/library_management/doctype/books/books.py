# Copyright (c) 2024, Krishna and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Books(Document):
	def validate(self):
		if not self.name1:
			frappe.throw("Please add Book Name")
