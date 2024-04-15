import pytest
from all_questions import *
import pickle



#-----------------------------------------------------------
def question1():
    answers = {}

    # type: float
    # Calculate the probability.
    answers['(a)'] = 0.0288

    # type: float
    # Calculate the probability.
    answers['(b)'] = 0.002

    # type: float
    # Calculate the probability.
    answers['(c)'] = 0.064
    return answers


#-----------------------------------------------------------
def question2():
    answers = {}

    # type: bool
    answers['(a) A'] = True  # Boosting reduces bias by focusing more on instances previous models misclassified.

    # type: bool
    answers['(a) B'] = False # Boosting does not employ parallel model training.

    # type: bool
    answers['(a) C'] = False # Boosting does not increase model diversity by training each model on a random subset.

    # type: bool
    answers['(a) D'] = True  # Boosting assigns weights to each training instance, adjusting these weights after each round.

    # type: bool
    answers['(b) A'] = True  # Boosting can increase the model's variance due to the high weight it may place on outliers.

    # type: False
    answers['(b) B'] = False # Boosting does not lead to underfitting, it places too much emphasis on instances that are hard to classify.

    # type: bool
    answers['(b) C'] = True  # The sequential nature of boosting can lead to increased training times compared to bagging.

    # type: bool
    answers['(b) D'] = True  # Boosting's focus on reducing bias makes it less susceptible to overfitting compared to other ensemble methods.

    # type: eval_float
    # The formulas should only use the variable 'p'. The formulas should be
    # a valid Python expression. Use the functions in the math module as
    # required.
    answers['(c) Weight update'] = 0.424  # The weight update factor alpha calculated from an error rate of 0.3.

    # type: float
    # the answer should be correct to 3 significant digits
    answers['(d) Weight influence'] = 1.528  # The new weight for an instance misclassified in the previous round.
    return answers


#-----------------------------------------------------------
def question3():
    answers = {}

    # type: string
    answers['Agree?'] = 'No'

    # type: explain_string
    answers['Explain'] =  'flipping a coin is purely random and does not use any real data to make predictions, Ensemble methods require classifiers that have some level of accuracy independently random guesses do not provide that'
    return answers


#-----------------------------------------------------------
def question4():
    answers = {}

    # type: bool
    answers['(a) e=0.5, independent'] = False

    # type: bool
    answers['(b), independent'] = True

    # type: bool
    answers['(c) identical'] = False
    return answers


#-----------------------------------------------------------
def question5():
    answers = {}

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(a)'] = None

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(b)'] = None

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(c)'] = None

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(d)'] = None
    return answers


#-----------------------------------------------------------
def question6():
    answers = {}

    # type: eval_float
    answers['(a) C1-TPR'] = None

    # type: eval_float
    answers['(a) C2-TPR'] = None

    # type: eval_float
    answers['(a) C1-FPR'] = None

    # type: eval_float
    answers['(a) C2-FPR'] = None

    # type: string
    # Hint: The random guess line in an ROC curve corresponds to TPR=FPR.
    # choices: ['yes', 'no']
    answers['(b) C2 better classifier than C1?'] = None

    # type: explain_string
    answers['(b) C2 better classifier than C1? Explain'] = None

    # type: string
    # choices: ['TPR/FPR', 'precision/recall']
    answers['(c) Which metric?'] = None

    # type: explain_string
    answers['(c) explain'] = None
    return answers


#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = None

    # type: explain_string
    answers['(i) Best classifier, explain'] = None

    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] = None

    # type: explain_string
    answers['(ii) appropriate metric pair, explain'] = None

    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = None

    # type: explain_string
    answers['(iii) best classifier, explain'] = None
    return answers


#-----------------------------------------------------------
def question8():
    answers = {}

    # type: eval_float
    answers['(a) precision for C0'] = None

    # type: eval_float
    answers['(a) recall for C0'] = None

    # type: eval_float
    answers['(b) F-measure of C0'] = None

    # type: string
    # choices: ['yes', 'no', 'unknown']
    answers['C1 better than random?'] = None

    # type: float
    # What is the range of p for which C1 is better than random?  What is
    # "?" in the expression "p > ?"

    answers['p-range'] = None
    return answers


#-----------------------------------------------------------
def question9():
    answers = {}

    # type: dict[string,float]
    # keys: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) metrics'] = None

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) best metric?'] = None

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) worst metric?'] = None

    # type: explain_string
    answers['(ii) Explain your choices of best and worst metrics'] = None
    return answers


#-----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    # choices: ['T1', 'T2']
    answers['(a) better test based on F-measure?'] = None

    # type: string
    # choices: ['T1', 'T2']
    answers['(b) better test based on TPR/FPR?'] = None

    # type: string
    # choices: ['F1', 'TPR/FPR']
    answers['(c) Which evaluation measure to use between the two tests?'] = None

    # type: explain_string
    answers['(c) Which evaluation measure? Explain'] = None

    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = None
    return answers
#-----------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
