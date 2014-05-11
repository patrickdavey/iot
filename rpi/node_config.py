# -*- coding: utf-8 -*-

import json
import datetime

class NodeConfig:
	id = None
	node_id = None
	sensor_id = None
	formula = None
	created_at = None

	def __init__(self):
		created_at = str(datetime.datetime.strftime("%Y-%m-%d %H:%M:%S", datetime.datetime.utcnow()))

	def save(self, cursor):
		if self.id is not None:
			cursor.execute("UPDATE node_configs SET node_id = (%s), sensor_id=(%s), formula=(%s) WHERE id = (%s)", (self.node_id, self.sensor_id, self.formula, datetime.datetime.utcnow(), self.id))
		else:
			cursor.execute("INSERT INTO node_configs(node_id, sensor_id, formula, created_at) VALUES (%s, 'default', %s, %s, %s)", (self.node_id, self.sensor_id, self.formula, datetime.datetime.utcnow()))

	@staticmethod
	def init(json_config):
		if json_config is None:
			return None
		
		new_config = NodeConfig()

		if 'id' in json_config:
			new_config.id = json_config['id']
		if 'node_id' in json_config:
			new_config.node_id = json_config['node_id']
		if 'sensor_id' in json_config:
			new_config.sensor_id = json_config['sensor_id']
		if 'formula' in json_config:
			new_config.formula = json.loads(json_config['formula'])
		if 'created_at' in json_config:
			new_config.created_at = json_config['created_at']
		return new_config

	@staticmethod
	def get_by_node_id(node_id, cursor):
		result = cursor.execute("SELECT * FROM node_configs WHERE node_id = (%s)", (node_id,))
		configs = []
		for r in result:
			configs = configs + [NodeConfig.init(r)]