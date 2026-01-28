from src.data_generator import generate_data
from src.ml_models import train_models
from src.plots import plot_results

# Step 1: Generate Simulation Data
print("Generating simulation data...")
df = generate_data(1000)
print("Data generated and saved in data/simulation_data.csv")

# Step 2: Train ML Models
print("Training ML models...")
results = train_models(df)
print("Model comparison saved in results/model_comparison.csv")
print(results)

# Step 3: Generate Plots
print("Generating graphs...")
plot_results()
print("Graphs saved in graphs/ folder")
