# Minimal Model Monitoring & Drift Detection

import random
import pickle

# 1. Create dataset
X_train = [[random.uniform(0,5) for _ in range(4)] for _ in range(80)]
y_train = [random.randint(0,2) for _ in range(80)]

X_test = [[random.uniform(0,5) for _ in range(4)] for _ in range(20)]
y_test = [random.randint(0,2) for _ in range(20)]

feature_names = ["feature1","feature2","feature3","feature4"]

# 2. Train simple model
class SimpleDecisionTree:
    def fit(self, X, y):
        self.majority_class = max(set(y), key=y.count)
    def predict(self, X):
        return [self.majority_class for _ in X]

model = SimpleDecisionTree()
model.fit(X_train, y_train)

with open("baseline_model.pkl","wb") as f:
    pickle.dump(model,f)

# 3. Simulate drift
X_new = [[x + random.uniform(-1,1) for x in row] for row in X_test]
y_new = y_test

# 4. Drift detection
print("Drift Detection (feature mean comparison):")
for i, f in enumerate(feature_names):
    train_mean = sum(row[i] for row in X_train)/len(X_train)
    new_mean = sum(row[i] for row in X_new)/len(X_new)
    drift = "Yes" if abs(new_mean - train_mean)>0.5 else "No"
    print(f"{f}: Train={train_mean:.2f}, New={new_mean:.2f}, Drift: {drift}")

# 5. Model performance
y_pred = model.predict(X_new)
accuracy = sum(1 for a,b in zip(y_pred,y_new) if a==b)/len(y_new)
print(f"\nNew Data Accuracy: {accuracy:.2f}")
if accuracy<0.5: print("⚠️ Model performance dropped!")
else: print("Model performance is stable.")
