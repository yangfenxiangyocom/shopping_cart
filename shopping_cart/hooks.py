# coding=utf-8
app_name = "shopping_cart"
app_title = "Shopping Cart"
app_publisher = "ERP Boost"
app_description = "直销以及分销下单渠道"
app_icon = "icon-shopping-cart"
app_color = "#B7E090"
app_email = "support@erpboost.com"
app_url = "https://www.erpboost.com"
app_version = "0.5.0"

web_include_js = "assets/js/shopping-cart-web.min.js"
web_include_css = "assets/css/shopping-cart-web.css"

on_session_creation = "shopping_cart.utils.set_cart_count"
on_logout = "shopping_cart.utils.clear_cart_count"
update_website_context = "shopping_cart.utils.update_website_context"

# Bean Events
doc_events = {
	"Sales Taxes and Charges Master": {
		"on_update": "shopping_cart.shopping_cart.doctype.shopping_cart_settings.shopping_cart_settings.validate_cart_settings"
	},
	"Price List": {
		"on_update": "shopping_cart.shopping_cart.doctype.shopping_cart_settings.shopping_cart_settings.validate_cart_settings"
	},
	# "Quotation": {
	# 	"validate": "shopping_cart.shopping_cart.doctype.shopping_cart_settings.shopping_cart_settings.apply_shopping_cart_settings"
	# }
}
