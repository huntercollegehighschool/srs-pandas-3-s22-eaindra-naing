# 1. Import pandas
import pandas as pd

# 2. Read the "metacritic2.csv" file, and save the data in a dataframe variable. Print the data
crit = pd.read_csv('metacritic2.csv')
print (crit)

# 3. Create a new dataframe with only Mario Games. Save that in a new dataframe variable and print that data (this will involve Boolean indexing)

mario = crit[crit["Game"].str.contains("Mario")]
print (mario)


# 4. Sort the Mario data by release year in descending order. (a .sort_values() function exists)


marioryear = mario.sort_values("Release Year", ascending = False)
print (marioryear)


# 5. Last time we used a loop to find individual data on different platforms, years, etc. There is a .groupby() function that exists as well. Let's start by grouping by Release Year. Run the following code:
# <var> = <dataframe>.groupby("Release Year").count()
# What does it seems like count presents?

critgroup = crit.groupby("Release Year").count()
print (critgroup)

# 6. Use groupby again, but this time on Platform. Afterwards, run .count(), .mean(), and .median(). Which platform looks like it has the best games?

critcount = crit.groupby("Platform").count()
print (critcount)
critmean = crit.groupby("Platform").mean()
print (critmean)
critmedian = crit.groupby("Platform").median()
print (critmedian)

# 7. Create a new dataframe from the HunterAMC.csv file.

amc = pd.read_csv('HunterAMC.csv', sep = "\t")
print (amc)

# 8. In that csv, contest 0 is the AMC 10, and contest 2 is the AMC 12. Create two separate dataframes containing data from the two different contests.

amc10 = amc[amc["contest"] == 0]
amc12 = amc[amc["contest"] == 2]

# 9. Find the average scores for each contest.

avg10 = amc10["TotalScore"].mean()
avg12 = amc12["TotalScore"].mean()

# 10. For each column, count how often each answer choice was selected.

print (avg10.count())
print (avg12.count())

