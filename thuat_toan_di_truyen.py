import random
import train_test_model
import math

def sigmoid(x):
    return 1 / (1 + math.e ** (-x))

# Khởi tạo quần thể ban đầu
def init_population(pop_size, num_weights):
    population = []
    for i in range(pop_size):
        weights = [random.uniform(-1, 1) for _ in range(num_weights)]
        population.append(weights)
    return population

# Đánh giá sự phù hợp của các cá thể
def evaluate_fitness(population, X, y):
    fitness_scores = []
    for weights in population:
        # Tính toán độ chính xác của mạng neural network với các trọng số này
        accuracy = neural_network(X, y, weights)
        fitness_scores.append(accuracy)
    return fitness_scores

# Chọn lọc các cá thể tốt nhất
def select_parents(population, fitness_scores, num_parents):
    parents = []
    for _ in range(num_parents):
        max_index = fitness_scores.index(max(fitness_scores))
        parents.append(population[max_index])
        fitness_scores[max_index] = -1
    return parents

# Lai ghép các cá thể để tạo ra các cá thể mới
def crossover(parents, num_offspring):
    offspring = []
    for i in range(num_offspring):
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        child = [(parent1[j] + parent2[j])/2 for j in range(len(parent1))]
        offspring.append(child)
    return offspring

# Đột biến các cá thể để tạo ra các cá thể mới
def mutation(offspring, mutation_rate):
    for i in range(len(offspring)):
        for j in range(len(offspring[i])):
            if random.random() < mutation_rate:
                offspring[i][j] += random.uniform(-0.5, 0.5)
    return offspring

# Áp dụng thuật toán di truyền để tìm kiếm các trọng số tối ưu
def genetic_algorithm(X, y, pop_size, num_weights, num_generations, num_parents, num_offspring, mutation_rate):
    population = init_population(pop_size, num_weights)
    for i in range(num_generations):
        fitness_scores = evaluate_fitness(population, X, y)
        parents = select_parents(population,fitness_scores, num_parents)
        offspring = crossover(parents, num_offspring)
        offspring = mutation(offspring, mutation_rate)
        population = parents + offspring
    best_weights = max(population, key=lambda x: neural_network(X, y, x))
    return best_weights

def split_weight_layer2(weight):
    weights = []
    for i in range(0, 60, 5):
        weights.append(weight[i:i+5])
    return weights
# Hàm tính toán độ chính xác của mạng neural network với các trọng số cho trước
def neural_network(X, y, weights):
    # Xây dựng mạng neural network và tính toán độ chính xác
    # print(weights)
    rate_true = 0
    weights_layer1 = weights[:5]
    # print(weights_layer1)
    # print(weights[5:])
    weights_layer2 = split_weight_layer2(weights[5:])
    # print(weights_layer2)
    for i in range(100):
        number = X[i][0] / 100
        # print(number)
        value1 = []
        value2 = []
        for j in range(5):
            # print(weights_layer1[i])
            value1.append(sigmoid(number * weights_layer1[j]))
        # print(value1)
        for j in range(12):
            value = 0
            for k in range(5):
                value += value1[k] * weights_layer2[j][k]
            value2.append(sigmoid(value))
        max_index = value2.index(max(value2))
        if train_test_model.dict[max_index + 1] == X[i][1]:
            rate_true += 1
        # print("---------------------")
    return (rate_true / 80000)

# Sử dụng thuật toán di truyền để tìm kiếm các trọng số tối ưu cho mạng neural network
# best_weights = genetic_algorithm(train_test_model.train_data, 
#                                  train_test_model.test_data, 
#                                  pop_size=100, 
#                                  num_weights=65, 
#                                  num_generations=50, 
#                                  num_parents=20, 
#                                  num_offspring=80, 
#                                  mutation_rate=0.1)
# print(best_weights)
def prediction(number, weights):
    # Xây dựng mạng neural network và tính toán độ chính xác
    # print(weights)
    # rate_true = 0
    weights_layer1 = weights[:5]
    # print(weights_layer1)
    # print(weights[5:])
    weights_layer2 = split_weight_layer2(weights[5:])
    # print(weights_layer2)
    # for i in range(100):
    number /= 100
    # print(number)
    value1 = []
    value2 = []
    for j in range(5):
        # print(weights_layer1[i])
        value1.append(sigmoid(number * weights_layer1[j]))
    # print(value1)
    for j in range(12):
        value = 0
        for k in range(5):
            value += value1[k] * weights_layer2[j][k]
        value2.append(sigmoid(value))
    max_index = value2.index(max(value2))
    # print("---------------------")
    return train_test_model.dict[max_index + 1]

weights = [-0.777191255932709, -0.5889769734925288, -0.7549979487950976, 0.4260876096032806, 0.059173226093856834, 0.1528315980111236, -0.41867897758387673, -0.5914934215320725, 0.714766338346138, -0.039652779674148805, 0.4253233124204908, 0.7487679827137081, -0.047975784568535934, -0.27813570293204465, 0.3193498119032441, -0.9770555563880643, 0.22637436765726748, -0.3696706551066849, 0.09348200108548281, -0.1027765262295234, 0.4660265009853625, 0.2326432673359576, -0.6988881746580812, 0.41736046205007493, -0.10685396539803337, -0.16047386392069912, 0.004677259340287121, 0.734113888242977, -0.037687306537841206, 0.4872301025196101, 0.8592778516006916, -0.3941748739312925, 0.002726662402053104, -0.09159793299377146, 0.2983968227121254, 0.05192940280282464, 0.8497721425454491, 0.7148095061461839, -0.3168029907824039, -0.4753374173027872, 0.30838854488918327, 0.41173899723672935, 0.13923538650973052, 0.45107105876515546, -0.15213054345129653, -0.33640452291101897, -0.8681352927296674, -0.3879891299792843, -0.3861170300414562, -0.10132926908996981, -0.11502849006565477, 0.13283914624580836, 0.6827241075061075, -0.21344630115807237, -0.8505598415751795, 0.1727736943094861, 0.4729000415464538, -0.2902085254174135, 0.9402136902413365, -0.16959282892098887, -0.4770726157875295, 0.23658936632212368, -0.1742913450783592, 0.22797605605093635, -0.7529780268021182]
for i in range(1, 13):
    print(prediction(i, weights))