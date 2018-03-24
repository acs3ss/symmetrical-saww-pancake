from io import StringIO
import json
import re

with open('raw-document.json', 'r') as file:
    paragraphList = []
    data = file.read()
    io = StringIO(data)
    test = json.load(io)
    blocks = test['responses'][0]['fullTextAnnotation']['pages'][0]['blocks']
    for block in blocks:
        paragraphs = block['paragraphs']
        for paragraph in paragraphs:
            words = paragraph['words']
            actualParagraph = ''
            for word in words:
                symbols = word['symbols']
                actualWord = ''
                for symbol in symbols:
                    actualWord += symbol['text']
                actualParagraph += actualWord + ' '
            for paragraph in re.split(r'\d\s?.\s?\d\d', actualParagraph):
                if not re.search(r"^[\d\s\.]*$", paragraph):
                    start = paragraph.find('(')
                    if start != -1:
                        end = paragraph.find(')')
                        if end != -1:
                            paragraph = paragraph[:start] + paragraph[end+1:]
                    paragraphList.append(paragraph)

    for paragraph in paragraphList:
        print(paragraph)
