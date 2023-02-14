import math
from flask import Flask

def average_class_grade(grades, weights=[30, 30, 40], class=None):
  
   if class.title() == "Science": #Science uses a different way of calculating grades. Point based system
      return "Science Grade"
  
   total_average_grade = ((weight[0] * grades[0] + weights[1] * grades[1] + weights[2] * grades[2]) / 100) / 100
   return total_average_grade

app = Flask()
