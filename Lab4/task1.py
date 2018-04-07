from Lab4.concept import generate_concepts
from Lab4.bayesian import likelihood


if __name__ == "__main__":
    concepts = generate_concepts(1, 100)
    data = [3, 6, 9]

    results = [(concept.name, likelihood(data, concept)) for concept in concepts if concept.satisfy_concept(data)]

    for result in sorted(results, key=lambda x: x[1], reverse=True):
        print(result)