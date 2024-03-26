import frappe

def execute():
    books = frappe.get_all("Books", fields=["name", "sold"])
    for book in books:
        if book.sold:
            frappe.db.set_value("Books", book.name, "book_status", "Out of Stock")
        else:
            frappe.db.set_value("Books", book.name, "book_status", "In Stock")
