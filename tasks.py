def read_population_data(file_path):
    population_data = {}
    with open(file_path, 'r') as file:
        for line in file:
            country, year, population = line.strip().split(', ')
            year = int(year)
            population = int(population)
            if country not in population_data:
                population_data[country] = [(year, population)]
            else:
                population_data[country].append((year, population))
    return population_data

def main():
    file_path = 'population_data'
    population_data = read_population_data(file_path)
if __name__ == "__main__":
    main()