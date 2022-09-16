from pathlib import Path
import math

directory = Path('blocks')
acids = dict()
freq = dict()
ex_freq = dict()
observed = dict()
obsfreq = dict()
result = dict()
thesum = 0

for file in directory.iterdir():
	fh = open(file)
	for acid in fh.read():
		acids[acid] = acids.get(acid, 0) + 1

acids.pop("\n")
sum = sum(acids.values())

for key, value in acids.items():
	freq[key] = acids.get(key)/sum

for key, i in freq.items():
	for key2, j in freq.items():
		ex_freq[f'{key}{key2}'] = i*j

for file in directory.iterdir():
	fh2 = open(file)
	file_col_ac = dict()
	c = 0
	for line in fh2:
		c +=1
		for pos, ac in enumerate(line.rstrip()):
			if pos not in file_col_ac: file_col_ac[pos] = {}
			file_col_ac[pos][ac] = file_col_ac[pos].get(ac, 0) +1
	for col in file_col_ac.values():
		for key, j in col.items():
			for key2, k in col.items():
				if key not in observed:
					observed[key] = {}
				observed[key][key2] = observed[key].get(key2, 0) + (j*k if key != key2 else j*(j-1)*0.5)
	thesum += c*(c-1)*0.5*(len(file_col_ac))

for key, value in observed.items():
	for key2, value2 in value.items():
		O = round(value2/thesum, 7)
		if key not in result: result[key] = {}
		result[key][key2] = math.floor(2*math.log((O/ex_freq[f'{key}{key2}']),2))



print(end='  ')
for key in sorted(result):
	print(f'{key:>3}', end='')
print()
for key in sorted(result):
	print(key, end=' ')
	for key2 in sorted(result):
		print(f'{result[key2][key]:>3}', end="")
	print()





