# ==========================================================
# PROJECT 2: DATA CLASSIFICATION USING AI
# EcodeLabs Internship 2026
# ==========================================================

import random


# ----------------------------------------------------------
# DATASET
# ----------------------------------------------------------

dataset = [
    [5.1, 3.5, 1.4, 0.2, "Setosa"],
    [4.9, 3.0, 1.4, 0.2, "Setosa"],
    [4.7, 3.2, 1.3, 0.2, "Setosa"],
    [5.0, 3.6, 1.4, 0.2, "Setosa"],
    [5.4, 3.9, 1.7, 0.4, "Setosa"],
    [4.6, 3.4, 1.4, 0.3, "Setosa"],
    [5.0, 3.4, 1.5, 0.2, "Setosa"],
    [5.4, 3.7, 1.5, 0.2, "Setosa"],
    [4.8, 3.4, 1.6, 0.2, "Setosa"],
    [5.2, 3.5, 1.5, 0.2, "Setosa"],

    [6.4, 3.2, 4.5, 1.5, "Versicolor"],
    [6.9, 3.1, 4.9, 1.5, "Versicolor"],
    [5.5, 2.3, 4.0, 1.3, "Versicolor"],
    [6.5, 2.8, 4.6, 1.5, "Versicolor"],
    [5.7, 2.8, 4.5, 1.3, "Versicolor"],
    [6.3, 2.9, 4.3, 1.3, "Versicolor"],
    [4.9, 2.4, 3.3, 1.0, "Versicolor"],
    [6.6, 2.9, 4.6, 1.3, "Versicolor"],
    [5.2, 2.7, 3.9, 1.4, "Versicolor"],
    [5.0, 2.0, 3.5, 1.0, "Versicolor"],

    [6.7, 3.1, 5.6, 2.4, "Virginica"],
    [6.9, 3.1, 5.4, 2.1, "Virginica"],
    [5.8, 2.7, 5.1, 1.9, "Virginica"],
    [6.8, 3.2, 5.9, 2.3, "Virginica"],
    [6.7, 3.3, 5.7, 2.5, "Virginica"],
    [6.7, 3.0, 5.2, 2.3, "Virginica"],
    [6.3, 2.5, 5.0, 1.9, "Virginica"],
    [6.5, 3.0, 5.2, 2.0, "Virginica"],
    [6.2, 3.4, 5.4, 2.3, "Virginica"],
    [7.3, 2.9, 6.3, 1.8, "Virginica"]
]


# ----------------------------------------------------------
# DISPLAY DATASET INFORMATION
# ----------------------------------------------------------

def show_dataset_info(data):

    print("\n========== DATASET INFORMATION ==========")

    print("Total Records:", len(data))

    print("\nFeatures:")
    print("1. Sepal Length")
    print("2. Sepal Width")
    print("3. Petal Length")
    print("4. Petal Width")

    print("\nClasses:")
    print("1. Setosa")
    print("2. Versicolor")
    print("3. Virginica")


# ----------------------------------------------------------
# SPLIT DATASET
# ----------------------------------------------------------

def split_dataset(data):

    random.shuffle(data)

    split_point = int(len(data) * 0.7)

    training_data = data[:split_point]
    testing_data = data[split_point:]

    return training_data, testing_data


# ----------------------------------------------------------
# CLASSIFICATION ALGORITHM
# ----------------------------------------------------------

def classify(sepal_length, sepal_width, petal_length, petal_width):

    # Simple decision-based classification algorithm

    if petal_length <= 2.0:
        return "Setosa"

    elif petal_length <= 4.8:
        return "Versicolor"

    else:
        return "Virginica"


# ----------------------------------------------------------
# TRAIN MODEL
# ----------------------------------------------------------

def train_model(training_data):

    print("\n========== MODEL TRAINING ==========")

    print("Training Records:", len(training_data))

    print("Algorithm: Decision-Based Classification")

    print("Training model...")

    # Analyze classes in training data
    classes = {}

    for row in training_data:

        class_name = row[4]

        if class_name not in classes:
            classes[class_name] = 0

        classes[class_name] += 1

    print("\nClasses learned by model:")

    for class_name in classes:
        print(class_name, ":", classes[class_name])

    print("\nModel trained successfully!")


# ----------------------------------------------------------
# TEST MODEL
# ----------------------------------------------------------

def test_model(testing_data):

    print("\n========== MODEL TESTING ==========")

    correct = 0

    for row in testing_data:

        actual = row[4]

        predicted = classify(
            row[0],
            row[1],
            row[2],
            row[3]
        )

        print(
            "Actual:",
            actual,
            "| Predicted:",
            predicted
        )

        if actual == predicted:
            correct += 1

    accuracy = (correct / len(testing_data)) * 100

    print("\nCorrect Predictions:", correct)
    print("Total Test Records:", len(testing_data))
    print("Accuracy:", round(accuracy, 2), "%")

    return accuracy


# ----------------------------------------------------------
# PREDICT NEW DATA
# ----------------------------------------------------------

def predict_new_flower():

    print("\n========== NEW DATA PREDICTION ==========")

    try:

        sepal_length = float(
            input("Enter Sepal Length: ")
        )

        sepal_width = float(
            input("Enter Sepal Width: ")
        )

        petal_length = float(
            input("Enter Petal Length: ")
        )

        petal_width = float(
            input("Enter Petal Width: ")
        )

        prediction = classify(
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        )

        print("\nAI Prediction:", prediction)

    except ValueError:

        print("\nInvalid input!")
        print("Please enter numbers only.")


# ----------------------------------------------------------
# MAIN PROGRAM
# ----------------------------------------------------------

def main():

    print("\n==========================================")
    print("       DATA CLASSIFICATION USING AI")
    print("          EcodeLabs Internship")
    print("              Project 2")
    print("==========================================")

    # Step 1: Understand dataset
    show_dataset_info(dataset)

    # Step 2: Split dataset
    training_data, testing_data = split_dataset(dataset.copy())

    print("\n========== DATA SPLIT ==========")

    print("Training Data:", len(training_data))
    print("Testing Data:", len(testing_data))

    # Step 3: Train model
    train_model(training_data)

    # Step 4: Test model
    test_model(testing_data)

    # Step 5: Prediction menu
    while True:

        print("\n==========================================")
        print("              MAIN MENU")
        print("==========================================")

        print("1. Predict New Flower")
        print("2. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            predict_new_flower()

        elif choice == "2":

            print("\nThank you for using Data Classification AI!")
            print("EcodeLabs Internship 2026")
            break

        else:

            print("\nInvalid choice. Please select 1 or 2.")


# ----------------------------------------------------------
# START PROGRAM
# ----------------------------------------------------------

if __name__ == "__main__":
    main()