import pandas as pd

sub_1_v1 = pd.read_csv("./sub_1_v1.csv") # jan: 
sub_1_v2 = pd.read_csv("./sub_1_v2.csv")
sub_2_v1 = pd.read_csv("./sub_2_v1.csv") # jan: 1691359541.0418816, fev: 1344249711.646313, mar: 1742131085.0023522
sub_2_v2 = pd.read_csv("./sub_2_v2.csv") # jan: 1669822217.8894515, fev: 1316782751.9076555, mar: 1770674904.4219131
sub_2_v3 = pd.read_csv("./sub_2_v3.csv") # jan: 1651296854.322644 , fev: 1323600494.1822453, mar: 1774719891.0740142


sub = pd.DataFrame(columns=["cod_loja","faturamento","jan","fev","mar"])

sub["cod_loja"] = sub_2_v1["cod_loja"].values
sub["jan"] = sub_2_v3["jan"].values
sub["fev"] = sub_2_v2["fev"].values
sub["mar"] = sub_2_v1["jan"]

sub["faturamento"] = (sub["jan"].values + sub["fev"].values + sub["mar"].values)/3
print(sub)
print(sub["faturamento"].sum())
print(sub_2_v3["faturamento"].sum())

sub.to_csv("./sub_2_join_version",sep=";",index=False)
sub[["cod_loja","faturamento"]].to_csv("./desafio_2_join_version",sep=";",index=False)

