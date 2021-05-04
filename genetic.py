import random
import numpy as np
import matplotlib.pyplot as plt
import math


class Gnome:

    def __init__(self, genes):
        self.genes = genes

    def get_length(self):
        return len(self.genes)

    def get_genes(self):
        return self.genes


class GnomeFactory:
    """
        This class acts as factory and generates a new genome object.
        Here, genome is a sequence of 0s and 1s which are chose by
        random.
    """

    def __init__(self):
        pass

    @staticmethod
    def create_gene():
        return random.choice([0, 1])

    @staticmethod
    def create_gnome(length, genes=[]):
        if not genes:
            genes = [GnomeFactory.create_gene() for i in range(0, length)]
        return Gnome(genes)


class Individual:
    """
        The Individual class represents a single instance of the population.
    """

    def __init__(self, gnome):
        self.gnome = gnome
        self.length = gnome.get_length()
        self.fitness = self.get_fitness()

    def mate(self, partner):
        genes1 = self.gnome.get_genes()
        genes2 = partner.gnome.get_genes()
        child_genes = []

        for g1, g2 in zip(genes1, genes2):

            prob = random.random()

            if prob < 0.47:
                child_genes.append(g1)

            elif prob < 0.94:
                child_genes.append(g2)

            else:
                child_genes.append(GnomeFactory.create_gene())

        child_gnome = GnomeFactory.create_gnome(len(child_genes), child_genes)
        return Individual(child_gnome)

    def get_fitness(self):
        genes = self.gnome.get_genes()
        fitness = 0
        for (i, j) in enumerate(genes):
            fitness += (j * (2 ** i))

        return fitness


class GeneticAlgorithm:

    def __init__(self, population_size, length):
        self.population_size = population_size
        self.length = length
        self.population = []
        self.generations = 1  # Initializing number of generations
        self.best_fitness = 255

    @staticmethod
    def choose_by_russian_roulette(sorted_population, total):

        draw = random.uniform(0, 1)
        accu = 0

        for i in sorted_population:
            prob = i.fitness / total
            accu += prob
            if draw <= accu:
                return i

    def run(self):

        # generating initial population
        for i in range(self.population_size):
            child_gnome = GnomeFactory.create_gnome(self.length)
            self.population.append(Individual(child_gnome))

        while True:

            # sort the population with respect to the most fitness score
            self.population = sorted(self.population, key=lambda ind: ind.fitness, reverse=True)

            if self.population[0].fitness == self.best_fitness:
                return self.population[0]

            fitness_sum = 0
            new_generation = []

            for i in self.population:
                fitness_sum += i.fitness

            for i in range(self.population_size):
                parent1 = self.choose_by_russian_roulette(sorted_population=self.population, total=fitness_sum)
                parent2 = self.choose_by_russian_roulette(sorted_population=self.population, total=fitness_sum)

                child = parent1.mate(parent2)
                new_generation.append(child)

            self.population = new_generation
            self.generations += 1


if __name__ == "__main__":

    n = 7
    offset = 4
    data_x = np.empty(n, dtype=int)
    data_y = np.empty(n)

    for i in range(n):

        population_size = i + offset
        data_x[i] = population_size
        iterations = 100
        g = np.empty(iterations, dtype=int)
        gen = 0

        for j in range(iterations):

            length = 8
            genetic = GeneticAlgorithm(population_size, length)
            best = genetic.run()
            g[j] = genetic.generations
            gen = np.average(g)

        data_y[i] = gen

    print(data_x)
    print(data_y)

    plt.plot(data_x, data_y)
    plt.xlabel("Population")
    plt.ylabel("Average Generations")
    plt.show()