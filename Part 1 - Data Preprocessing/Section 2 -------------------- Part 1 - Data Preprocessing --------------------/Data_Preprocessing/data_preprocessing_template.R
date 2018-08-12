# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('Data.csv')


#Take care of the missing values
dataset$Age = ifelse(is.na(dataset$Age),ave(dataset$Age,FUN = function(X) mean(X,na.rm = TRUE)),dataset$Age) 
dataset$Salary = ifelse(is.na(dataset$Salary),ave(dataset$Salary,FUN = function(X) mean(X,na.rm = TRUE)),dataset$Salary) 

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')


# Feature Scaling
# training_set = scale(training_set)
# test_set = scale(test_set)