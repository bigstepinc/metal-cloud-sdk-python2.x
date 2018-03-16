# -*- coding: utf-8 -*-

class ContainerInterface(object):
	"""
	A ContainerInterface is used to attach all the corresponding Container host
	interfaces to networks.
	"""

	def __init__(self):
		pass;


	"""
	The ID of the ContainerInterface.
	"""
	container_interface_id = None;

	"""
	This property helps ensure that edit operations don’t overwrite other,
	more recent changes made to the same object. It gets updated automatically
	after each successful edit operation.
	"""
	container_interface_change_id = None;

	"""
	The ID of the Container that the ContainerInterface belongs to.
	"""
	container_id = None;

	"""
	The ID of the network to which the ContainerInterface is attached.
	"""
	network_id = None;

	"""
	The ContainerInterface's label which is unique and it is used to form the
	<code>container_interface_subdomain</code>. Can be used to call API
	functions.
	"""
	container_interface_label = None;

	"""
	Automatically created based on <code>container_interface_label</code>. It is
	a unique reference to the ContainerInterface object.
	"""
	container_interface_subdomain = None;

	"""
	The status of the ContainerInterface.
	"""
	container_interface_service_status = None;

	"""
	The operation type, operation status and modified ContainerInterface object.
	"""
	container_interface_operation = None;

	"""
	Shows the index of the interface. Numbering starts at 0. There are 2
	interfaces for Container, with indexes 0 and 1.
	"""
	container_interface_index = None;

	"""
	ISO 8601 timestamp which holds the date and time when the ContainerInterface
	was created. Example format: 2013-11-29T13:00:01Z.
	"""
	container_interface_created_timestamp = "0000-00-00T00:00:00Z";

	"""
	ISO 8601 timestamp which holds the date and time when the ContainerInterface
	was edited. Example format: 2013-11-29T13:00:01Z.
	"""
	container_interface_updated_timestamp = "0000-00-00T00:00:00Z";

	"""
	The schema type.
	"""
	type = None;