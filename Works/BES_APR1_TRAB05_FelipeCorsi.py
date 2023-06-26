#Felipe Gabriel de Marchi Corsi
class Iris:
    sepal_lenght = -0.1
    sepal_width = -0.1
    petal_length = -0.1
    petal_width = -0.1
    species = ""
    
def read_file_iris():
    flowers = []

    file = open("iris.data.csv", 'r')
    next(file)
    for line in file:
        infos = line.strip().split(',')
        iris = Iris()
        iris.sepal_lenght = float(infos[0])
        iris.sepal_width = float(infos[1])
        iris.petal_length = float(infos[2])
        iris.petal_width = float(infos[3])
        iris.species = infos[4]
        flowers.append(iris)
    file.close()
    return flowers

def read_file_unclassified_iris():
    unclassified_iris = []

    file = open("unclassified_iris.data.csv", 'r')
    next(file)
    for line in file:
        infos = line.strip().split(',')
        iris = Iris()
        iris.sepal_lenght = float(infos[0])
        iris.sepal_width = float(infos[1])
        iris.petal_length = float(infos[2])
        iris.petal_width = float(infos[3])
        unclassified_iris.append(iris)
    file.close()
    return unclassified_iris

def euclidean_distance(sepal_length, sepal_width, petal_length, petal_width, flowers):
    distances = {"setosa": [], "versicolor": [], "virginica": []}
    for i in range(len(flowers)):
        distance = ((sepal_length - flowers[i].sepal_lenght) ** 2 + (sepal_width - flowers[i].sepal_width) ** 2 +
         (petal_length - flowers[i].petal_length) ** 2 + (petal_width - flowers[i].petal_width) ** 2) ** 0.5
        if flowers[i].species == "setosa":
            distances["setosa"].append(distance)
        elif flowers[i].species == "versicolor":
            distances["versicolor"].append(distance)
        else:
            distances["virginica"].append(distance)
    distances["setosa"].sort()
    distances["versicolor"].sort()
    distances["virginica"].sort()
    return distances

def classify_iris(K, distances):
    x = slice(K)
    setosa = distances["setosa"][x]
    versicolor = distances["versicolor"][x]
    virginica = distances["virginica"][x]

    setosa_count = 0
    versicolor_count = 0
    virginica_count = 0

    i = 0
    while i < K:
        if versicolor[versicolor_count] >= setosa[setosa_count] and virginica[virginica_count] >= setosa[setosa_count]:
            setosa_count += 1
        elif setosa[setosa_count] >= versicolor[versicolor_count] and virginica[virginica_count] >= versicolor[versicolor_count]:
            versicolor_count += 1
        else:
            virginica_count += 1
        i += 1

    if setosa_count > versicolor_count and setosa_count > virginica_count:
        print("Essa flor é Setosa!")
    elif versicolor_count > setosa_count and versicolor_count > virginica_count:
        print("Essa flor é Versicolor!")
    else:
        print("Essa flor é Virginica!")

def main():
    flowers = read_file_iris()
    unclassified_iris = read_file_unclassified_iris()
    for i in range(len(unclassified_iris)):
        print(f"Flor de Nº{i + 1}:")
        distances = euclidean_distance(unclassified_iris[i].sepal_lenght, unclassified_iris[i].sepal_width, unclassified_iris[i].petal_length, unclassified_iris[i].petal_width, flowers)
        K = len(flowers) + 1
        while K > len(flowers):
            K = int(input("Valor de K: "))
            if K > len(flowers):
                print("Valor fora de alcance, insira novamente!")
                print()
                print(f"Flor de Nº{i + 1}:")
        classify_iris(K, distances)
        print()
main()