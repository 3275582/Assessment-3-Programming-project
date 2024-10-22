''''
Author:
u3275582, u3216765, u3284179, 4483 Undergraduate 28, Assessment 3: Programming project, 21/ 10/2024
Programming:
// Code adapted from BostonHousPriceProject_Final.ipynb example:
// https://uclearn.canberra.edu.au/courses/16822/files/5397584?module_item_id=1346775
'''
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

class CellphonePricePredictionApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Cellphone price prediction')
        self.data = pd.read_csv('Cellphone.csv')
        self.sliders = []

        self.X = self.data.drop('Price', axis=1).values
        self.y = self.data['Price'].values

        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

        self.model = LinearRegression()
        self.model.fit(self.X_train, self.Y_train)

        self.create_widgets()

    def create_widgets(self):
      for i, column in enumerate(self.data.columns[:-1]):
            label = tk.Label(self.master, text=column + ': ')
            label.grid(row=i, column=0)
            current_val_label = tk.Label(self.master, text='0.0')
            current_val_label.grid(row=i, column=2)
            slider = ttk.Scale(self.master, from_=self.data[column].min(), to=self.data[column].max(), orient="horizontal",
                               command=lambda val, label=current_val_label: label.config(text=f'{float(val):.2f}'))
            slider.grid(row=i, column=1)
            self.sliders.append((slider, current_val_label))

      predict_button = tk.Button(self.master, text="Predict Cellphone price", command=self.predict_price)
      predict_button.grid(row=len(self.data.columns[:-1]), columnspan=3)

    def predict_price(self):
        input = [float(slider.get()) for slider, _ in self.sliders]
        price = self.model.predict([input])
        messagebox.showinfo('Predicted Price', f'The predicted cellphone price is ${price[0]:.2f}')

if __name__ == '__main__':
    root = tk.Tk()
    app = CellphonePricePredictionApp(root)
    root.mainloop()