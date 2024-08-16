import matplotlib.pyplot as plt
import koreanize_matplotlib
import pandas as pd
import csv

file_name = 'GlobalLandTemperatures.csv'

Climate = pd.read_csv(file_name, encoding = 'utf-8')




# file_name = 'GlobalLandTemperatures.csv'



Climate = pd.read_csv(file_name, encoding = 'utf-8')
print(Climate.info())