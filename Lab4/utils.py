from Lab4.concept import concept_label


def results_log(results):
    return '\n' + '\n'.join(["h = {0: <30} p = {1:}".format(result[0], result[1]) for result in sorted(results, key=lambda x: x[1], reverse=True)]) + '\n'


def priors_log(prior):
    return '\n' + '\n'.join(["h = {0: <30} p = {1:}".format(concept_label(concept), value) for concept, value in prior.items()]) + '\n'