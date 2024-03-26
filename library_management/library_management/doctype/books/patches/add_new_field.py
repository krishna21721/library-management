import frappe

def execute():
    # Fetch the meta data of the DocType
    doc_meta = frappe.get_meta("Books")

    # Add new field
    new_field = {
        "label": "Rating",
        "fieldname": "rating",
        "fieldtype": "Rating"
    }
    doc_meta.fields.append(new_field)


    # Save the changes to the DocType
    frappe.db.sql("ALTER TABLE `tabBooks` ADD COLUMN `rating` varchar(255)")

    # Reload DocType cache to reflect the changes
    frappe.cache().delete_value("fieldnames")
