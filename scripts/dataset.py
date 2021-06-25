import re
from conf import ROOT_DIR as rd


def convert(inputFile: str, outputFile: str) -> None:
    """
    Converts raw input text into plain sentences by removing loan words in braces
    :param inputFile:   input file
    :param outputFile:  output file
    :return:    None
    """
    with open(inputFile, 'r', encoding="utf-8") as inf:
        with open(outputFile, 'w', encoding="utf-8") as wnf:
            for line in inf.readlines():
                t = re.sub(r'\(.+?\)', '', line)
                t1 = re.sub(r'\[.+?\]', '', t)
                t2 = re.sub(r'".+?"', '', t1)
                wnf.write(t2)


def splitLines(inputFile: str, outputFile: str, lc: str) -> None:
    """
    splits the input file into 16 word sequences file with classifier

    :param inputFile:   input file
    :param outputFile:  output file
    :param lc:  language code classifier
    :return:    None
    """
    lc += "|"
    with open(inputFile, 'r', encoding="utf-8") as inf:
        with open(outputFile, 'w', encoding="utf-8") as wnf:
            for line in inf.readlines():
                words = line.split()
                count = 1
                line = lc
                for word in words:
                    if count < 16:
                        line += word + ' '
                        count += 1
                    if count == 16:
                        wnf.write(line.strip() + "\n")
                        count = 1
                        line = lc


convert(rd + '/datafiles/french.txt', rd + '/datafiles/temp.txt')
splitLines(rd + '/datafiles/temp.txt', rd + '/datafiles/frenchfinal.txt', 'fr')
