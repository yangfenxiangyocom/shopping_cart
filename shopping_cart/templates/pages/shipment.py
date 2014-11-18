# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from shopping_cart.templates.utils import get_transaction_context

no_cache = 1
no_sitemap = 1

def get_context(context):
	shipment_context = frappe._dict({
		"parent_link": "shipments",
		"parent_title": _("Shipments")
	})
	shipment_context.update(get_transaction_context("Delivery Note", frappe.form_dict.name))
	modify_status(shipment_context.doc)
	return shipment_context

def modify_status(doc):
	doc.status = '<span class="label label-success"><i class="icon-fixed-width icon-ok"></i>' +  _(doc.status) + '</span> &nbsp' 