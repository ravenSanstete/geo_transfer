## let us attain some statistics of the foursquare dataset
import csv
import pickle
import numpy as np
from scipy import stats
PREFIX = '/home/mlsnrs/data/pxd/dataset_tsmc2014/'

NY = 'dataset_TSMC2014_NYC.txt';

COUNT = 'counts.txt'
DES = 'deses.txt';
OUT_CTRL = False;

f = open(PREFIX + NY, 'r');


reader = csv.reader(f, delimiter = '\t');


counter = dict();

for row in reader:
    uid = int(row[0]);
    if(not (uid in counter)):
        counter[uid] = 0;
    counter[uid] += 1;
    
# counter = list(counter.values());


f.close();
print(len(counter));

f = open(PREFIX + NY, 'r');

reader = csv.reader(f, delimiter = '\t');


coords = dict();

for row in reader:
    uid = int(row[0]);
    if(not (uid in coords)):
        coords[uid] = np.zeros(shape = [counter[uid], 2]) 
    (coords[uid])[counter[uid]-1, 0] = row[4]
    (coords[uid])[counter[uid]-1, 1] = row[5]
    counter[uid] -= 1

print(len(coords));

deses = dict()

for key in coords:
    deses[key] = [stats.describe(coords[key][:, 0]), stats.describe(coords[key][:, 1])];

print(len(deses))
    
    


if(OUT_CTRL):
    f = open(PREFIX + COUNT, 'w+');
    f.write(pickle.dumps(counter));
    f.close();

f = open(PREFIX + DES, 'w+');
f.write(pickle.dumps(deses.values()));
f.close();


