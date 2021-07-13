# Copyright (c) 2021, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals

import frappe
from press.agent import Agent


def execute():
	servers = frappe.get_all(
		"Server", {"is_upstream_setup": True, "status": "Active"}, ["name", "proxy_server"],
	)
	for server in servers:
		agent = Agent(server.proxy_server, "Proxy Server")
		agent.update_upstream_private_ip(server.name)
