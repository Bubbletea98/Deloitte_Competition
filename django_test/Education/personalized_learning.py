import math

def calculateProbability(theta, difficulty):
    return 1 / (1 + math.exp(-1.7*(theta - difficulty)))

def calculateLikelihood(theta, problems):
    likelihood = 0
    for problem in problems:
        probability = calculateProbability(theta, problem.difficulty)
        u = 1 if problem.isCorrect else 0
        likelihood += pow(probability, u) * pow(1-probability, 1-u)
    return likelihood

# find the most likely ability for the student's ability
def calculateAbility(learning, problems):
    max_difficulty = 1
    for problem in problems:
        if(problem.isCorrect and problem.difficulty > max_difficulty):
            max_difficulty = problem.difficulty
    suitableTheta = max_difficulty
    maximum = 0
    # Calculate the likelihood for each theta 
    for theta in reversed(range(1, max_difficulty + 1)):
        likelihood = calculateLikelihood(theta, problems)
        print(likelihood)
        print(theta)
        if(likelihood > maximum):
            maximum = likelihood
            suitableTheta = theta
    return (suitableTheta, maximum)

def updateAbility(learning, newProblems, oldProblems):
    return calculateAbility(learning, newProblems + oldProblems)