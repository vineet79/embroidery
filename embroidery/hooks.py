# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "embroidery"
app_title = "Embroidery"
app_publisher = "Mayur"
app_description = "Embroidery App"
app_icon = "octicon octicon-file-zip"
app_color = "#bd4747"
app_email = "mayur@mittalclothing.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/embroidery/css/embroidery.css"
# app_include_js = "/assets/embroidery/js/embroidery.js"

# include js, css files in header of web template
# web_include_css = "/assets/embroidery/css/embroidery.css"
# web_include_js = "/assets/embroidery/js/embroidery.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "embroidery.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "embroidery.install.before_install"
# after_install = "embroidery.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "embroidery.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"embroidery.tasks.all"
# 	],
# 	"daily": [
# 		"embroidery.tasks.daily"
# 	],
# 	"hourly": [
# 		"embroidery.tasks.hourly"
# 	],
# 	"weekly": [
# 		"embroidery.tasks.weekly"
# 	]
# 	"monthly": [
# 		"embroidery.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "embroidery.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "embroidery.event.get_events"
# }

