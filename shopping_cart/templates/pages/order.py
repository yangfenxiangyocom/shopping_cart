# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from shopping_cart.templates.utils import get_transaction_context

no_cache = 1
no_sitemap = 1

def get_context(context):
	order_context = frappe._dict({
		"parent_link": "orders",
		"parent_title": _("My Orders")
	})

	order_context.update(get_transaction_context("Sales Order", frappe.form_dict.name))
	modify_status(order_context.doc)
	return order_context

def modify_status(doc):
	doc.status = []
	if 0 < doc.per_billed < 100:
		doc.status.append(("label-warning", "icon-ok", _("Partially Billed")))
	elif doc.per_billed == 100:
		doc.status.append(("label-success", "icon-ok", _("Billed")))

	if 0 < doc.per_delivered < 100:
		doc.status.append(("label-warning", "icon-truck", _("Partially Delivered")))
	elif doc.per_delivered == 100:
		doc.status.append(("label-success", "icon-truck", _("Delivered")))
	doc.status = '<span class="label label-success"><i class="icon-fixed-width icon-ok"></i>' +  _("Submitted") + '</span> &nbsp' + " ".join(('<span class="label %s"><i class="icon-fixed-width %s"></i> %s</span>' % s
			for s in doc.status))
