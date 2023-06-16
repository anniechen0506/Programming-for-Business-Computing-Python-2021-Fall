from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
from collections import Counter
import pandas as pd

with open(file='submission_complete.csv', mode='r', encoding='utf-8') as f:
	df = pd.read_csv(f)

	mean_list = []
	challenge_list = []
	filt_1 = (df['challenge_title']=='PBC 110-1 HW1')
	data_1 = df.loc[filt_1, ['challenge_title', 'problem_label', 'submission_result_score']]
	mean_1 = data_1['submission_result_score'].mean()
	mean_list.append(mean_1)

	filt_2 = (df['challenge_title']=='PBC 110-1 HW2')
	data_2 = df.loc[filt_2, ['challenge_title', 'problem_label', 'submission_result_score']]
	mean_2 = data_2['submission_result_score'].mean()
	mean_list.append(mean_2)

	filt_3 = (df['challenge_title']=='PBC 110-1 HW3')
	data_3 = df.loc[filt_3, ['challenge_title', 'problem_label', 'submission_result_score']]
	mean_3 = data_3['submission_result_score'].mean()
	mean_list.append(mean_3)

	filt_4 = (df['challenge_title']=='PBC 110-1 HW4')
	data_4 = df.loc[filt_4, ['challenge_title', 'problem_label', 'submission_result_score']]
	mean_4 = data_4['submission_result_score'].mean()
	mean_list.append(mean_4)

	filt_5 = (df['challenge_title']=='PBC 110-1 HW5')
	data_5 = df.loc[filt_5, ['challenge_title', 'problem_label', 'submission_result_score']]
	mean_5 = data_5['submission_result_score'].mean()
	mean_list.append(mean_5)

	filt_6 = (df['challenge_title']=='PBC 110-1 HW6')
	data_6 = df.loc[filt_6, ['challenge_title', 'problem_label', 'submission_result_score']]
	mean_6 = data_6['submission_result_score'].mean()
	mean_list.append(mean_6)

	filt_7 = (df['challenge_title']=='PBC 110-1 HW7')
	data_7 = df.loc[filt_7, ['challenge_title', 'problem_label', 'submission_result_score']]
	mean_7 = data_7['submission_result_score'].mean()
	mean_list.append(mean_7)

	# print(mean_list)
	challenge_list.append('HW1')
	challenge_list.append('HW2')
	challenge_list.append('HW3')
	challenge_list.append('HW4')
	challenge_list.append('HW5')
	challenge_list.append('HW6')
	challenge_list.append('HW7')

	plt.plot(challenge_list, mean_list)

	plt.title('每份作業中每一題的全班平均成績')
	plt.xlabel('每份作業')
	plt.ylabel('全班在每份作業中每一題的平均成績')

	plt.show()

# /Users/anniechen/Desktop
