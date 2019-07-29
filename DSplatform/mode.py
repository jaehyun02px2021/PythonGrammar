import src.formatting as formatting
import src.SurveyInput as SurveyInput
import src.Plotting as Plotting
import src.Reporting as Reporting
import src.LeastSquare as LeastSquare

modeHeader = """
====={}====
"""

modeOption = "{}. {} : {} " # index. name : explanation

modeFooter = """
================
Select Mode : """



class mode:
    def __init__(self, name, explanation, children, feature ):
        self.name = name
        self.explanation = explanation
        self.feature = feature
        self.children = children

    def start(self) :
        print(modeHeader.format(self.name))
        for index, value in enumerate(self.children):
            print(modeOption.format(index + 1, value.name, value.explanation))
        if len(self.children) :
            temp = int(input(modeFooter))
            self.children[temp - 1].start()
        else :
            for features in self.feature:
                features()

# additional method :
# 1. press * to go back


Research = mode("Research", "sdgf", [], [])
Survey = mode("Survey", "sdg", [], [SurveyInput.SurveyInput])

Reporting = mode("Reporting", "asdf", [], [Reporting.Reporting])
Plotting = mode("Plotting", "daf", [], [Plotting.Plotting])
LeastSquare = mode("LeastSquare", "dfdfd", [], [LeastSquare.LeastSquare])


Analyzing = mode("Analyzing", 'SFD', [Reporting, Plotting, LeastSquare],[])
Formating = mode("Formating", "dsg", [], [formatting.formatting])
Gathering = mode("Gathering", "asdf", [Research, Survey], [])


Welcome = mode("Welcome", "start", [Gathering, Formating, Analyzing], [])
