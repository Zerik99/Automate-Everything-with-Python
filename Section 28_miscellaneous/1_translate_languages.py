from googletrans import Translator

translator = Translator()

translation = translator.translate("Hello World", dest="es").text

print(translation)
