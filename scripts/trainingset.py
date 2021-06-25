from conf import ROOT_DIR as rd


def createTrainSet(in1: str, in2: str, in3: str, in4:str, out: str) -> None:
    """
    Creates a training set from classified sets of languages
    :param in1: dutch file
    :param in2: german file
    :param in3: english file
    :param out: training set filename
    :return: None
    """
    with open(in1, 'r', encoding="utf-8") as inf:
        file1 = []
        for line in inf.readlines():
            file1.append(line)
    with open(in2, 'r', encoding="utf-8") as inf1:
        file2 = []
        for line in inf1.readlines():
            file2.append(line)
    with open(in3, 'r', encoding="utf-8") as inf2:
        file3 = []
        for line in inf2.readlines():
            file3.append(line)
    with open(in4, 'r', encoding="utf-8") as inf3:
        file4 = []
        for line in inf3.readlines():
            file4.append(line)
    with open(out, 'w', encoding="utf-8") as wnf:
        for i in range(max(len(file1), len(file2), len(file3))):
            if i < len(file1):
                wnf.write(file1[i])
            if i < len(file2):
                wnf.write(file2[i])
            if i < len(file3):
                wnf.write(file3[i])
            if i < len(file4):
                wnf.write(file4[i])


createTrainSet(rd + '/datafiles/dutchfinal.txt', rd + '/datafiles/germanfinal.txt', rd + '/datafiles/englishfinal.txt',
               rd + '/datafiles/frenchfinal.txt', rd + '/datasets/train.dat')
