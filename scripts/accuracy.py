from conf import ROOT_DIR as rd

def accuracy(inputFile: str) -> None:
    data = []
    with open(inputFile, 'r', encoding="utf-8") as input:
        for line in input.readlines():
            data.append(line.strip())

    falsecount = 0
    for i in range(len(data)):
        if i < 473:  # Till 473 we have english testcases
            if data[i] != 'en':
                falsecount += 1
        elif 473 <= i < 741:  # Till 741 we have dutch test cases
            if data[i] != 'nl':
                falsecount += 1
        elif 741 <= i < 1119:  # Till 1119 we have german test cases
            if data[i] != 'de':
                falsecount += 1
        elif 1119 <= i < 1593:  # Till 1593 we have french test cases
            if data[i] != 'fr':
                falsecount += 1

    per = ((len(data) - falsecount) / len(data)) * 100
    print(per)

accuracy(rd+'/dtresult.txt')
