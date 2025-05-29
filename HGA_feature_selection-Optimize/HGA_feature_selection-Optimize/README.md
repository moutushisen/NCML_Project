The goal of this project is to apply Hybrid GA for feature reduction.
Fitness function uses random forest as a (binary) classifier.

syn_data_on_SCOM.ipynb:
	To generate Synthetic data based on SECOM dataset

HGA_with_synthetic_data (1).ipynb
	Original code has been modularized for better understanding, 
	population initialization now based on probability=desired features/total features to make more likely for the algorithm to focus on small subsets instead of larger ones in further generations.
	Stopped modifications of this file and instead renamed it to keep improving it --> HGA_generic.ipynb: 

HGA_generic.ipynb: 
07/05/25:
	Added alternative cell to use the combined SECOM dataset csv in the dataset subfolder
    Define the dataset folder path (the files are in a subfolder called dataset)
	Added printouts for better progress tracking.
	Evaluation of the population (fitness) is now parallelized with the evaluate_population() function.
08/05/25:
	Evaluate fitness population in parallel and saves each new pair individual, fitness in cache, population is pre-filtered so only individuals not in the cache are actually calculated. It could be improved if saved to disk, but then must review dataset splitting process. Although early convergence problem persists, current time is around 8 min for 10 generations, population=100 and desired number of features= 50. And results seems good: Result for Generation 10/10: Best Fitness = -0.5814, Features Selected = 29


unifies_dataset.py
	Script to unify the 2 files of SECOM dataset into a single .csv
	output file saved in the subfolder: dataset/SECOM_combined_dataset.csv
	

dataset folder:
	It contains the SECOM dataset:
	https://archive.ics.uci.edu/dataset/179/secom
	
	Attribute Information:
	Key facts: Data Structure: The data consists of 2 files the dataset file SECOM 
	consisting of 1567 examples each with 591 features a 1567 x 591 matrix and a labels 
	file containing the classifications and date time stamp for each example.

	The data is represented in a raw text file each line representing an individual 
	example and the features seperated by spaces. The null values are represented by 
	the 'NaN' value as per MatLab.
	