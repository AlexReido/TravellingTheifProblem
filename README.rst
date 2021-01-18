GECCO 2019 Competition - Bi-objective Traveling Thief Problem
TEAM EPSILON
============================================================
Python 3.8 is required.

We have two working implementations "PyThief" and "PyThief2"
We are submiting them both to fully illustrate our developement.
First running PyThief:

Run the Pytheif/src/main/__init__.py

This will run the NTGA algorithm for the test problem on line 15
and write the results to the directtory TravellingThief/results/
This includes the .x files and .f files.

Second we have PyThief2:

Configure the .ini file with desired parameters; including mutation rate, population size,
generation limit(max number of generations) and the mutation and crossover operators. 

Run the file Pytheif2/src/main/__init__.py
The results will be written in the same place as before.

Please run the jupyter notebook at:
 TravellingTheifProblem/TravellingThief/submissions/!EVALUATION/evaluation.ipynb 
This will read in the results and show:
	The pareto fronts of all combinations of genetic operators (both mutation and crossover)

	The results of the specialized NGTA approach with all competition problems, with analysis in cell below.

	A table showing the hypervolume of the combinations of genetic operators with analysis.

Please note that when generating new results they are placed in the dir TravellingThief/results/ 
while the jupyter notebook reads from TravellingThief\submissions\Epsilon to match the original
competition implementation.