## to obtain more global stats directly from the descriptions

import pickle

file_path = '/home/mlsnrs/data/pxd/dataset_tsmc2014/deses.txt'

desps = pickle.load(open(file_path, 'r'));

minimum = [361.0, 361.0];
maximum = [-361.0, - 361.0];

for desp in desps:
    minmax = desp[0].minmax
    if(minmax[0] < minimum[0]):
        minimum[0] = minmax[0];
    if(minmax[1] > maximum[0]):
        maximum[0] = minmax[1];
    minmax = desp[1].minmax;
    if(minmax[0] < minimum[1]):
        minimum[1] = minmax[0];
    if(minmax[1] > maximum[1]):
        maximum[1] = minmax[1];

print(minimum)
print(maximum)
