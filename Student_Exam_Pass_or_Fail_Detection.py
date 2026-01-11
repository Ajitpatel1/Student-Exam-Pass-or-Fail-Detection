import numpy as np 
X = Study_Hours = np.array([1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15])
Y = Study_result = np.array([0 , 0 , 0 , 0 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ])

m = len(X)

b0 = 0
b1 = 0
alpha = 0.1 
epochs = 1000

def sigmoid(z):
    return 1/(1 + np.exp(-z))

for i in range(epochs):
    z = b0 + b1 * X
    y_hat = sigmoid(z)
    
    db0 = (1/m) * np.sum(y_hat - Y) 
    db1 = (1/m) * np.sum((y_hat - Y) * X)
    
    b0 = b0 - alpha * db0
    b1 = b1 - alpha * db1

while True:   
    
    user_input_Study_hours = float(input("Enter your Study Time : "))
        
    z = b0 + b1 * user_input_Study_hours
    probability = sigmoid(z)

    probability_percentage = round(probability * 100)    

    print(f"\n your Probability of passing : {round(probability_percentage , 2)} %")
        
    if probability >= 0.5 :
        print(f"your Study time {user_input_Study_hours} is perfect for well result ")
        print("Result : PASS ✅")
    else:
        print(f"plese improve your study time more than {user_input_Study_hours}")          
        print("Result : FAIL ❌")

    user_program_Exit = input("You need to Program Exit (Yes/No) : ").lower()
    if user_program_Exit == "yes":
        print("GoodBye......")
        break
    else:
        user_program_Exit == "No"
        continue
       