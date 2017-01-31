#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)

### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
feature_3 = "total_payments"
poi  = "poi"

# Let's see what are the min and max of exercised_stock_options
# First Step : Find the stock options.
stock_options = []
for key, value in data_dict.iteritems():
    if value['exercised_stock_options'] != 'NaN':
        stock_options.append(value['exercised_stock_options'])
print "stock:", stock_options

# Then order this list
stock_options_sorted = sorted(stock_options)
print "Stock options sorted", stock_options_sorted
# Then print the min and the max
min_stock = stock_options_sorted[0]
print "Minimum stock options:", min_stock
# Don't forget to - 1 because the key of an array begin at 0 not 1.
lenght = len(stock_options_sorted)-1
max_stock = stock_options_sorted[lenght]
#print lenght
print "Maximum stock options:", max_stock

# Let's see what are the min and max of salary
# First Step : Find the salary.
salary = []
for key, value in data_dict.iteritems():
    if value['salary'] != 'NaN':
        salary.append(value['salary'])
print "salary:", salary

# Then order this list
salary_sorted = sorted(salary)
print "Salary sorted", salary_sorted
# Then print the min and the max
min_salary = salary_sorted[0]
print "Minimum salary:", min_salary
# Don't forget to - 1 because the key of an array begin at 0 not 1.
lenght = len(salary_sorted)-1
#print lenght
max_salary = salary_sorted[lenght]
print "Maximum salary:", max_salary

#Find rescaled value of stock that is = 1,000,000
stock_scale_val = 1000000.
from sklearn.preprocessing import MinMaxScaler
stock_weights = numpy.array([float(min_stock), stock_scale_val, float(max_stock)])
stock_scaler = MinMaxScaler()
rescaled_stock = stock_scaler.fit_transform(stock_weights)
print "Rescaled stock:", rescaled_stock

#Find rescaled value of salary that is = 200,000
salary_scale_val = 200000.
salary_weights = numpy.array([float(min_salary), salary_scale_val, float(max_salary)])
salary_scaler = MinMaxScaler()
rescaled_salary = salary_scaler.fit_transform(salary_weights)
print "Rescaled salary:", rescaled_salary 


features_list = [poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )


### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
for f1, f2 in finance_features:
    plt.scatter( f1, f2 )
plt.show()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred
from sklearn.cluster import KMeans
clf = KMeans(n_clusters=2)
clf.fit(finance_features)
pred = clf.predict(finance_features)



### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters3.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"
