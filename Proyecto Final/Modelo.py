#Librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model,preprocessing
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from collections import Counter
from imblearn.over_sampling import RandomOverSampler, SMOTE
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import classification_report, confusion_matrix, recall_score, log_loss
from sklearn.metrics import f1_score, accuracy_score, precision_score
from sklearn.model_selection import train_test_split, cross_val_score, ShuffleSplit

#importancion del dataset
df =pd.read_csv('fetal_health.csv',sep=",")


#Cargar las variables x y y
x=df[["baseline value","accelerations","fetal_movement","uterine_contractions","light_decelerations","severe_decelerations","prolongued_decelerations","abnormal_short_term_variability","mean_value_of_short_term_variability","percentage_of_time_with_abnormal_long_term_variability"]]
y=df["fetal_health"].values
#normalizacion de x
scaler=preprocessing.MinMaxScaler()
x=scaler.fit_transform(x)

#Division
x_train, x_test, y_train, y_test = train_test_split(x,y,random_state=42, train_size=0.7)

#Corrigiendo desbalanceo
ros_train = RandomOverSampler(random_state=1000)
x_train, y_train = ros_train.fit_resample(x_train, y_train)

ros_test = RandomOverSampler(random_state=1000)
x_test, y_test = ros_test.fit_resample(x_test, y_test)


#Entrenamiento del modelo
regs=linear_model.LogisticRegression(multi_class="multinomial",solver="lbfgs",C=1,max_iter=10000)
regs.fit(x_train,y_train)

#predicciones
def prediccion(datos):
    if regs.predict([datos])==1:
        return 1
    if regs.predict([datos])==2:
        return 2
    if regs.predict([datos])==3:
        return 3

