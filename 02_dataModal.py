import csv

# Synthetic training data
training_data = [
    # Skills match, Experience match, Projects match, Num skills, Num experience, Num projects, Score
    (0.75, 0.5, 0.6, 4, 3, 2, 75),
    (0.5, 0.4, 0.5, 3, 4, 3, 60),
    (0.9, 0.7, 0.8, 5, 5, 4, 90),
    (0.3, 0.2, 0.3, 2, 2, 1, 30),
    (0.85, 0.6, 0.7, 5, 4, 3, 80),
    (0.7, 0.5, 0.6, 4, 3, 3, 70),
    (0.6, 0.4, 0.5, 3, 3, 2, 65),
    (0.4, 0.3, 0.4, 2, 2, 1, 40),
    (0.95, 0.8, 0.9, 6, 5, 5, 95),
    (0.2, 0.1, 0.2, 1, 1, 1, 20)
]

# Write to CSV
with open('training_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Skills Match', 'Experience Match', 'Projects Match', 'Num Skills', 'Num Experience', 'Num Projects', 'Score'])
    writer.writerows(training_data)

print("Training data written to 'training_data.csv'")
