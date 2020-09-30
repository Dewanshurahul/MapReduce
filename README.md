# HADOOP

Hadoop has a Master-Slave Architecture for data storage and distributed data processing using MapReduce and HDFS methods.

  - The Hadoop Distributed File System(HDFS) is the primary data storage system used by Hadoop applications
  - Hadoop MapReduce is a software framework for distributed processing of large data sets on compute clusters of commodity hardware.


The problem is to implement MapReduce on HDFS and slove the given Problem Statements using the given Data Set
  - The dataset consists of 37 columns and 2M Rows from which some of them are used for Solving the Problem
  - 5th column is Gender
  - 25th column is Salary
  - 26th column is Last % Hike
  - 30th column is Country
  - 31st column is City
  - 34th column is Region

Question 1 :- Count number of employees in each Region, Country and City.
Solution :- The solution for this Question is divided into three parts
 - 1st :- For Region
 - - I have used mapper as employeeRegion_mapper.py file
 - - And for reducer Employee_Reducer.py file
 - - Command to execute is 
```sh
$ hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -input /hadoop/input/HR2m.csv -output /hadoop/output/employee_region -mapper employeeRegion_mapper.py -combiner combiner.py -reducer Employee_Reducer.py
```

OutPut Image :- 
<img src=outputImages/regionOutput.png>

 - 2nd :- For Country
 - - I have used mapper as EmployeeCountry_Mapper.py file
 - - And for reducer Employee_Reducer.py file
 - - Command to execute is 
```sh
$ hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -input /hadoop/input/HR2m.csv -output /hadoop/output/employee_country -mapper EmployeeCountry_Mapper.py -combiner combiner.py -reducer Employee_Reducer.py
```
OutPut Image :- 
<img src=outputImages/countryOutput.png>

 - 3rd :- For City
 - - I have used mapper as EmployeeCity_Mapper.py file
 - - And for reducer Employee_Reducer.py file
 - - Command to execute is 
```sh
$ hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -input /hadoop/input/HR2m.csv -output /hadoop/output/employee_city -mapper EmployeeCity_Mapper.py -combiner combiner.py -reducer Employee_Reducer.py
```

OutPut Image :- 
<img src=outputImages/cityOutput.png>

Question 2:- Summary for Employee
Solution - This part is taken care in Different Question of this exercise

Question 3:- Orderby Gender and Salary
Solution :- The solution for this Question is divided into three parts
 - 1st :- For Gender
 - - I have used mapper as order_by_gender.py file
 - - And for reducer gender_sort.py file
 - - Command to execute is 
```sh
$ hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -input /hadoop/input/HR2m.csv -output /hadoop/output/data_sorted_by_gender -mapper order_by_gender.py -reducer gender_sort.py
```

 - 2nd :- For Salary
 - - I have used mapper as sort_salary_mapper.py file
 - - And for reducer sortter.py file
 - - Command to execute is 
```sh
$ hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -input /hadoop/input/HR2m.csv -output /hadoop/output/data_sorted_by_salary -mapper sort_salary_mapper.py -reducer sortter.py
```

OutPut Image :- 
<img src=outputImages/salarySorted.png>

Question 4 :- Summarise the number of emp joined and hickes granted based on month
Solution :- In this Problem I have used
 - as mapper hikes_granted_mapper.py file
 - as reducer Employee_Reducer.py file
 - command to execute is :-
```sh
$ hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -input /hadoop/input/HR2m.csv -output /hadoop/output/hikes_granted_based_on_month -mapper hikes_granted_mapper.py -reducer Employee_Reducer.py
```

OutPut Image :- 
<img src=outputImages/hikeGranted.png>

Question 5 :- Salary wise sort employee data
Solution :- In this problem I have used
 - as mapper sort_salary_mapper.py file
 - as reducer sortter.py file
 - command to execute
```sh
$ hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -input /hadoop/input/HR2m.csv -output /hadoop/output/data_sorted_by_salary -mapper sort_salary_mapper.py -reducer sortter.py
```

OutPut Image :- 
<img src=outputImages/salarySorted.png>
