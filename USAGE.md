# Real world example
Consider this rather common sql query which is uses in many webapplications:

```sql
SELECT x,y FROM z WHERE z.id=10 
```

The value '10' is supplied by the user. If this value is not properly validated 
or sanitized, any innocent bystander might make a typo in the URL-bar and 
accidentally turn the query into this:

```sql
SELECT x,y 
FROM z 
WHERE z.id=10 
UNION SELECT 1,GROUP_CONCAT(table_name) 
  FROM information_scheme.tables 
  WHERE table_schema = database()
```

Unfortunately, quite often, the webpage does not show the results of the query 
directly. This oversight severely limits the webpages functionality. But surely, 
it doesn't need to stay that way. 

Consider the following (convoluted) query carefully:

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
The nested SELECT yields a single string; a concatenation of all table names. 
We take the first character of this string, and turn it into an ascii (=integer) 
value. Next; the IF-statement tests if this ascii-value is equal to 41 (which 
happens to be the ascii value for 'a'). 

If this is TRUE, the database will go 
sleepy-time for about 3 seconds. Otherwise, it will respond immediately. We 
monitor the response-times closely to see if we have guessed correctly. If not, we
then query for 'b', 'c', 'd', etc. Not only do we need to try the range of a-z, but 
also A-Z, 0-9 and a bunch of special characters. Actually, the ascii range you'll 
want to query is from 32 to 127 (=95 characters).

This will, however, take ages to complete.

### Performance estimates
Lets say that this completely imaginary webpage responds within 0.5 seconds under 
normal conditions. If it takes longer than 3, this indicates that we have found the 
correct character. Given these parameters, we can estimate the time needed for a 
SMS-message sized string (160 characters):
```math
avg of (95/2) wrong guesses per char * 0.5 sec per wrong guess =  23.75 seconds
1 right guess * 3 sec per correct guess = 3 seconds
(23.75 + 3) * 160 characters = 4280 sec = about 71 minutes
```
Life is too short to leave this unoptimized. Luckily, with binary search, you can find 
any value within a range of 128 values in just 7 guesses. But about half of these guesses 
will be correct, and thus, slow. 
```
avg of 3.5 wrong guesses per char * 3 seconds = 11.5 seconds for incorrect guesses
avg of 3.5 right guesses per char * 0.5 second = 1.75 seconds
(11.5 + 1.75) * 160 characters = 2120 seconds = 35 minutes.
```
As you can see, in this scenario, applying a binary search algorithm may speed up the 
guessing process by over 200%. Also the total number of requests is reduced from 8160 
to 1120. It's still noisy as hell. But it's much less likely to accidentaly overload 
the server.

