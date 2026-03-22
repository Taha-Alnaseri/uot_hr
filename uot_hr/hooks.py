app_name = "uot_hr"
app_title = "UOT-HR"
app_publisher = "Eng. Taha Al-Naseri"
app_description = "this app for manageing the human resource in the university of technology - iraq "
app_email = "taha.a.oohayyid@uotechnology.edu.iq"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "uot_hr",
# 		"logo": "/assets/uot_hr/logo.png",
# 		"title": "university of technology human resource managment application",
# 		"route": "/uot_hr",
# 		"has_permission": "uot_hr.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/uot_hr/css/uot_hr.css"
# app_include_js = "/assets/uot_hr/js/uot_hr.js"

# include js, css files in header of web template
# web_include_css = "/assets/uot_hr/css/uot_hr.css"
# web_include_js = "/assets/uot_hr/js/uot_hr.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "uot_hr/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "uot_hr/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "uot_hr.utils.jinja_methods",
# 	"filters": "uot_hr.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "uot_hr.install.before_install"
# after_install = "uot_hr.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "uot_hr.uninstall.before_uninstall"
# after_uninstall = "uot_hr.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "uot_hr.utils.before_app_install"
# after_app_install = "uot_hr.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "uot_hr.utils.before_app_uninstall"
# after_app_uninstall = "uot_hr.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "uot_hr.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"uot_hr.tasks.all"
# 	],
# 	"daily": [
# 		"uot_hr.tasks.daily"
# 	],
# 	"hourly": [
# 		"uot_hr.tasks.hourly"
# 	],
# 	"weekly": [
# 		"uot_hr.tasks.weekly"
# 	],
# 	"monthly": [
# 		"uot_hr.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "uot_hr.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "uot_hr.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "uot_hr.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["uot_hr.utils.before_request"]
# after_request = ["uot_hr.utils.after_request"]

# Job Events
# ----------
# before_job = ["uot_hr.utils.before_job"]
# after_job = ["uot_hr.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"uot_hr.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

permission_query_conditions = {
    "UOT Leave Request": "uot_hr.uot_hr.permissions.leave_request.get_permission_query_conditions",
    "UOT Employees": "uot_hr.uot_hr.permissions.leave_request.get_employee_permission_query_conditions",
    "User": "uot_hr.uot_hr.permissions.leave_request.get_user_permission_query_conditions"
}

has_permission = {
    "UOT Leave Request": "uot_hr.uot_hr.doctype.uot_leave_request.uot_leave_request.has_permission"
}

after_migrate = [
    "uot_hr.uot_hr.api.sync_custom_permissions"
]


fixtures = [
    # Roles
    {
        "doctype": "Role",
        "filters": [["name", "like", "UOT%"]]
    },
    # Workflow
    {
        "doctype": "Workflow",
        "filters": [["name", "=", "leave reques approval workflow"]]
    },
    # Workflow States
    {
        "doctype": "Workflow State",
        "filters": [["name", "in", [
            "Pending",
            "Approved",
            "Rejected",
            "approved by the line manager",
            "Approved by the Administrative Associate"
        ]]]
    },
    # Workflow Actions
    {
        "doctype": "Workflow Action Master",
        "filters": [["name", "in", [
            "Approve",
            "Reject",
            "Review"
        ]]]
    },
    # Leave Types
    {
        "doctype": "UOT Leave Type"
    },
    # Notifications
    {
        "doctype": "Notification",
        "filters": [["name", "in", [
            "New Leave Request  Creation",
            "UOT Leave Request manager action",
            "New Maternity leave request notification",
            "uot leave request update"
        ]]]
    },
    # Print Formats
    {
        "doctype": "Print Format",
        "filters": [["name", "in", [
            "UOT leave request",
            "Maternity leave form"
        ]]]
    },
    # Number Cards
    {
        "doctype": "Number Card",
        "filters": [["name", "in", [
            "Leave Requests"
        ]]]
    },
    # Workspace
    {
        "doctype": "Workspace",
        "filters": [["name", "=", "UOT HR"]]
    },
    # Custom Fields
    {
        "doctype": "Custom Field",
        "filters": [["name", "in", [
            "Leave Request-workflow_state"
        ]]]
    }
]