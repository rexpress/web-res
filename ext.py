# -*- coding: utf-8 -*-
"""
	ext
	----------------
	extension functions of regular.express

	:author: Prev(prevdev@gmail.com)
"""

def customize_model(model) :
	model.make_macro('#view',       'GET', '/re/_design/$1/_view/$2?$3')
	model.make_macro('#view-eq',    'GET', '/re/_design/$1/_view/$2?keys=["$3"]&include_docs=true')
	model.make_macro('#view-range', 'GET', '/re/_design/$1/_view/$2?startkey=["$3",{}]&endkey=["$3"]&descending=true&include_docs=true')
	model.make_macro('#git-env',    'GET', '/rexpress/environments/raw/master/$1', baseurl='https://github.com/', immutable=True, headers={})


def get_envs(model) :
	result = model.get('/repos/rexpress/environments/git/trees/master?recursive=1', baseurl='https://api.github.com', headers={})
	output = {}

	for info in result['tree'] :
		p = info['path'].split('/')

		if len(p) != 2 : continue

		env_group = p[0]
		env_child = p[1].split('.json')[0]

		if env_child == '_info' :
			# Set Env Group
			output[ env_group ] = {
				'env'     : env_group,
				'info'    : model.macro('#git-env', env_group + '/_info.json'),
				'shares'  : model.macro('#view-range', 'env', 'shares', env_group)['rows'],
				'children': {},
			}

		else :
			# Set Env child
			output[ env_group ]['children'][ env_child ] = {
				'env_group' : env_group,
				'env_child' : env_child,
				'info' : model.macro('#git-env', env_group + '/' + env_child + '.json'),
				'shares' : model.macro('#view-range', 'env', 'shares', env_group + '","' + env_child)['rows'],
			}

	return output



_devicon_data = None

def get_devicon_class(env) :
	global _devicon_data

	if _devicon_data is None :
		data = {
			'python': ['python'],
			'java': ['java'],
			'apache': ['apache', 'hive', 'flume']
		}

		output = {}
		for k, l in data.items() :
			for i in l :
				output[i] = k

		_devicon_data = output

	return _devicon_data[env]


