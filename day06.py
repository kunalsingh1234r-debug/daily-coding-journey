
class MLProject:

    def __init__(self, name: str, framework: str):
        self.name = name
        self.framework = framework
        self.epochs = 0
        self.is_trained = False
        self.accuracy = 0.0

    def train(self, epochs: int, target_acc: float):
        """Simulates training the model across specified epochs."""
        self.epochs += epochs
        self.accuracy = target_acc
        self.is_trained = True
        print(f"[{self.name}] Trained for {epochs} epochs using {self.framework}.")

    def evaluate(self):
        """Evaluates model performance metrics."""
        if not self.is_trained:
            print(f"[{self.name}] Warning: Model has not been trained yet.")
            return

        print(f"\n--- Model Evaluation: {self.name} ---")
        print(f"Framework : {self.framework}")
        print(f"Epochs    : {self.epochs}")
        print(f"Accuracy  : {self.accuracy:.2%}")



if __name__ == "__main__":
   
    vision_model = MLProject(name="ImageClassifier", framework="PyTorch")
    tabular_model = MLProject(name="HousePricePredictor", framework="Scikit-Learn")

    
    vision_model.evaluate()  
    vision_model.train(epochs=10, target_acc=0.924)
    vision_model.evaluate()

    tabular_model.train(epochs=5, target_acc=0.887)
    tabular_model.evaluate()