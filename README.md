# moloco-online-exam
code and answers to moloco online exam

First, I saved the data as a csv file. Then I imported the data to python 3 to start the code. 

#1. 
after selecting the entries with 'country_id' == 'BDV', I grouped the remaining columns by site_id and counted unique numbers of users. 

#2. 
I extracted the rows from the index '2019-02-03 00:00:00' to '2019-02-04 23:59:59'. Then I grouped the data by both user_id and site_id 
and counted the number of site visited. Next, I applied the condition to the data where the visited number exceeds 10. 

#3. 
I grouped the original data by user_id and applied to the site_id. Then I used the function 'nth' where it finds the nth value. I sorted
the number of unique users in descending order and chose the top three. 

#4. 
Similar to #3, I used the function 'nth' to find the user's first and last visit to the site. -1 indicatest the last and 0 indicates the first.
Then I used the equality operator (==) to find the boolean and applied to the first_visit data (applying to the last_visit data gives the same result). 

#5. 
For calculating A, I used for loop. For each site_id, I grouped by user_id and counted the unique country names. Then I found unique country_id 
greater than 1 (since the question asks for at least two countries visited). Calculation for B is similar as #1. For easier calculations 
of ratio, I created the answers for A and B as a dictionary. 
The question asks for the ratio of B to A, but calculating division right away is not applicable since three sites ('JSUUP','RT9Z6','EUZ/Q') 
have zero number of unique users. So I created a new dictionary A and B without those three sites and calculated the ratio B/A. 


