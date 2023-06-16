from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
from collections import Counter
import pandas as pd

#Q1
with open(file='submission_complete.csv', mode='r', encoding='utf-8') as f:
	df = pd.read_csv(f)
	filt = (df['challenge_title']=='PBC 110-1 HW4') 
	data = df.loc[filt, ['challenge_title', 'problem_label', 'submission_result_score']]
	problem_list = data['problem_label'].tolist()
	data_list = data['submission_result_score'].tolist()

	plt.scatter(problem_list, data_list)

	plt.title('The HW4 Score')
	plt.xlabel('Problem_label')
	plt.ylabel('submission_result_score')

	plt.show()

# /Users/anniechen/Desktop
