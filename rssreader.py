#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import webapp2
import jinja2
import os
import urllib
from xml.dom import minidom, Node


jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class IndexPage(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(self.init())
	
	def post(self):
		self.response.out.write(self.init())
	
	def init(self):
		rss_reader = RSSReader('http://feeds.feedburner.com/PioneersFestival?format=xml') #add feed url to RSS Reader - tested with feedburner
		items = rss_reader.GetItems()
		
		template_values = {
			"items": items
		}

		template = jinja_environment.get_template('templates/index.html')

		return template.render(template_values)


class RSSItem:
	"""This is an RSS item, it contain all the RSS info like Tile and Description"""
	def __init__(self,item_node):
		self.title = self.GetChildText(item_node,"title")
		self.link = self.GetChildText(item_node, "link")
		self.pubDate = self.GetChildText(item_node, "pubDate")
		self.description = self.GetChildText(item_node,"description")

	
	def GetItemText(self,xml_node):
		"""Get the text from an xml item"""
		text = ""
		for text_node in xml_node.childNodes:
			if (text_node.nodeType == Node.TEXT_NODE):
				text += text_node.nodeValue
			elif (text_node.nodeType == 4): #CDATA Node Type
				text += text_node.nodeValue

		return text
	
	def GetChildText(self, xml_node, child_name):
		"""Get a child node from the xml node"""
		if (not xml_node):
			print "Error GetChildNode: No xml_node"
			return ""
		for item_node in xml_node.childNodes:
			if (item_node.nodeName==child_name):
				logging.info("++++ founded " + child_name)
				return self.GetItemText(item_node)
		"""Return Nothing"""
		return ""

class RSSReader:
	"""This class is an RSS reader, it should have a better docstring"""
	
	def __init__(self,RSSUrl):
		"""Initialize the class"""
		self.items = []
		self.RSSUrl = RSSUrl
		self.xmldoc = self.GetXMLDocument(RSSUrl)
		if (not self.xmldoc):
			print "Error Getting XML Document!"
		
	def GetXMLDocument(self,RSSUrl):
		"""This function reads in a RSS URL and then"""
		"""returns the XML document on success"""
		url_info = urllib.urlopen(RSSUrl)
		xmldoc = None
		if (url_info):
			xmldoc = minidom.parse(url_info)
		else	:
			print "Error Getting URL"
		return xmldoc
	
	def GetItems(self):
		"""Generator to get items"""
		for item_node in self.xmldoc.documentElement.childNodes:
			if (item_node.nodeName == "channel"):
				for child_node in item_node.childNodes:
					if (child_node.nodeName == "item"):
						"""Allright we have an item"""
						rss_item = RSSItem(child_node)
						self.items.append(rss_item)
		return self.items



app = webapp2.WSGIApplication([('/.*', IndexPage)], debug=True)

