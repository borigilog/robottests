import xml.etree.ElementTree as XMLParser
class SettingsDicReader:
    def _convert_langcode(self, langCode):
        if langCode.upper() == 'D':
            return 'DE'
        if langCode.upper() == 'E':
            return 'EN'
        if langCode.upper() == 'F':
            return 'FR'
        if langCode.upper() == 'DE':
            return 'D'
        if langCode.upper() == 'EN':
            return 'E'
        if langCode.upper() == 'FR':
            return 'F'
        return ''
    def get_dic_text(self, path, regionName, dicId, langCode):
        root = XMLParser.parse(path)
        code = self._convert_langcode(langCode)
        xpath = 'DictionaryContent/Region[@Name="[NAME]"]/DicItem[@ID="[ID]"]/I[@L="[L]"]'
        xpath = xpath.replace("[NAME]", regionName).replace("[ID]", dicId).replace("[L]", code)
        item = root.find(xpath)
        text = item.get('C')
        return text
    def get_dictionary(self, path, regionName, dicId):
        root = XMLParser.parse(path)
        xpath = 'DictionaryContent/Region[@Name="[NAME]"]/DicItem[@ID="[ID]"]/I'
        xpath = xpath.replace("[NAME]", regionName).replace("[ID]", dicId)
        result = {}
        for items in root.findall(xpath):
            langCode = items.get('L')
            key = self._convert_langcode(langCode)
            if not key:
                continue
            value = items.get('C').strip()
            if value:
                result[key] = value
            print items.get('L')
            print items.get('C')
            print result
        return result