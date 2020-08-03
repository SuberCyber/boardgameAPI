import os, glob, re

folder_path = '../gameSource'

def formatting(field, file):
    if field:
        field = field.group()
        file.write(field)
        file.write(',')

with open ('listOfGamesInfo.json', 'w') as listOfGamesInfo:
    listOfGamesInfo.write('[')
    for filename in glob.glob(os.path.join(folder_path, '*')):
        if not ".txt" in filename and not ".sh" in filename and not "accessory" in filename and not "traditional" in filename:
            print(filename[14:])
            listOfGamesInfo.write('{')
            with open(filename, 'r', encoding = 'cp850') as f:
                text = f.read()
                formatting(re.search(r"\"rankinfo\":\[.*?\]",text), listOfGamesInfo)
                formatting(re.search(r"\"playerage\":\"[0-9][0-9]?\+?\"", text), listOfGamesInfo)
                formatting(re.search(r"\"averageweight\":[0-9]\.[0-9]*", text), listOfGamesInfo)
                 # could add community player recs
                formatting(re.search("\"minplayers\":\"[0-9][0-9]?\"", text), listOfGamesInfo)
                formatting(re.search("\"maxplayers\":\"[0-9][0-9]?\"",text), listOfGamesInfo)
                formatting(re.search("\"minplaytime\":\"[0-9][0-9]?[0-9]?\"", text), listOfGamesInfo)
                formatting(re.search("\"maxplaytime\":\"[0-9][0-9]?[0-9]?\"", text), listOfGamesInfo)
                formatting(re.search(r'"boardgamecategory":\[.*?\]', text), listOfGamesInfo)
                formatting(re.search(r'"boardgamemechanic":\[.*?\]', text), listOfGamesInfo)
                formatting(re.search(r'"boardgamesubdomain":\[.*?\]', text), listOfGamesInfo)

            with open(filename, 'r', encoding ='utf-8') as f:
                text = f.read()

                title= re.search(r'meta name="title" content=".*?"', text)
                print(title)
                if title:
                    title = title.group()
                    # print(title[26:])
                    listOfGamesInfo.write('"fancyTitle":')
                    listOfGamesInfo.write(title[26:])
                    listOfGamesInfo.write(",")
                link = re.search(r'https://boardgamegeek.com/boardgame/[0-9]*/', text)
                if link:
                    link = link.group()
                    # print(link+filename[14:])
                    listOfGamesInfo.write('"link":"'+link+filename[14:]+'",')
                listOfGamesInfo.write('"name":"' +  filename[14:] + '"}')
                # TODO: add spacing to names
                if "zombies" not in filename:
                    listOfGamesInfo.write(',')
    listOfGamesInfo.write(']')
