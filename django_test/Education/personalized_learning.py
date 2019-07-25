import math

def calculateProbability(theta, difficultly):
    return 1 / (1 + math.exp(-1.7*(theta - difficultly)))

def calculateLikelihood(theta, problems):
    likelihood = 0
    for problem in problems:
        probability = calculateProbability(theta, problem.difficultly)
        u = 1 if problem.isCorrect else 0
        likelihood *= pow(probability, u) * pow(probability, 1-u)
    return likelihood

# find the most likely ability for the student's ability
def calculateAbility(learning, problems):
    max_difficulty = 0
    for problem in problems:
        if(problem.isCorrect and problem.difficultly > max_difficulty):
            max_difficulty = problem.difficultly
    
    suitableTheta = max_difficulty
    maximum = 0
    # Calculate the likelihood for each theta 
    for theta in reversed(range(1, max_difficulty + 1)):
        likelihood = calculateLikelihood(theta, problems)
        
        if(likelihood > maximum):
            maximum = likelihood
            suitableTheta = theta
    return theta

def updateAbility(learning, newProblems, oldProblems):
    if(calculateLikelihood(learning.ability, newProblems) >= learning.estimation):
        return learning.ability
    else:
        return calculateAbility(learning, newProblems + oldProblems)