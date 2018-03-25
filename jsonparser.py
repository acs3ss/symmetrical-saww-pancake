from io import StringIO
import json
import re
import math

with open('raw-document.json', 'r') as file:
    paragraphList = []
    data = file.read()
    io = StringIO(data)
    test = json.load(io)
    blocks = test['responses'][0]['fullTextAnnotation']['pages'][0]['blocks']
    block_list = []
    for block in blocks:
        lines = {}
        paragraphs = block['paragraphs']
        for paragraph in paragraphs:
            words = paragraph['words']
            actualParagraph = ''
            for word in words:
                word_list = []
                symbols = word['symbols']
                actualWord = ''
                for symbol in symbols:

                    height = symbol['boundingBox']['vertices'][3]['y']
                    word_list.append(symbol['text'])

                    actualWord += symbol['text']
                    if 'detectedBreak' in symbol['property'].keys():
                        if symbol['property']['detectedBreak']['type'] == "LINE_BREAK":
                            actualWord += "\n"
                        elif symbol['property']['detectedBreak']['type'] == "SPACE":
                            actualWord += " "
                actualParagraph += actualWord


                lines.setdefault(height, []).append(word_list)
        block_list.append(lines)

            # for paragraph in re.split(r'\d\s?.\s?\d\d', actualParagraph):
            #     if not re.search(r"^[\d\s\.]*$", paragraph):
            #         start = paragraph.find('(')
            #         if start != -1:
            #             end = paragraph.find(')')
            #             if end != -1:
            #                 paragraph = paragraph[:start] + paragraph[end+1:]
            #         paragraphList.append(paragraph)

for block_dict in block_list:
    previous_key_str = ""
    for key in sorted(block_dict.keys()):
        value = block_dict[key]
        strr = ""
        for line in value:
            for char in line:
                strr += char
            strr += " "

        if re.search(r"^[\d\s\.]*$", strr):  # if not all spaces, #, .
            continue

        start = strr.find('(')  #look for first parenthises
        if start != -1:
            strr = strr[:start]
        end = strr.find(')')
        if end != -1:
            continue

        match = re.search(r'\$?\s*\d+\s*\.\s*\d\d', strr)
        if match != None:
            strr = strr[:match.start()]

        print(strr)


        # if 0 < key - previous_key < 5:
        #     previous_key_str += strr
        # else:
        #     print(previous_key_str + strr)
        #     previous_key = key
        #     previous_key_str = ""


    # for paragraph in paragraphList:
    #     print(paragraph)


# for paragraph in re.split(r'\d\s?.\s?\d\d', strr):
#     if not re.search(r"^[\d\s\.]*$", paragraph):
#         start = paragraph.find('(')
#         if start != -1:
#             end = paragraph.find(')')
#             if end != -1:
#                 paragraph = paragraph[:start] + paragraph[end+1:]
#         paragraphList.append(paragraph)
