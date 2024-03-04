# Copyright (c) 2024, Krishna and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Books(Document):
	def save(self):
		if not self.name1:
			
			# frappe.throw("Creating Stock Balance: Quantity Cannot Be Less Than 0!")
			frappe.msgprint("Please add Book Name",raise_exception=True)
