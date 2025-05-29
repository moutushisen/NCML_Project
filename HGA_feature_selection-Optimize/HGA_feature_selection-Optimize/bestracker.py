import pandas as pd
import os
from pathlib import Path

# Define the results folder path 
results_folder = Path('results')

# Define file paths
results_file = results_folder / 'best_chromosomes.csv'

class BestTracker:
    def __init__(self, save_path= results_file ):
        self.save_path = save_path
        self.records = []  # List of bests per generation
        self.best_fitness_so_far = None  # Tracks best fitness so far

        # Load existing file to get the last experiment number
        if os.path.exists(self.save_path):
            existing_df = pd.read_csv(self.save_path, sep=';')
            self.experiment_number = existing_df['experiment'].max() + 1
        else:
            self.experiment_number = 1

    def update(self, fitness, features, number_of_features, generation,
                crossover_operator_point, mutation_coef, population_size, selection_coef,
                strategy, expectedFitness, classif_model, goal_features_number,
                penalty_coef, num_elite, crossover_rate,
                **kwargs):
        # If new best fitness found
        if (self.best_fitness_so_far is None) or (fitness > self.best_fitness_so_far):
            self.best_fitness_so_far = fitness

            record = {
                'experiment': self.experiment_number,
                'fitness': fitness,
                'features': features,
                'number_of_features': number_of_features,
                'generation': generation,
                'selection_coef': selection_coef,
                'crossover_operator_point': crossover_operator_point,
                'crossover_rate': crossover_rate,
                'mutation_coef': mutation_coef,
                'penalty_coef': penalty_coef,
                'population_size': population_size,
                'strategy': strategy,
                'num_elite': num_elite,                
                'expectedFitness': expectedFitness,
                'classif_model': classif_model,
                'goal_features_number': goal_features_number,                
                **kwargs  # For extra attributes
            }

            self.records.append(record)

    def save(self):
        if not self.records:
            print("No records to save.")
            return

        # Convert to DataFrame
        df_new = pd.DataFrame(self.records)

        # Append to file
        if os.path.exists(self.save_path):
            df_existing = pd.read_csv(self.save_path, sep=';')
            df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        else:
            df_combined = df_new

        df_combined.to_csv(self.save_path, sep=';', index=False)
        print(f"{len(self.records)} best records saved to {self.save_path}")
