# patches/add_custom_field.py

import frappe

def execute():
    # Define custom field properties
    field_properties = {
        "label": "Color",
        "fieldname": "color",
        "fieldtype": "Data",
        "insert_after": "book_status",
        # Add other properties as needed
    }

    # Create custom field
    doc = frappe.new_doc("Custom Field")
    doc.dt = "Books"
    doc.update(field_properties)
    doc.insert()
