# How is binary search useful?
Well, just by itself, it's not. The supplied example code already shows the secret_value, so there is absolutely no need to deduce it. But there are certain scenario's where one might not actually know the secret_value. Then this little algorithm gets radically more interesting. 

Consider this rather common sql query which is uses in many webapplications:

```sql
SELECT x,y FROM z WHERE z.id=10 
```

The value '10' is supplied by the user. If this value is not properly validated or sanitized, any innocent bystander might make a typo in the URL-bar and accidentaly turn the query into this:

```sql
SELECT x,y 
FROM z 
WHERE z.id=10 
UNION SELECT 1,GROUP_CONCAT(table_name) 
  FROM information_scheme.tables 
  WHERE table_schema = database()
```

Unfortunately, quite often, the webpage does not show the results of the query directly. This oversight severely limits the webpages functionality. But surely, it doesn't need to stay that way. Consider the following convoluted query carefully:

```sql
SELECT x,y 
FROM z 
WHERE z.id=10 
AND IF( 
    ASCII(
        SUBSTRING(	
            (SELECT GROUP_CONCAT(table_name) 
	    FROM information_schema.tables 
	    WHERE table_scheme = database()),
	    1,1
        )
    ) = 41,
    SLEEP(3),
    NULL
)
```
The inner SELECT may return any string, in this case, a concatenation of all table names. Then the IF-statement tests if the first character of this string is equal to 41 (which is the ascii value for 'a'). If this is the case, the database will go sleepy-time for 3 seconds. So, this means that if the website is responding fast, we guessed the first letter wrong. We monitor the response-times closely to see if we have guessed correctly.

Next we query for 'b', 'c', 'd', etc. And once we found the winner, we increment the SUBSTRING-index and continue with the second character, and so on and so forth, until we know the entire string. You will eventually expose the complete string, but it may take a sweet while. Not only do we need to try all a-z, A-Z and 0-9, but also a bunch of special characters. Actually, the ascii range you'll want to query is from 32 to 127 (=95 characters).

Lets say that the webpage responds within 0.5 seconds. But if it takes longer than 3, we can safely conclude that we found the correct character. Now we estimate the time needed for a SMS-message sized string (160 characters):
```math
avg of 95/2 wrong guesses * 0.5 sec per wrong guess =  23.75 seconds
1 correct guess * 3 sec per correct guess = 3 seconds
(23.75 + 3) * 160 characters = 4280 sec = about 71 minutes
```
Life is too short to leave this unoptimized. Luckily, with binary search, you can find any value within a range of 128 values in just 7 guesses. But about half of these guesses will be correct, and thus, slow. 
```
avg of 3.5 wrong guesses * 3 seconds = 11.5 seconds for incorrect guesses
avg of 3.5 right guesses * 0.5 second = 1.75 seconds
(11.5 + 1.75) * 160 characters = 2120 seconds = 35 minutes.
```
As you can see, in this scenario, applying a binary search algorithm may speed up the guessing process by over 200%. Also the total number of requests is reduced from 8160 to 1120. It's still noisy as hell. But it's much less likely to accidentaly overload the server.

