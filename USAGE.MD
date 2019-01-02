# How is binary search useful?
Well, just by itself, it's not. The example code already knows the secret_value, so there is absolutely no need to deduce it. But there are certain scenario's where one might not actually know the secret_value. Then this little algorithm gets radically more interesting. 

For example, consider this rather common sql query which is uses in many webapplications:

```sql
SELECT x,y FROM z WHERE z.id=10 
```

The value 10 is often supplied by the user. If this value is not properly validated or sanitized, any innocent bystander might make a typo in the URL-bar and turn the query into this:

```sql
SELECT x,y 
FROM z 
WHERE z.id=10 
UNION SELECT 1,GROUP_CONCAT(table_name) 
  FROM information_scheme.tables 
  WHERE table_schema = database()
```

However, more often than not, the webpage doesn't directly show the results of the query directly. This oversight severely limits the websites' functionality. But it doesn't need to stay this way. Consider the following convoluted query carefully:

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
    ) == 41,
    SLEEP(5),
    NULL
)
```
The inner SELECT may return any string, in this case, a concatenation of all table names. Then the IF-statement tests if the first character of this string is equal to 41 (which is the ascii value for 'a'). If this is the case, the database will go sleepy-time for 5 seconds. But if the website is responding quickly, we guessed the first letter wrong. We monitor the response-times closely to see if we have guessed correctly.

Next we query for 'b', 'c', 'd', etc. And once we have a winner, we increment the SUBSTRING-index and continue with the second character, and so on and so forth, Until we know the entire string. This will ofcourse, take ages. Not only do we need to try all a-z and A-Z, but also a bunch of special characters (about 65 in total).

Lets make an optimistic calculation of the time needed for a SMS-message sized string (160 characters):
```
160 characters * ~32 wrong guesses * 1 sec per wrong guess =  5120 seconds
160 characters * 1 correct guess * 2 sec per correct guess = 320 seconds
5120 sec + 320 sec = 5420 sec = about 1.5 hour
```
My life is too short to wait for this. So I wrote binary search in the meanwhile.  
