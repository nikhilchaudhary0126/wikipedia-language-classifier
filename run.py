"""
file: run.py
description:
This program tests a wikipedia 15 word line and classifies it as english, dutch, german or french using decision trees.

language: python3
"""

# imports
import sys
import pickle
from decisiontree import createTree, DecisionNode, printLeaf, classify

# FEATURES LIST
DUTCH_PRONOUNS = ['lk', 'jij', 'je', 'u', 'hij', 'zij', 'ze', 'wij', 'jullie', 'mij', 'jou', 'hem', 'haar', 'ons',
                  'hen''mijn', 'mijne', 'jouw', 'jouwe', 'uw', 'uwe', 'zijn', 'onze', 'hun']
DUTCH_PREPOSITION = ['bij', 'aan', 'van', 'naar', 'te', 'uit', 'om', 'tot', 'samen', 'op',
                     'naast', 'behalve', 'nabij', 'dichtbij', 'tegenover', 'jegens', 'tegen']
DUTCH_DETERMINERS = ['het', 'een']
ENGLISH_PRONOUNS = ['i', 'you', 'he', 'she', 'it', 'they', 'him', 'her', 'us', 'them', 'my', 'your', 'his', 'our',
                    'their']
ENGLISH_PREPOSITION = ['at', 'to', 'with', 'be', 'by', 'upon', 'towards', 'beside']
ENGLISH_DETERMINERS = ['the', 'a', 'an']
GERMAN_PRONOUNS = ['ich', 'mich', 'mir', 'dich', 'dir', 'er', 'ihn', 'ihm', 'sie', 'es', 'wir', 'uns',
                   'euch', 'ihnen']
GERMAN_PREPOSITION = ['bis', 'durch', 'entlang', 'um', 'gegen', 'ohne', 'aus', 'bei', 'mit', 'nach', 'seit', 'von',
                      'zu', 'der', 'das', 'dieser', 'jeder', 'jener', 'mancher', 'solcher', 'welcher', 'alle']
GERMAN_DETERMINERS = ['ein', 'kein', 'mein', 'dein', 'sein', 'ihr', 'euer', 'unser']
FRENCH_PRONOUNS = ['je', 'j’', 'nous', 'tu', 'vous', 'il', 'elle', 'elles', 'ils']
FRENCH_PREPOSITION = ['avant', 'après', 'vers', 'depuis', 'pendant', 'pour', 'à', 'au-', 'autour de', 'chez', 'dans',
                      'derrière', 'devant', 'parmi', 'sous', 'sur', 'en', 'loin de']
FRENCH_DETERMINERS = ['le', 'la', 'les', 'un', 'une', 'des', 'de la', 'del', 'ce', 'cet', 'cette', 'ces', 'mon',
                      'ma', 'mes', 'moins']
FEATURES = [DUTCH_PRONOUNS, DUTCH_PREPOSITION, DUTCH_DETERMINERS, ENGLISH_PRONOUNS, ENGLISH_PREPOSITION,
            ENGLISH_DETERMINERS, GERMAN_PRONOUNS, GERMAN_PREPOSITION, GERMAN_DETERMINERS, FRENCH_PRONOUNS,
            FRENCH_PREPOSITION, FRENCH_DETERMINERS]
# Subordinate checks
DUTCH_SUBORDINATE_CONSTRUCTIONS = ['-ie', 'z\'n', 'd\'r', 'haar-']
ENGLISH_SUBORDINATE_CONSTRUCTIONS = ['q', 'x', 'Q', 'X']


def main():
    """
    Main function to pass runtime parameters and call train and predict methods
    :return:    None
    """
    entryPoint = sys.argv[1]
    if entryPoint == "train":
        examples = sys.argv[2]  # file containing labeled examples
        hypothesisOut = sys.argv[3]  # specifies the file name to write your model to.
        train(entryPoint, examples, hypothesisOut)

    if entryPoint == "predict":
        hypothesis = sys.argv[2]  # hypothesis is a trained decision tree or ensemble created by your train program
        file = sys.argv[3]  # file is a file containing lines of 15 word sentence fragments in either English or Dutc
        predict(entryPoint, hypothesis, file)


def generateFeatures(operation, dataList: list) -> list:
    """
    Processes every line in dataset and creates boolean list with feature boolean values

    :param operation:   train or predict
    :param dataList:    input file
    :return:    boolean list of features
    """
    booleanData = []
    for item in dataList:
        row = []
        if operation == "train":  # Classifier passed while training
            words = item[0].split()
        else:
            words = item.split()  # Empty result classifier for test
        # Language Classifiers check; feature 1 to 9
        for index in range(len(FEATURES)):
            flag = False
            for word1 in words:
                for word2 in FEATURES[index]:
                    if word1.lower() == word2:
                        flag = True
            row.append(flag)
        # Subordinate Constructions Check
        dutchSubFlag = False
        for subword in DUTCH_SUBORDINATE_CONSTRUCTIONS:
            if subword in item[0]:
                dutchSubFlag = True
        row.append(dutchSubFlag)
        engSubFlag = False
        for subword in ENGLISH_SUBORDINATE_CONSTRUCTIONS:
            if subword in item[0]:
                engSubFlag = True
        row.append(engSubFlag)
        if operation == "train":
            row.append(item[1])  # classifier
        else:
            row.append("")
        booleanData.append(row)
    return booleanData


def train(operation: str, examples: str, hypothesisOut: str) -> None:
    """
    Training method used to train inputset based on learning type
    :param examples:        file containing labeled examples
    :param hypothesisOut:   file name to write your model to
    :return:
    """
    trainingRawData = []  # All input lines
    with open(examples) as trainfile:
        for line in trainfile.readlines():
            temp = line.split('|')
            temp.reverse()
            trainingRawData.append(temp)
    trainingData = generateFeatures(operation, trainingRawData)

    decisionTree = createTree(trainingData)
    with open(hypothesisOut, 'wb') as hypOut:
        pickle.dump(decisionTree, hypOut, pickle.HIGHEST_PROTOCOL)
    print("Decision Tree object serialized in file:", hypothesisOut)


def predict(operation, hypothesis, file):
    """
    Predict method used for predicting based on learning objects written in hypothesis file
    :param hypothesis:  hypothesis file
    :param file:        test file
    :return:    None. Prints predictions
    """
    testDataStrings = []
    with open(file, 'r') as inf:
        for line in inf.readlines():
            testDataStrings.append(line)
    testData = generateFeatures(operation, testDataStrings)

    with open(hypothesis, 'rb'):
        object = pickle.load(open(hypothesis, 'rb'))  # Get written object

    # Determine the learning method based on object stored
    if isinstance(object, DecisionNode):
        with open("dtresult.txt", "w") as wnf:
            for row in testData:
                wnf.write(printLeaf(classify(row, object)) + "\n")


if __name__ == '__main__':
    main()
