import re
def header_parse(text:str)->str:
	"""[regex check for headers]

	Args:
		text (str): [Markdown text]

	Returns:
		str: [HTML text]
	"""	
	_headers = ['#', '##', '###', '####', '#####', '######']
	for i in _headers:
		if re.match(f'{i} (.*)', text) is not None:
			_hlength = len(i)
			return f'<h{_hlength}>' + text[_hlength + 1:] +  f'</h{_hlength}>' 
	return None

def bold_parse(text:str)->str:
	"""[regex check for bold]

	Args:
		text (str): [Markdown text]

	Returns:
		str: [HTML text]
	"""	
	m = re.match('(.*)__(.*)__(.*)', text)
	if m is not None:
		return m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
	return text

def italic_parse(text:str)->str:
	"""[regex check for italics]

	Args:
		text (str): [Markdown text]

	Returns:
		str: [HTML text]
	"""	
	m = re.match('(.*)_(.*)_(.*)', text)
	if m is not None:
		return m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
	return text

def list_parse(text:str, inlist:bool)->(str, bool):
	"""[Parses list]

	Args:
		text (str): [Input line item of markdown]
		inlist (bool): [Whether or not currently in a list]

	Returns:
		str: [HTML formatted list item]
		bool: [Whether item is in list still]
	"""	
	#Check the beginning for asterisk
	start_bool = text.startswith('*')
	
	if start_bool:
		#If it is a list item, check if already in list
		if inlist:
			return '<li>' + text[2:] + '</li>', True
		
		else:
			#Means beginning of list
			in_list = True
			return '<ul><li>' + text[2:] + '</li>', in_list
	else:
		if inlist:
			#Means end of list
			return '</ul>' + text, False
		else:
			return text, inlist
	
##Converts a markdown string to HTML
def parse(markdown:str)->str:
	"""[Parses Markdown text into HTML tags]

	Args:
		markdown ([str]): [Markdown text]

	Returns:
		[str]: [HTML text]
	"""	
	#split lines
	lines = markdown.split('\n')
	#Set up variables
	res, inlist = '', False
	#Iterate through each line
	for i in lines:
		#Parse for headers
		m = header_parse(i)
		if m is not None:
			res += m
			continue
		#Parse for lists
		m, inlist = list_parse(i, inlist)
		#Parse for bold
		m = bold_parse(m)
		#Parse for italics
		m = italic_parse(m)
		#If it doesn't find relevant tags, adds paragraph tags
		r = re.match('<h|<ul|<p|<li', m)
		if not r:
			#If its the end of the list, wraps the end list tag correctly
			if m.startswith("</ul>"):
				m = m[:5] + '<p>' + m[5:] + '</p>'
			else:
				m = '<p>' + m + '</p>'
			res += m
			continue
		res += m
	#If the last line was a list, wrap it up
	if inlist:
		res += '</ul>'
	return res