import xgboost as xgb
import pandas as pd
import tkinter as tk
from tkinter import messagebox

# Путь к модели
save_path = r"C:\Users\User\Desktop\dataset\xgb_model.json"

# Функция для загрузки модели
def load_model(model_path):
    model = xgb.Booster()
    model.load_model(model_path)
    return model

# Функция для прогнозирования
def predict(model, input_data):
    dmatrix = xgb.DMatrix(input_data)  # Преобразуем входные данные в формат, понятный XGBoost
    prediction = model.predict(dmatrix)
    return prediction[0]

# Функция для обработки данных и предсказания
def on_predict():
    try:
        # Считываем значения из полей ввода
        longitude = float(entry_longitude.get())
        latitude = float(entry_latitude.get())
        housing_median_age = float(entry_housing_median_age.get())
        total_rooms = float(entry_total_rooms.get())
        total_bedrooms = float(entry_total_bedrooms.get())
        population = float(entry_population.get())
        households = float(entry_households.get())
        median_income = float(entry_median_income.get())
        ocean_proximity = int(entry_ocean_proximity.get())

        # Проверяем, что ocean_proximity находится в допустимом диапазоне
        if ocean_proximity not in [0, 1, 2, 3, 4]:
            messagebox.showerror("Ошибка", "Ocean Proximity должен быть числом от 0 до 4.")
            return

        # Подготавливаем данные для модели
        input_data = pd.DataFrame([{
            'longitude': longitude,
            'latitude': latitude,
            'housing_median_age': housing_median_age,
            'total_rooms': total_rooms,
            'total_bedrooms': total_bedrooms,
            'population': population,
            'households': households,
            'median_income': median_income,
            'ocean_proximity': ocean_proximity
        }])

        # Загружаем модель
        model = load_model(save_path)

        # Получаем предсказание
        prediction = predict(model, input_data)

        # Выводим результат в окно
        messagebox.showinfo("Предсказание", f"Предсказанное значение: {prediction}")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите правильные числовые значения для всех полей.")

# Создание окна
root = tk.Tk()
root.title("Прогнозирование с XGBoost")

# Создание и размещение элементов
label_longitude = tk.Label(root, text="Longitude:")
label_longitude.grid(row=0, column=0)
entry_longitude = tk.Entry(root)
entry_longitude.grid(row=0, column=1)

label_latitude = tk.Label(root, text="Latitude:")
label_latitude.grid(row=1, column=0)
entry_latitude = tk.Entry(root)
entry_latitude.grid(row=1, column=1)

label_housing_median_age = tk.Label(root, text="Housing Median Age:")
label_housing_median_age.grid(row=2, column=0)
entry_housing_median_age = tk.Entry(root)
entry_housing_median_age.grid(row=2, column=1)

label_total_rooms = tk.Label(root, text="Total Rooms:")
label_total_rooms.grid(row=3, column=0)
entry_total_rooms = tk.Entry(root)
entry_total_rooms.grid(row=3, column=1)

label_total_bedrooms = tk.Label(root, text="Total Bedrooms:")
label_total_bedrooms.grid(row=4, column=0)
entry_total_bedrooms = tk.Entry(root)
entry_total_bedrooms.grid(row=4, column=1)

label_population = tk.Label(root, text="Population:")
label_population.grid(row=5, column=0)
entry_population = tk.Entry(root)
entry_population.grid(row=5, column=1)

label_households = tk.Label(root, text="Households:")
label_households.grid(row=6, column=0)
entry_households = tk.Entry(root)
entry_households.grid(row=6, column=1)

label_median_income = tk.Label(root, text="Median Income:")
label_median_income.grid(row=7, column=0)
entry_median_income = tk.Entry(root)
entry_median_income.grid(row=7, column=1)

label_ocean_proximity = tk.Label(root, text="Ocean Proximity (0-4):")
label_ocean_proximity.grid(row=8, column=0)
entry_ocean_proximity = tk.Entry(root)
entry_ocean_proximity.grid(row=8, column=1)

# Кнопка для предсказания
button_predict = tk.Button(root, text="Предсказать", command=on_predict)
button_predict.grid(row=9, columnspan=2)

# Запуск интерфейса
root.mainloop()
