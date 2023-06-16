from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
from collections import Counter
import pandas as pd

with open(file='submission_complete.csv', mode='r', encoding='utf-8') as f:
	df = pd.read_csv(f)
	# data = df['submission_result_verdict', 'submission_code_length']
	# filt_1 = (df['submission_result_verdict']=='ACCCEPTED')
	# filt_2 = (df['submission_result_verdict']=='WRONG ANSWER')
	# filt_3 = (df['submission_result_verdict']=='RUNTIMEERROR') 
	x_list = df['submission_result_verdict'].tolist()
	y_list = df['submission_code_length'].tolist()

	plt.scatter(x_list, y_list)

	plt.title('繳交狀態跟code長度的關係')
	plt.xlabel('繳交狀態')
	plt.ylabel('code長度')

	plt.show()

# /Users/anniechen/Desktop
