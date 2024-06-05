import csv
import re
import numpy as np

from sklearn.linear_model import LinearRegression # Import directly

def clean_text(text):
  """Cleans text by removing non-alphanumeric characters and converting to lowercase."""
  return re.sub(r'\W+', ' ', text).lower()

def extract_features(profile):
  """Extracts features (number of skills, experience, projects) from a profile dictionary."""
  skills = profile.get('skills', '')
  experience = profile.get('experience', '')
  projects = profile.get('projects', '')

  num_skills = len(skills.split(','))
  num_experience = len(experience.split(','))
  num_projects = len(projects.split(','))

  return num_skills, num_experience, num_projects

def match_keywords(candidate_keywords, job_keywords):
  """Calculates the percentage of matching keywords between candidate and job descriptions."""
  candidate_keywords_set = set(clean_text(candidate_keywords).split(','))
  job_keywords_set = set(clean_text(job_keywords).split(','))
  matches = candidate_keywords_set.intersection(job_keywords_set)
  return len(matches) / len(job_keywords_set) if job_keywords_set else 0

def calculate_score(model, candidate, job):
  """Calculates a score based on feature vectors and keyword matches."""
  candidate_features = extract_features(candidate)
  job_features = extract_features(job)

  skills_match = match_keywords(candidate['skills'], job['skills'])
  experience_match = match_keywords(candidate['experience'], job['experience'])
  projects_match = match_keywords(candidate['projects'], job['projects'])

  feature_vector = [
    skills_match, experience_match, projects_match,
    candidate_features[0], candidate_features[1], candidate_features[2]
  ]

  feature_vector = np.array(feature_vector).reshape(1, -1)
  score = model.predict(feature_vector)[0]
  return score

def get_input(prompt):
  """Gets user input for candidate and job descriptions."""
  return input(prompt)

def train_model(training_data_file):
  """Trains a linear regression model using the provided CSV file."""
  X_train = []
  Y_train = []
  with open(training_data_file, mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
      X_train.append([float(val) for val in row[:-1]])
      Y_train.append(float(row[-1]))

  # Create a linear regression model
  model = LinearRegression()
  model.fit(X_train, Y_train)  # Train the model
  return model

if __name__ == "__main__":
  # Train the model
  model = train_model('training_data.csv')

  # Get user input
  candidate = {
    'skills': get_input("Enter candidate's skills (comma-separated): "),
    'experience': get_input("Enter candidate's job titles/experience (comma-separated): "),
    'projects': get_input("Enter candidate's projects (comma-separated): ")
  }

  job = {
    'skills': get_input("Enter job required skills (comma-separated): "),
    'experience': get_input("Enter job required experience (comma-separated): "),
    'projects': get_input("Enter job required projects (comma-separated): ")
  }

  # Calculate score
  score = calculate_score(model, candidate, job)
  print(f'Candidate Score: {score:.2f}')
