import pandas as pd
data={'Name':['Alice', 'Bob', 'Charlie'], 'Age':[24, 22, 654565564525445232345], 'City':["Prishtina", "Peja", "Krungthepmahanakhon Amonrattanakosin Mahintharayutthaya Mahadilokphop Noppharatratchathaniburirom Udomratchaniwetmahasathan Amonphimanawatansathit Sakkathattiyawitsanukamprasit"]}
df=pd.DataFrame(data)
print(df)
df.to_csv("output.csv", index=False)