import pandas as pd
import matplotlib.pyplot as plt

# Read data into a Pandas DataFrame
df = pd.read_csv('basicOutput.csv')
print(df)
# Plot data

df.columns = ['Occurrences', 'ExecutionTime']
plt.plot(df['Occurrences'], df['ExecutionTime'], label='Data Line')

# Customize the plot
plt.xlabel("Nombre d'occurences")
plt.ylabel('Temps exécution')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
