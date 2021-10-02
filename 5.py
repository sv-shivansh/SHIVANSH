from pandas import read_excel, DataFrame

read = read_excel('./Book.xlsx')
print(type(read))

next = DataFrame.to_csv(read, index=False, header=False)
print(next)