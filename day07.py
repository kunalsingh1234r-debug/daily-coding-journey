from daytime import datetime 
import json
import os

class MetricPipeline:
    def __init__(self, run_id: str, learning_rate : float):
        self.run_id = run_id
        self.learning_rate = learning_rate
        self.epochs_completed = learning_rate
        self.epchs_completed = 0
        self.history = []
        