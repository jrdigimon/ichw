'''wcount.py:count words from an Internet file.'''
import sys
from urllib.request import urlopen
import urllib

def wcount(text, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    import string
    text = text.lower()
    for mark in string.punctuation:
        text = text.replace(mark, ' ')        
    line = text.splitlines()
    words = []
    for i in line:
        words = words + i.split()
    histogram = dict()
    for word in words:
        histogram[word] = histogram.get(word, 0) + 1
    lst = list(histogram.items())
    lst2 = []
    lst3 = []
    for k,v in lst:
        lst2 = lst2 + [(v,k)]
    lst2 = sorted(lst2, reverse = True)
    for k,v in lst2:
        lst3 = lst3 + [(v,k)]
    for i in range(min(topn,len(lst3))):
        print(lst3[i][0],lst3[i][1])
    pass

if __name__ == '__main__':

    if len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    url = sys.argv[1]
    if len(sys.argv) == 2:
        topn = 10
    else:
        topn = int(sys.argv[2])
    try:
        web_file = urlopen(url)
        lines_byte = web_file.read()
        web_file.close()
        lines = bytes.decode(lines_byte)
        wcount(lines, topn)
    except urllib.request.URLError:
        sys.stdout.write('Web path unexist or denied request!')
    except ValueError:
        sys.stdout.write('Unsupported url format "{}" !'.format(url))
    except Exception:
        sys.stdout.write('Other unpredictable error, please ensure the url starts with "http://" and check your spelling')
