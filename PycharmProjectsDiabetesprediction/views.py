import pickle
from django.shortcuts import render
from django.http import HttpResponse
import numpy as np

def predict(request):
    if request.method == 'POST':
        # Assuming you have a form with input fields named 'feature1', 'feature2', etc.
        feature1 = float(request.POST.get('feature1'))
        feature2 = float(request.POST.get('feature2'))
        feature3 = float(request.POST.get('feature3'))
        feature4 = float(request.POST.get('feature4'))
        feature5 = float(request.POST.get('feature5'))
        feature6 = float(request.POST.get('feature6'))
        feature7 = float(request.POST.get('feature7'))
        feature8 = float(request.POST.get('feature8'))
        # Assuming X_test is a numpy array containing the input features
        X_test = np.array([[feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8]])

        # Load the trained model
        with open(r'C:\Users\BKand\PycharmProjectsDiabetesprediction\PycharmProjectsDiabetesprediction\static\Diabetesprediction\Images\Diabetesprediction.sav','rb') as file:
            # Your code here
            loaded_model = pickle.load(file)

        # Make predictions
        prediction = loaded_model.predict(X_test)
        context = {'prediction': prediction[0]}  # Assuming prediction is a single value
        return render(request, 'predict.html', context)

    return render(request, 'predict.html')
