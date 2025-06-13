import tkinter as tk
from tkinter import messagebox


# Create the main window
root = tk.Tk()
root.title("Loan Default Prediction")

# Function to make predictions
def make_prediction():
    # Get the values from the entry widgets
    loan = float(entry_loan.get())

    # Make the prediction
  #  prediction = model.predict([[loan]])

    # Show the prediction in a message box
    messagebox.showinfo("Prediction", f"The predicted loan default is: {loan}")


# Create and place labels and entry widgets for each feature with default values
tk.Label(root, text="Loan Amount").grid(row=0, column=0, padx=10, pady=5)
entry_loan = tk.Entry(root)
entry_loan.insert(0, "10000")  # Default value
entry_loan.grid(row=0, column=1, padx=10, pady=5)


# Create a button to make the prediction
predict_button = tk.Button(root, text="Predict", command=make_prediction)
predict_button.grid(row=12, column=0, columnspan=2, pady=10)


root.mainloop()