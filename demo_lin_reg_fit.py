import pickle
from sklearn.linear_model import LinearRegression

Age = [[23], [25], [30], [45], [50]]
Salary = [200000, 350000, 600000, 1200000, 1900000]

model = LinearRegression()
model.fit(Age, Salary)

# Save the trained model using pickle
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)
