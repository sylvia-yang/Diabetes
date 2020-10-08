# Diabetes
This is a python project to build a multiple linear regression model of diabetes disease progression against ten explantory variables including age, sex, bmi, etc.

This dataset is a built-in dataset from sklearn and it contains:

target(y): a quantitative measure of disease progression one year after baseline.
10 input variables (x): 
age,
sex,
body mass index,
average blood pressure,
six blood serum measurements.

Based on this project, our model is:
y =-28.2528924*(age)-192.27359695*(sex)+512.03905586*(bmi)+282.69909415*(bp)-630.4813557*(s1)+393.50457699*(s2)+20.19357534*(s3)+112.73522418*(s4)+696.38689731*(s5)+36.59645541(s6) + 150.04613206397468

Mean Squared Error (MSE) is: 2822.72

R^2 is: 0.60

Therefore, we can make the conclustion that the diabetes disease progression depends on these factors, including age, sex, body mass index, average blood pressure, six blood serum measurements.
