import random
import math

import pandas as pd

df = pd.DataFrame(columns = ['a', 'b', 'p', 'n'])
################################################
num_hash_functions = 60
upper_bound_on_number_of_distinct_terms  = 10000000
#upper_bound_on_number_of_distinct_terms =   138492
#upper_bound_on_number_of_distinct_terms =  3746518

################################################


### primality checker
def is_prime(number):
	for j in range(2, int(math.sqrt(number)+1)):
		if (number % j) == 0:
			return False
	return True



set_of_all_hash_functions = set()
while len(set_of_all_hash_functions) < num_hash_functions:
	a = random.randint(1, upper_bound_on_number_of_distinct_terms-1)
	b = random.randint(0, upper_bound_on_number_of_distinct_terms-1)
	p = random.randint(upper_bound_on_number_of_distinct_terms, 10*upper_bound_on_number_of_distinct_terms)
	while is_prime(p) == False:
		p = random.randint(upper_bound_on_number_of_distinct_terms, 10*upper_bound_on_number_of_distinct_terms)
	#
	current_hash_function_id = tuple([a, b, p])
	set_of_all_hash_functions.add(current_hash_function_id)

for a, b ,p in set_of_all_hash_functions:
	df.loc[len(df)] = [a,b,p,upper_bound_on_number_of_distinct_terms]
df.to_csv('hash_functions/hash60.tsv', index = False, sep = '\t')

