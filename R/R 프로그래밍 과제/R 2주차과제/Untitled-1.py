import numpy as np

num_list = np.array(range(1,46))
lotto = np.random.choice(num_list, 6, replace=False)
lotto.sort()
print('추출된 번호 : {}'.format(lotto))