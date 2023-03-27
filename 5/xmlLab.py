import xml.etree.ElementTree as ET


class TemperatureConverter:
    @staticmethod
    def convert_celcius_to_fahrenheit(celcius):
        return 9/5 * celcius + 32

class ForecastXmlParser:

    def parse(self):
        tree = ET.parse('forecast.xml')
        root = tree.getroot()
        for item in root:
            print(f'{item[0].text}: {int(item[1].text)} Celcius, {TemperatureConverter.convert_celcius_to_fahrenheit(int(item[1].text))} Fahrenheit')


forcast = ForecastXmlParser()

forcast.parse()
