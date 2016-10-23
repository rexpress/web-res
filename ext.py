# -*- coding: utf-8 -*-
"""
	ext
	----------------
	extension functions of regular.express

	:author: Prev(prevdev@gmail.com)
"""


def get_shares(design_name, key, envinfo) :
	global model

	return process_shares(
		model.macro('#view-range', design_name, 'shares', key).rows,
		envinfo = envinfo,
	)


def process_shares(shares, envinfo) :
	output = []

	for index, data in enumerate(shares) :
		if index % 2 == 1 : continue

		o = data['doc']
		o['author'] = shares[index+1]['doc']
		o['env_group'] = envinfo.getdict(o['env'][0], loose_mode=True)
		o['env_child'] = envinfo.getdict(o['env'][0], o['env'][1], loose_mode=True)

		output.append(o)

	return output


def env_icon(icon_info) :
	if icon_info['type'] == 'devicon' :
		return '<i class="devicon-%s-plain"></i>' % icon_info['value']

	elif icon_info['type'] == 'img':
		return '<img src="%s">' % icon_info['value']

	elif icon_info['type'] == 'raw':
		return icon_info['value']

	else:
		return None
	

