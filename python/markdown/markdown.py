import re


def parse(markdown):
	lines = markdown.split('\n') #Split on newline
	res = ''
	#Empty lists
	in_list = False
	in_list_append = False
	#Step through line splits matching characters
	#Looking for h1, h2, h6 tags?
	for i in lines:
		if re.match('###### (.*)', i) is not None:
			i = '<h6>' + i[7:] + '</h6>'
		elif re.match('## (.*)', i) is not None:
			i = '<h2>' + i[3:] + '</h2>'
		elif re.match('# (.*)', i) is not None:
			i = '<h1>' + i[2:] + '</h1>'
		m = re.match(r'\* (.*)', i)
		#If there's a match.  
		if m:
			if not in_list:
				in_list = True
				is_bold = False
				is_italic = False
				curr = m.group(1)
				m1 = re.match('(.*)__(.*)__(.*)', curr)
				if m1:
					curr = m1.group(1) + '<strong>' + \
						m1.group(2) + '</strong>' + m1.group(3)
					is_bold = True
				m1 = re.match('(.*)_(.*)_(.*)', curr)
				if m1:
					curr = m1.group(1) + '<em>' + m1.group(2) + \
						'</em>' + m1.group(3)
					is_italic = True
				i = '<ul><li>' + curr + '</li>'
			else:
				is_bold = False
				is_italic = False
				curr = m.group(1)
				m1 = re.match('(.*)__(.*)__(.*)', curr)
				if m1:
					is_bold = True
				m1 = re.match('(.*)_(.*)_(.*)', curr)
				if m1:
					is_italic = True
				if is_bold:
					curr = m1.group(1) + '<strong>' + \
						m1.group(2) + '</strong>' + m1.group(3)
				if is_italic:
					curr = m1.group(1) + '<em>' + m1.group(2) + \
						'</em>' + m1.group(3)
				i = '<li>' + curr + '</li>'
		else:
			if in_list:
				in_list_append = True
				in_list = False

		m = re.match('<h|<ul|<p|<li', i)
		if not m:
			i = '<p>' + i + '</p>'
		m = re.match('(.*)__(.*)__(.*)', i)
		if m:
			i = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
		m = re.match('(.*)_(.*)_(.*)', i)
		if m:
			i = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
		if in_list_append:
			i = '</ul>' + i
			in_list_append = False
		res += i
	if in_list:
		res += '</ul>'
	return res

import unittest


class MarkdownTest(unittest.TestCase):
	def test_parses_normal_text_as_a_paragraph(self):
		self.assertEqual(
			parse("This will be a paragraph"), "<p>This will be a paragraph</p>"
		)

	def test_parsing_italics(self):
		self.assertEqual(
			parse("_This will be italic_"), "<p><em>This will be italic</em></p>"
		)

	def test_parsing_bold_text(self):
		self.assertEqual(
			parse("__This will be bold__"), "<p><strong>This will be bold</strong></p>"
		)

	def test_mixed_normal_italics_and_bold_text(self):
		self.assertEqual(
			parse("This will _be_ __mixed__"),
			"<p>This will <em>be</em> <strong>mixed</strong></p>",
		)

if __name__ == "__main__":
	unittest.main()
