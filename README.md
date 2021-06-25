# Wikipedia Language Classification

This repository shows how we can use Decision Trees from scratch to classify Wikipedia text into English, German, French and Dutch classifiers.

## Considerations
* Features of language like Pronouns, Prepositions and Determiners are used to classify text.
* To train the decision tree model a training set of 9436(15 word sequences) is created.
* The model is tested against 1592 test sequences.
* An accuracy of 96% is observed for the above model.

## Requirements
No additional module installation is required. Python libraries used are ```sys```, ```pickle``` and ```re```

## Instructions
Create a decision tree object using the training set provided in ```\datasets```. This object is written on a file using ```pickle``` and later used to test any test set. 

* To train your decision tree based on training set pass below parameters:
 
  ```python3 run.py train <Train File\> <object File>```

  Example: ```python3 run.py train datasets/train.dat dt.pkl```

* To test any sequence pass below parameters:

  ```python3 run.py predict <Object File> <Test File>```

  Example: ```python3 run.py predict dt.pkl datasets/test.dat```

* A ```dtresult.txt``` file is created with output classifiers
 

## Helper Files and Scripts

File \| Directory  | Usage
------------- | -------------
```\scripts\accuracy.py```   | Used to test accuracy of model.
```\scripts\dataset.py```    | Used to convert raw text from Wikipedia into 15 word sequences.
```\scripts\trainingset.py```| Used to create a training set of mixed languages from language files.
```\datasets\```   | Contains training and test set.
```\datafiles\```   | Contains all raw wikipedia texts and processed files.



