import math


class DecisionNode:
    """
    Decision Node for Decision tree
    """
    __slots__ = 'question', 'trueBranch', 'falseBranch'

    def __init__(self, question, trueBranch, falseBranch):
        """
        Initializes the decision Node object
        :param question:        Question Object that splits the input rows
        :param trueBranch:      True branch Node
        :param falseBranch:     False branch Node
        """
        self.question = question
        self.trueBranch = trueBranch
        self.falseBranch = falseBranch


class Question:
    """
    Class question used to store question object and its value
    """
    __slots__ = 'column', 'featureValue'

    def __init__(self, column, featureValue):
        self.column = column
        self.featureValue = featureValue

    def match(self, example):
        """
        Return question value; True or False
        """
        val = example[self.column]
        return val

    def __repr__(self):
        """
        String representation of question
        """
        return "Question " + str(self.column + 1)


class Leaf:
    """
    Leaf class for prediction
    """
    __slots__ = 'prediction'

    def __init__(self, rows):
        self.prediction = classCount(rows)


def classCount(rows):
    """
    Counts the labels in list of rows
    :param rows:    Input rows
    :return:        Dictionary of labels with count as values
    """
    counts = {}
    for row in rows:
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts


def printLeaf(counts):
    """
    Returns the prediction values based on higher probability
    :param counts:  Dictionary of label counts
    :return:    Prediction
    """
    total = sum(counts.values()) * 1.0
    probs = {}
    for lbl in counts.keys():
        probs[lbl] = int(counts[lbl] / total * 100)
    maxprob = max(probs.values())  # Max probability label
    for key, value in probs.items():
        if value == maxprob:
            return key


def bestSplit(rows):
    """
    finds the best split for rows based on information gain
    :param rows:    input rows
    :return:    bestgain and question for splitting
    """
    bestGain = 0  # track best gain
    bestQuestion = None  # track best question
    uncertainty = entropyOf(rows)
    features = len(rows[0]) - 1  # total number of columns
    for col in range(features):
        values = set([row[col] for row in rows])  # unique values in the column
        for val in values:
            question = Question(col, val)
            trueRows, falseRows = split(rows, question)
            if len(trueRows) == 0 or len(falseRows) == 0:
                continue
            gain = informationGain(trueRows, falseRows, uncertainty)
            if gain > bestGain:
                bestGain, bestQuestion = gain, question
    return bestGain, bestQuestion


def informationGain(left, right, unCertainity):
    """
    Computes the information gain of a feature split
    :param left:    left branch
    :param right:   right branch
    :param unCertainity: Current uncertainity
    :return:
    """
    p = float(len(left)) / (len(left) + len(right))
    return unCertainity - p * entropyOf(left) - (1 - p) * entropyOf(right)


def entropyOf(rows):
    """
    Camputes the entropy of rows
    :param rows: input rows
    :return:    entropy
    """
    counts = classCount(rows)
    entropy = 0
    for lbl in counts:
        labelProbability = counts[lbl] / float(len(rows))  # probability
        entropy -= labelProbability * math.log2(labelProbability)
    return entropy


def createTree(rows):
    """
    Builds a decision tree recursively
    :param rows: input rows
    :return: root node of decision tree
    """
    gain, question = bestSplit(rows)
    if gain == 0:
        return Leaf(rows)
    trueRows, falseRows = split(rows, question)
    trueBranch = createTree(trueRows)  # True branch
    falseBranch = createTree(falseRows)  # False branch
    return DecisionNode(question, trueBranch, falseBranch)


def split(rows, question):
    """
    Partitions the rows based on question
    :param rows:        input rows
    :param question:    question/feature
    :return:
    """
    # partition rows based on question
    trueRows, falseRows = [], []
    for row in rows:
        if question.match(row):
            trueRows.append(row)
        else:
            falseRows.append(row)
    return trueRows, falseRows

def classify(row, node):
    """
    This method classifies data in a Decision tree
    :param row:     Test row
    :param node:    Current node
    :return:        Prediction
    """
    # Base case: Leaf node check and predict once reached
    if isinstance(node, Leaf):
        return node.prediction

    # Recursive cases
    if node.question.match(row):
        return classify(row, node.trueBranch)
    else:
        return classify(row, node.falseBranch)
