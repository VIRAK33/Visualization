import os

import flask
from flask import Blueprint, render_template, request


bargraph = Blueprint('bargraph', __name__)
heatmap = Blueprint('heatmap', __name__)

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@bargraph.route("/bargraph", methods=['GET', 'POST'])
def data_barplot():

    if flask.request.method == 'POST':
        from flask import request
        dataframe = request.files.get('file')
        dataframe.save(os.path.join('static/dataframes/', dataframe.filename))
        df1 = pd.read_csv(os.path.join('static/dataframes/', dataframe.filename))

        df1.columns = ['Surname', 'First name', 'Email address', 'State', 'Started on', 'Completed', 'Time taken', 'Score', \
                       'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15',
                       'q16', 'q17', 'q18', 'q19', 'q20']

        df2 = df1[
            ['First name', 'Score', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14',
             'q15', 'q16', 'q17', 'q18', 'q19', 'q20']]

        df2 = df2.sort_values(by='First name')

        plt.figure(figsize=(4, 6), dpi=250)
        g2 = sns.barplot(x="Score", y="First name", data=df2)
        for p in g2.patches:
            percentage = '{:.1f}'.format(p.get_width())
            x = p.get_x() + p.get_width() + 0.02
            y = (p.get_y() + p.get_height() / 2) + 0.15
            g2.annotate(percentage, (x, y))

        plt.title("Final exam result")
        plt.xlabel('Final Exam Score')
        plt.ylabel('Student Name')
        plt.savefig('./static/images/final exam result.png', bbox_inches='tight')
        # plt.show()



    return render_template('upload.html')

@heatmap.route("/heatmap", methods=['GET', 'POST'])
def data_heatmap():
    return 'Heatmap'