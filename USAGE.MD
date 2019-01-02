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

Next we query for 'b', 'c', 'd', etc. And once we found the winner, we increment the SUBSTRING-index and continue with the second character, and so on and so forth, until we know the entire string. You will eventually expose the complete string, but it may take a sweet while. Not only do we need to try all a-z and A-Z, but also a bunch of special characters (about 64 in total).

Lets say that the webpage responds within 0.5 seconds. But if it takes longer than 3, we can safely conclude that we found the correct character. Now we estimate the time needed for a SMS-message sized string (160 characters):
```math
~32 wrong guesses * 0.5 sec per wrong guess =  16 seconds
1 correct guess * 3 sec per correct guess = 3 seconds
(16 + 3) * 160 characters = 3040 sec = about 50 minutes
```
My life is too short to wait for this. So I wrote binary search in the meanwhile. With binary search, you can find any value within a range of 64 values in 6 guesses. About half of the guesses will be correct and therefor slow. 
```
3 * 3 seconds = 9 seconds for incorrect guesses
3 * 0.5 second = 1.5 second for the correct guesses
(9 + 1.5) * 160 characters = 1680 seconds = 28 minutes.
```
As you can see, in a real world scenario, applying a binary search algorithm may significantly speed up the guessing process. Also the total number of requests is reduced from 5280 to 960. 

