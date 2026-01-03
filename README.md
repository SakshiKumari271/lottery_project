🎰 Lottery & Probability Simulator (Python)

“Winning the lottery is luck. Understanding probability is skill.” 🎯

A Python-based Lottery & Probability Simulator that uses repeated random trials to demonstrate how extremely rare winning lottery combinations really are.
This project applies Monte Carlo simulation techniques to visualize probability through data rather than assumptions.

📌 Project Overview

This simulator mimics a real-world lottery system where:

A ticket consists of 6 unique numbers between 1 and 49

Random draws are repeated thousands to millions of times

The system analyzes how often different match counts occur

The goal is to build a practical intuition for probability, randomness, and statistical distribution using Python.

🚀 Key Features

🎲 Realistic lottery simulation (6 numbers from 1–49)

🔁 Large-scale Monte Carlo simulations

📊 Match frequency tracking (0–6 matches)

🧮 Empirical probability calculation

🧹 Clean, readable, beginner-friendly Python code

📉 Clearly demonstrates why lotteries are statistically unfavorable

🧠 Concepts Demonstrated

Probability & Randomness

Monte Carlo Simulation

Statistical Distribution

Iterative Computation

Conditional Logic

Dictionary-based data aggregation

🛠 Tech Stack

Python 🐍

random module

Git & GitHub

(Optional: Matplotlib for visualization)

⚙️ How It Works (Algorithm Flow)

Generate a lottery ticket with 6 unique numbers

Randomly draw 6 numbers per simulation

Compare ticket and draw using set intersection

Count the number of matches (0–6)

Store results in a dictionary

Repeat for large iterations

Calculate probability distribution from results

▶️ How to Run
python lottery_simulator.py


(Ensure Python 3.10+ is installed)

📂 Project Structure
├── lottery_simulator.py
├── README.md
└── requirements.txt (optional)

📊 Sample Output
Matches: 0 → 79.23%
Matches: 1 → 18.12%
Matches: 2 → 2.45%
Matches: 3 → 0.18%
Matches: 4 → 0.02%
Matches: 5 → 0.0003%
Matches: 6 → ~0%


(Results vary based on number of simulations)

🎓 Who Should Use This Project?

Python Beginners

Data Science Aspirants

Probability & Statistics Learners

Students preparing for technical interviews

Anyone curious about “Why lottery never works” 😄

🌱 Future Improvements

Add data visualization (Matplotlib / Seaborn)

CLI arguments for simulation control

Export results to CSV

Compare theoretical vs experimental probability

Build a web interface (Flask / Streamlit)

🧑‍💻 Author

Sakshi Kumari
Computer Science Student | Python | Probability 

⭐ Why This Project Matters

This project demonstrates how code can debunk real-world myths using data.
It showcases analytical thinking, Python fundamentals, and simulation-based problem solving—making it a strong foundational project.
