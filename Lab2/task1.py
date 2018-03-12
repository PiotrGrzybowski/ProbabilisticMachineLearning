import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def normal_distribution(mean=0, sigma=1, samples=1):
    return np.random.normal(mean, sigma, samples)


def get_cumulative_data(data, func):
    return [func(data[:i]) for i in range(1, len(data) - 1)]


def get_cumulative_mean_and_variance(data):
    return get_cumulative_data(data, np.mean), get_cumulative_data(data, np.var)


def visualize_gaussian_distributions(means, sigmas, samples):
    data = np.zeros(shape=(len(means), samples))
    for i in range(len(means)):
        data[i, :] = normal_distribution(means[i], sigmas[i], samples)

    data = np.sum(data, axis=0)

    ax_0 = sns.distplot(data)
    ax_0.set_title('Gaussian Distribution with parameters: mean = {}, sigma = {}'.format(means, sigmas))
    ax_0.set_xlabel('x')
    ax_0.set_ylabel('y')
    plt.show()

    cumulative_means, cumulative_variances = get_cumulative_mean_and_variance(data)
    f, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, sharey=True)

    ax1.set_title('Mean depends on samples.')
    ax1.set_xlabel('Number of samples')
    ax1.set_ylabel('Mean')
    ax1.axhline(y=np.sum(means), color='red')
    ax1.plot(cumulative_means)

    ax2.set_title('Variance depends on samples.')
    ax2.set_xlabel('Number of samples')
    ax2.set_ylabel('Variance')
    ax2.plot(cumulative_variances)
    ax2.axhline(y=np.sum([x ** 2 for x in sigmas]), color='red')
    plt.show()


visualize_gaussian_distributions(means=[0,2,0, 4], sigmas=[2, 0.5, 1,12], samples=5000)
# visualize_gaussian_distributions(means=[5, 10], sigmas=[1, 1], samples=5000)
# visualize_gaussian_distributions(means=[5, 10], sigmas=[1, 1], samples=5000)

