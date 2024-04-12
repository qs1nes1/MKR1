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

def calculate_population_change(population_data):
    population_change = {}
    for country, data in population_data.items():
        population_change[country] = []
        prev_population = None
        for year, population in data:
            if prev_population is not None:
                change = population - prev_population
                population_change[country].append((year, change))
            prev_population = population
    return population_change

def main():
    file_path = 'population_data'
    population_data = read_population_data(file_path)
    population_change = calculate_population_change(population_data)


    for country, changes in population_change.items():
        print(f'Зміна населення для {country}:')
        for year, change in changes:
            print(f'\tРік {year}: {change}')


if __name__ == "__main__":
    main()