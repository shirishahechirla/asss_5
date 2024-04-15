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
    answers['(a)'] = 'iii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(b)'] = 'i'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(c)'] = 'ii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(d)'] = 'iv'
    return answers


#-----------------------------------------------------------
def question6():
    answers = {}

    # type: eval_float
    answers['(a) C1-TPR'] = 0.1

    # type: eval_float
    answers['(a) C2-TPR'] = 0.2

    # type: eval_float
    answers['(a) C1-FPR'] = 0.1

    # type: eval_float
    answers['(a) C2-FPR'] = 0.2

    # type: string
    # Hint: The random guess line in an ROC curve corresponds to TPR=FPR.
    # choices: ['yes', 'no']
    answers['(b) C2 better classifier than C1?'] = 'no'

    # type: explain_string
    answers['(b) C2 better classifier than C1? Explain'] = "C2 is not a better classifier than C1, Both classifiers are random, and C2 simply predicts the positive class more frequently without improving accuracy."

    # type: string
    # choices: ['TPR/FPR', 'precision/recall']
    answers['(c) Which metric?'] = 'precision/recall'

    # type: explain_string
    answers['(c) explain'] = "Precision and recall are better metrics in this scenario. C2 has a higher recall than C1 better at finding all positive samplewhile precision remains the same identical proportion of true positives among all positive predictions."
    return answers


#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = 'C1'

    # type: explain_string
    answers['(i) Best classifier, explain'] = "C1 is better than C2 as it has lower false positive rate and higher precision."

    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] = 'precision-recall-F1-Measure'

    # type: explain_string
    answers['(ii) appropriate metric pair, explain'] = "Precision, recall, and F1-measure provide a balanced view of classifier performance, considering both the cost of false positives and the ability to identify true positives."

    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = 'C3'

    # type: explain_string
    answers['(iii) best classifier, explain'] = "C3 is the preferred classifier as it has the highest precision without compromising too much on recall and FPR."

    return answers


#-----------------------------------------------------------
def question8():
    answers = {}

    # type: eval_float
    answers['(a) precision for C0'] = precision_C0_val


    # type: eval_float
    answers['(a) recall for C0'] = recall_C0_val

    # type: eval_float
    answers['(b) F-measure of C0'] = F_measure_C0_val


    # type: string
    # choices: ['yes', 'no', 'unknown']
    answers['C1 better than random?'] = 'yes' if F_measure_C0_val < 0.15 else 'no'


    # type: float
    # What is the range of p for which C1 is better than random?  What is
    # "?" in the expression "p > ?"

    answers['p-range'] = p_range[0].evalf()
    return answers


#-----------------------------------------------------------
def question9():
    answers = {}

    # type: dict[string,float]
    # keys: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) metrics'] =  {
        'recall': 0.533,  # Rounded to three decimal places
        'precision': 0.615,  # Rounded to three decimal places
        'F-measure': 0.571,  # Rounded to three decimal places
        'accuracy': 0.88  # Rounded to two decimal places
    }


    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) best metric?'] = 'accuracy'

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) worst metric?'] = 'precision'


    # type: explain_string
    answers['(ii) Explain your choices of best and worst metrics'] = 'Accuracy is the best single metric as it considers all correct predictions over the total number of cases, which is crucial for imbalanced classes. Precision is the worst because it only looks at the subset of predicted positives, ignoring the true negatives, which are predominant in this case.'

    return answers


#-----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    # choices: ['T1', 'T2']
    answers['(a) better test based on F-measure?'] = 'T1'

    # type: string
    # choices: ['T1', 'T2']
    answers['(b) better test based on TPR/FPR?'] = 'T2'

    # type: string
    # choices: ['F1', 'TPR/FPR']
    answers['(c) Which evaluation measure to use between the two tests?'] = 'TPR/FPR'

    # type: explain_string
    answers['(c) Which evaluation measure? Explain'] = 'TPR/FPR is preferred in cancer detection due to the high cost associated with false negatives,and this ratio ensures fewer false positives relative to true positives.'

    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = 'In a scenario where the condition being tested for has minimal health consequences or treatment is non-invasive,the precision and balance of F1-Score would be more important to avoid over-treatment.'
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
