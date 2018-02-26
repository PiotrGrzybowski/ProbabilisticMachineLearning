import numpy as np
import matplotlib.pyplot as plt


def calculate_medical_test(p_of_disease, p_of_positive_test_given_no_disease, p_of_negative_test_given_disease):
    p_a = p_of_disease
    p_not_a = 1 - p_a

    p_b_given_not_a = p_of_positive_test_given_no_disease
    p_not_b_given_a = p_of_negative_test_given_disease

    p_b_given_a = 1 - p_not_b_given_a
    p_not_b_given_not_a = 1 - p_b_given_not_a

    p_b = p_b_given_a * p_a + p_b_given_not_a * p_not_a
    p_not_b = p_not_b_given_a * p_a + p_not_b_given_not_a * p_not_a

    p_a_given_b = p_b_given_a * p_a / p_b
    p_a_given_not_b = p_not_b_given_a * p_a / p_not_b
    p_not_a_given_b = p_b_given_not_a * p_not_a / p_b
    p_not_a_given_not_b = p_not_b_given_not_a * p_not_a / p_not_b

    return p_a_given_b, p_a_given_not_b, p_not_a_given_b, p_not_a_given_not_b


population = 50000
affected_people_out_of_population = 10000

probability_of_disease = affected_people_out_of_population / population
positive_test_given_no_disease = 0.02
negative_test_given_disease = 0.01

results_description = ['Probability of disease when test positive',
                       'Probability of disease when test negative',
                       'Probability no disease when test positive',
                       'Probability no disease when test negative']

series1 = []
series2 = []
series3 = []
series4 = []

for i in range(1, affected_people_out_of_population + 1):
    result = calculate_medical_test(i / population, positive_test_given_no_disease, negative_test_given_disease)
    series1.append(result[0])
    series2.append(result[1])
    series3.append(result[2])
    series4.append(result[3])

affected = np.arange(1, affected_people_out_of_population + 1)

plt.plot(affected, series1, color='blue', label='Probability of disease when test positive.')
plt.plot(affected, series2, color='green', label='Probability of disease when test negative.')
plt.plot(affected, series3, color='red', label='Probability no disease when test positive.')
plt.plot(affected, series4, color='black', label='Probability no disease when test negative.')
plt.xlabel('People with disease on 50.000 population.')
plt.ylabel('Probability of having the disease.')
plt.legend()
plt.show()