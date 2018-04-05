import xml.etree.ElementTree as XMLParser
class SQLQueryReader:
    def get_query_by_name(self, path, queryName):
        root = XMLParser.parse(path)
        xpath = 'data[@name="[NAME]"]'
        xpath = xpath.replace("[NAME]", queryName)
        item = root.find(xpath)
        text = item.find('value').text
        return text