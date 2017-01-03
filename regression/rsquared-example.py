plt.scatter(ages, net_worths)
plt.xlabel("ages")
plt.ylabel("net worths")
plt.show()


from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(ages, net_worths)

print "prediction (needs to be in list syntax):", reg.predict([27]) 

print "slope:", reg.coef_
print "intercept:", reg.intercept_
print "r-squared score:", reg.score(ages, net_worths)

plt.scatter(ages, net_worths)
plt.plot(ages, reg.predict(ages), color='blue', linewidth=3)
plt.xlabel("ages")
plt.ylabel("net worths")
plt.show()
