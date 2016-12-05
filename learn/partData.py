import xlrd
import numpy as np

workbook = xlrd.open_workbook('../data/training_set_rel3.xlsx', on_demand=True)
sheet = workbook.sheet_by_index(0)
data = np.load('traindata.npy')

data_num = 12978
set_num = 8

set_arr = np.zeros((data_num, 1), dtype=np.double)
rubric_range = [[2, 12], [1, 6], [0, 3], [0, 3], [0, 4], [0, 4], [0, 30], [0, 60]]

for i in range(data_num):
    set = sheet.cell(i + 1, 1).value
    label = sheet.cell(i + 1, 6).value

    set = int(set)
    # calculate new label
    xmin = rubric_range[set - 1][0]
    xmax = rubric_range[set - 1][1]
    new_label = (label - xmin) / (xmax - xmin)
    set_arr[i, 0] = new_label
    data[i, data.shape[1] - 1] = new_label

print(set_arr)
np.savetxt('traindata.txt', data)
np.save('traindata.npy', data)
