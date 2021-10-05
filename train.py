from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import StratifiedKFold


def load_distribution(file):
    return pd.read_csv(file, header=None).to_numpy()


# old experiment
# x_4 = load_distribution("distribution/tpcc/distribution4.txt")
# y_4 = np.load("exp_2.npy")
# x_5 = load_distribution("distribution/tpcc/distribution5.txt")
x = load_distribution("distribution/tpcc/tpcc_distribution.txt")
y = np.load("exp_2_thp.npy")

# x = np.concatenate((x_5, x_4), axis=0)
x = x / 100
# y = np.concatenate((y_5, y_4))
y = y / 24000
print(y)

regressor_dt = DecisionTreeRegressor(random_state=0)
regressor_dt.fit(x[0:40], y[0:40])

model = Sequential()
model.add(Dense(32, input_dim=5, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='mean_squared_error', optimizer='adam')


test_mse_sum = 0


history = model.fit(x[0:40], y[0:40], validation_data=(x[40:], y[40:]), epochs=200, verbose=0)
train_mse = model.evaluate(x[0:40], y[0:40], verbose=0)
test_mse = model.evaluate(x[40:], y[40:], verbose=0)
print(train_mse, test_mse)
print("--------------train----------------------")
for i in range(30, 50):
    if i == 40:
        print("--------------test----------------------")
    print(x[i]*100, model.predict(np.array([x[i]])) * 24000, y[i] * 24000)


# start the document

# try model on p99 metrics

# new experiment: start the db after each work
# hypothesis: restart help accuracy

# new experiment on tatp
# hypothesis: restart doesn't help a lot

# tpcc results with restart
# tatp results with restart/ no restart


# get all the results by next week
# make slides

# reasons
# analysis

# in what situation it is less accurate
# distribution might be more accurate
# train decision tree


