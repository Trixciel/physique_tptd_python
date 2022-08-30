import numpy as np
import matplotlib.pyplot as plt
#Q2
Us=np.array([1.02,1.51,1.98,2.47,3.05,3.5,3.97,4.63,5,5.52,6.03,7.04,7.62]) #V
Is=np.array([1.2,2.4,3.4,5.2,7.4,10.0,12.5,17.7,20.6,26.2,32.0,47.5,59.8]) #A
plt.clf()
plt.plot(Us,Is,"xk",label="Données exp")
plt.xlabel("Tension (V)")
plt.ylabel("Courant (A)")
plt.grid()
#Q2
######
#Q3
alpha,lnK=np.polyfit(np.log(Us),np.log(Is),1)
K=np.exp(lnK)
print(f"On a K = {round(K,3)} A/V et alpha = {round(alpha,3)} sans unité.")
#Q3
######
#Q4
UReg=np.array(list(range(1,80)))/10 #V (tensions de 0.1V à 7.9 V)
IReg=K*UReg**alpha #A
plt.plot(UReg,IReg,"-b",label="Regression")
#Q4
######
plt.legend()
plt.show()