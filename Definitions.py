import re
import urllib.request

try: 
    word = input('Input the word that you want the definition of: ')
    url = 'https://www.dictionary.com/browse/' + word
    data = urllib.request.urlopen(url).read()
    data1 = data.decode('utf-8')

    m = re.search('<meta name="description" content="', data1)
    start = m.end()
    end = start + 300

    string = data1[start:end]

    m = re.search('See more.', string)
    end = m.start() - 1

    newString = string[0:end]
    print(newString)

except:
    print("Your word isn't in the dictionary.")