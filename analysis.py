import matplotlib.pyplot as plt
import seaborn as sns

class Analysis:
    
    def __init__(self, data):
        self.d = data
        sns.set(style="white")

    def bar_plot(self, column_no, file_name):
        plt.figure()
        sns.countplot(x=self.d.col[column_no], data=self.d.data)
        plt.show()
        plt.savefig(file_name, dpi=300)

    def histogram(self, column_no, file_name):
        plt.figure()
        sns.distplot(self.d.data[self.d.col[column_no]])
        plt.show()
        plt.savefig(file_name, dpi=300)