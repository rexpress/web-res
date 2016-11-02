# -*- coding: utf-8 -*-
"""
	ds
	----------------
	data structure of regular.express

	:author: Prev(prevdev@gmail.com)
"""


class EnvInfo :
	def __init__(self, model) :
		result = model.get('/repos/rexpress/environments/git/trees/master?recursive=1', baseurl='https://api.github.com', headers={})
		self.data = {}

		# init env info data
		for info in result['tree'] :
			p = info['path'].split('/')

			if len(p) != 2 : continue

			env_group = p[0]
			env_child = p[1].split('.json')[0]

			if env_child == '_info' :
				self.data[ env_group ] = EnvGroup(
					name = env_group,
					info = model.macro('#git-env', env_group + '/_info.json#' + info['sha']),
				)

			else :
				self.data[ env_group ].append_child( EnvChild(
					name = env_child,
					info = model.macro('#git-env', env_group + '/' + env_child + '.json#' + info['sha']),
				))


	@property
	def groups(self) :
		return self.data


	def getdict(self, group, child=None, loose_mode=False) :
		if group not in self.data :
			if loose_mode : {'name': child or group}
			else : return None
		
		eg = self.data[ group ]

		if child is None :
			return eg
		else :
			c = eg.get_child(child)
			if c is not None :
				return c
			else :
				if loose_mode : return {'name': child}
				else : return None


	def json(self) :
		import ast, json
		d = ast.literal_eval( str(self.groups) )
		return json.dumps(d)


class EnvBase :
	def __init__(self, name, info) :
		self.name = name
		self.info = info

	def __repr__(self):
		return str({
			'name': self.name,
			'info': self.info,
		})


class EnvGroup(EnvBase) :
	def __init__(self, name, info) :
		EnvBase.__init__(self, name, info)
		self.children = {}


	def append_child(self, env_child) :
		self.children[ env_child.name ] = env_child
		env_child.parent = self


	def get_child(self, child_name) :
		if child_name in self.children :
			return self.children[ child_name ]
		else :
			return None

	def __repr__(self):
		if self.children is None :
			return EnvBase.__repr__(self)
		else :
			return str({
				'name': self.name,
				'info': self.info,
				'children': self.children,
			})
			#dict( map( lambda k,v : (k, str(v)), self.children.keys(), self.children.values() ) )


class EnvChild(EnvBase) :
	def __init__(self, name, info, parent=None) :
		EnvBase.__init__(self, name, info)
		self.parent = parent


	def __repr__(self):
		if self.parent is None : nparent = None
		else :
			nparent = EnvGroup(self.parent.name, self.parent.info)
			nparent.children = None

		return str({
			'name': self.name,
			'info': self.info,
			'parent': nparent,
		})


