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
    answers['(c)'] = 0.008
    return answers


#-----------------------------------------------------------
def question2():
    answers = {}

    # type: bool
    answers['(a) A'] = True  

    # type: bool
    answers['(a) B'] = False 

    # type: bool
    answers['(a) C'] = False 

    # type: bool
    answers['(a) D'] = True  

    # type: bool
    answers['(b) A'] = True  

    # type: False
    answers['(b) B'] = False 

    # type: bool
    answers['(b) C'] = True  

    # type: bool
    answers['(b) D'] = False  

    # type: eval_float
    # The formulas should only use the variable 'p'. The formulas should be
    # a valid Python expression. Use the functions in the math module as
    # required.
    answers['(c) Weight update'] = 0.424 

    # type: float
    # the answer should be correct to 3 significant digits
    answers['(d) Weight influence'] = 1.528  
    return answers


#-----------------------------------------------------------
def question3():
    answers = {}

    # type: string
    answers['Agree?'] = "No"

    # type: explain_string
    answers['Explain'] = "Alan's technique of flipping a coin does not provide a genuine forecast; it's purely based on chance and lacks any real understanding of the stock market. For ensemble methods to be successful, the models involved must possess actual predictive capabilities, rather than relying on randomness."
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
    answers['(a) C1-TPR'] = "p"

    # type: eval_float
    answers['(a) C2-TPR'] = "2*p"

    # type: eval_float
    answers['(a) C1-FPR'] = "p"

    # type: eval_float
    answers['(a) C2-FPR'] = "2*p"

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
    answers['(i) Best classifier?'] = 'C2'

    # type: explain_string
    answers['(i) Best classifier, explain'] = "C2 outperforms C1 as it achieves a superior balance between precision and recall, as evidenced by its higher F1-score. Although C1 manages to keep its false positive rate low, it does so at the cost of a reduced recall, which results in a greater number of missed positive cases."

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
    answers['(a) precision for C0'] = '1/10'


    # type: eval_float
    answers['(a) recall for C0'] = "p"

    # type: eval_float
    answers['(b) F-measure of C0'] = "2 * (0.1 * p) / (0.1 + p)" or "2 * p / (1 + 10p)"


    # type: string
    # choices: ['yes', 'no', 'unknown']
    answers['C1 better than random?'] = "unknown"


    # type: float
    # What is the range of p for which C1 is better than random?  What is
    # "?" in the expression "p > ?"

    answers['p-range'] = 0.3
    return answers


#-----------------------------------------------------------
def question9():
    answers = {}

    # type: dict[string,float]
    # keys: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) metrics'] =  {
        'recall': 0.533,  # Rounded to three decimal places
        'precision': 0.615,  
        'F-measure': 0.571,  
        'accuracy': 0.88  
    }


    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) best metric?'] = "F-measure"

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) worst metric?'] = "accuracy"


    # type: explain_string
    answers['(ii) Explain your choices of best and worst metrics'] = "The F-measure stands out as the optimal metric since it encapsulates precision and recall, offering a comprehensive perspective on the classifier's efficacy in identifying the positive class — a vital consideration when dealing with imbalanced classes. In contrast, accuracy emerges as the least suitable metric here, given that it could present an overoptimistic view of performance amidst skewed class distributions, failing to accurately represent the model's ability to predict the minority class."
    return answers


#-----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    # choices: ['T1', 'T2']
    answers['(a) better test based on F-measure?'] = "T1"

    # type: string
    # choices: ['T1', 'T2']
    answers['(b) better test based on TPR/FPR?'] = "T2"

    # type: string
    # choices: ['F1', 'TPR/FPR']
    answers['(c) Which evaluation measure to use between the two tests?'] = "F1"

    # type: explain_string
    answers['(c) Which evaluation measure? Explain'] = "The F1 score is typically preferable when false positives and false negatives carry similar consequences and when achieving an equilibrium between precision and recall is important."

    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = "In situations where a disease is uncommon, and the repercussions of incorrect treatment due to false positives are substantial, or the emotional toll of false positives is intense, the TPR/FPR ratio is more desirable to minimize false positives. On the other hand, in circumstances where missing a diagnosis carries considerable danger, the F1 score would be emphasized to guarantee a more balanced detection of actual cases."
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
