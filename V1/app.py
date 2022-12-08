import tensorflow as tf
import numpy as np

def create_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=[2]),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1)
    ])

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.MeanSquaredError(),
                  metrics=['mae'])

    return model

num_grades = int(input("How many grades do you want to enter? "))

grades_and_weights = []

for i in range(num_grades):
    grade = float(input("Enter grade for class {}: ".format(i+1)))
    has_weight = input("Does this class have a weight (y/n)? ")

    if has_weight.lower() == 'y':
        weight = float(input("Enter weight for class {}: ".format(i+1)))
        grades_and_weights.append([grade, weight])
    else:
        grades_and_weights.append([grade, 1])

grades_and_weights = np.array(grades_and_weights, dtype=np.float32)

model = create_model()

model.fit(grades_and_weights[:, 0], grades_and_weights[:, 1], epochs=500)

final_grade = float(input("Enter the final grade you want to achieve: "))

predicted_weight = model.predict(final_grade)

current_grade_points = np.sum(grades_and_weights[:, 0] * grades_and_weights[:, 1])
current_credits = np.sum(grades_and_weights[:, 1])

needed_grade_points = final_grade * predicted_weight
needed_credits = predicted_weight - current_credits

needed_average = (current_grade_points + needed_grade_points) / (current_credits + needed_credits)

print("To achieve a final grade of {} with a weight of {},".format(final_grade, predicted_weight))
print("you need an average of {:.2f} in your remaining assignments.".format(needed_average))
