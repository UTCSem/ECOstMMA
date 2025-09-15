
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import joblib, os

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'models', 'simple_model.joblib')

def train_dummy():
    X, y = make_classification(n_samples=500, n_features=6, n_informative=4, random_state=42)
    clf = RandomForestClassifier(n_estimators=50, random_state=42)
    clf.fit(X, y)
    os.makedirs(os.path.join(os.path.dirname(__file__), 'models'), exist_ok=True)
    joblib.dump(clf, MODEL_PATH)
    print('Saved model to', MODEL_PATH)

if __name__ == '__main__':
    train_dummy()
