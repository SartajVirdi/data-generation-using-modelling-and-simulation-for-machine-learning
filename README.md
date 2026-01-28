# Predicting Queue Waiting Times: A Simulation-Driven ML Study

**By Sartaj Singh Virdi**  
**Roll Number: 102303259**

---

## Brief Intro

I developed a synthetic data generation pipeline using discrete-event queue simulation to train and evaluate five machine learning models. The objective? Determine which algorithm most accurately predicts waiting times in service queue systems. **The winner: Random Forest.**

---

## Main Goal
```
Simulate Queue Scenarios → Generate Training Data → Train 5 ML Models → Compare Performance
```

**Why simulation?** Real-world queue data is scarce and difficult to obtain. Simulation enables us to generate extensive training datasets while systematically exploring how different operational parameters influence system performance.

---

## Simulation Architecture

I built a discrete-event queueing system using **SimPy** with the following characteristics:

- **Customer arrivals:** Stochastic (random) arrival patterns
- **Queue discipline:** First-Come-First-Served (FCFS)
- **Service mechanism:** Multiple parallel servers with variable capacity
- **Performance metric:** Average waiting time per simulation run

The experimental design randomizes key parameters across **1,000 simulation scenarios**:

| **Parameter**           | **Range**              | **Description**                    |
|-------------------------|------------------------|------------------------------------|
| Arrival Rate            | 1–10 customers/unit    | Customer arrival frequency         |
| Service Time            | 1–8 time units         | Time required per customer         |
| Server Count            | 1–5 servers            | Available service capacity         |

**Output:** 1,000 unique parameter combinations = 1,000 labeled training instances

---

## Machine Learning Models Evaluated

I trained and compared five regression algorithms on the simulated dataset:

1. **Linear Regression** — Baseline linear model
2. **Decision Tree Regressor** — Single decision tree with recursive partitioning
3. **Random Forest Regressor** — Ensemble of decision trees with bagging
4. **K-Nearest Neighbors (KNN)** — Instance-based learning approach
5. **Support Vector Regression (SVR)** — Kernel-based non-linear regression

---

## Evaluation Metrics

Models were assessed using:

- **R² Score (Coefficient of Determination):** Proportion of variance explained (closer to 1 = better)
- **RMSE (Root Mean Squared Error):** Average prediction error magnitude (lower = better)

---

## Results & Performance Analysis

### R² Scores: Which Model Explained The Most Variance?

| **Model**              | **R² Score** |
|------------------------|--------------|
| Random Forest          | **0.76**     |
| KNN                    | 0.72         |
| SVR                    | 0.72         |
| Decision Tree          | 0.64         |
| Linear Regression      | 0.57         |

**Random Forest** achieved the highest R² score at **0.76**, indicating it captured **76% of the variance** in waiting times.

**Why did Linear Regression underperform?** Queue dynamics involve **non-linear interactions** between arrival rates, service times, and server counts—relationships that linear models struggle to capture.

<img width="800" height="500" alt="image" src="https://github.com/user-attachments/assets/9cc461d2-f459-4fee-908d-850b2b3d8169" />


---

### RMSE: Which Model Made The Smallest Errors?

| **Model**              | **RMSE**  |
|------------------------|-----------|
| Random Forest          | **4.7**   |
| KNN                    | 5.2       |
| SVR                    | 5.2       |
| Decision Tree          | 5.9       |
| Linear Regression      | 6.4       |

Random Forest maintained the **lowest average prediction error** at 4.7 time units—a meaningful improvement over the 6.4 error rate of Linear Regression.

<img width="800" height="500" alt="image" src="https://github.com/user-attachments/assets/53c96b67-a5e0-4533-a2c6-cf1b5dc1b28a" />


---

## Why Random Forest Won

Random Forest dominated due to its ability to:

1. **Handle non-linear relationships** without manual feature engineering
2. **Capture complex interactions** between multiple input parameters
3. **Reduce overfitting** through ensemble averaging
4. **Provide robust predictions** across diverse queue configurations

For systems with **multiple interacting factors**, ensemble methods consistently outperform simpler approaches.

---

## Reproduction Guide

### Installation
```bash
# Install dependencies
pip install -r requirements.txt
```

### Execution
```bash
# Run complete pipeline
python main.py
```

This script:
1. Generates 1,000 simulated queue scenarios
2. Trains all five models
3. Computes evaluation metrics
4. Saves comparison visualizations

---

## Project Structure
```
project-directory/
│
├── data/
│   └── simulation_data.csv          # 1000 simulated records
│
├── graphs/
│   ├── r2_comparison.png            # R² visualization
│   └── rmse_comparison.png          # RMSE visualization
│
├── results/
│   └── model_comparison.csv         # Detailed performance metrics
│
└── main.py                          # Main execution script
```

---

## Technology Stack

- **Python** — Core programming language
- **SimPy** — Discrete-event simulation framework
- **Pandas & NumPy** — Data manipulation and numerical computation
- **Scikit-learn** — Machine learning algorithms
- **Matplotlib** — Data visualization

---

## Key Takeaways

Not all machine learning algorithms perform equally across problem domains. For **complex systems with non-linear parameter interactions**, Random Forest and other ensemble methods significantly outperform linear approaches.

**Practical implication:** When modeling real-world operational systems, prioritize algorithms that can capture interaction effects and non-linear relationships.

---

## Future Enhancements

Potential extensions to this research:

- [ ] Implement **cross-validation** for more robust performance estimates
- [ ] Conduct **hyperparameter tuning** (GridSearchCV/RandomizedSearchCV)
- [ ] Explore more complex queue topologies (priority queues, tandem systems)
- [ ] Test different arrival distributions (Poisson, uniform, exponential)
- [ ] Add additional target variables (total system time, queue length)
- [ ] Develop an **interactive prediction interface** for live queue forecasting

---

**Project Completed:** January 2025  
**Research Focus:** Exploring the synergy between simulation modeling and machine learning for operational system prediction

---
