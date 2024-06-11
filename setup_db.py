import sqlite3

conn = sqlite3.connect('questions.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS QUESTIONS (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT NOT NULL, 
        markdown TEXT NOT NULL
    )
''')

markdown = """
## [Next Happy Number](https://practice.geeksforgeeks.org/problems/next-happy-number4538/1)

### For a given non-negative integer N, find the next smallest Happy Number. A number is called Happy if it leads to 1 after a sequence of steps. Wherein at each step the number is replaced by the sum of squares of its digits that is, if we start with Happy Number and keep replacing it with sum of squares of its digits, we reach 1 at some point.

```cpp

class Solution{
public:
    bool solve(int n){
        if(n==1 || n==7) return true;
        if(n==2 || n==3 || n==4 || n==8 || n==5 || n==6 || n==9) return false;
        int sq_sum=0;
        while(n){
            int x=n%10;
            sq_sum+=x*x;
            n/=10;
        }
        return solve(sq_sum);
    }
    int nextHappy(int n){
        while(true){
            n++;
            if(solve(n)) return n;
        }
        return 0;
    }
};

```
## Explaination

![Explaination Image](assets/image_Happy_Num.png)

The `solve` function checks if a given number `n` is a happy number. It handles the base cases where `n` is already known to be happy (1 or 7) or not happy (2, 3, 4, 5, 6, 8, 9). For other numbers, it calculates the sum of squares of its digits by repeatedly taking the modulo 10 of the number (`x = n % 10`) to get the last digit, squaring it (`x * x`), and adding it to `sq_sum`. Then, it updates `n` by dividing it by 10 (`n /= 10`) to remove the last digit. The process continues until `n` becomes 0, at which point the function recursively calls itself with the calculated `sq_sum`. This process repeats until `n` eventually becomes 1 or falls into a cycle, returning `true` or `false` accordingly.

The `nextHappy` function finds the next happy number greater than the given input `n`. It starts an infinite loop and increments `n` by 1 in each iteration. For each `n`, it checks if it is a happy number by calling the `solve` function. If `n` is found to be happy, it is returned as the next smallest happy number. The loop continues until a happy number is found.

## iterative approch via chatGPT

Alternative approaches and the best approach depend on the requirements and constraints of the problem. However, here's an alternative approach to finding the next smallest happy number:

```cpp
class Solution {
public:
    bool isHappy(int n) {
        while (true) {
            int sum = 0;
            while (n > 0) {
                int digit = n % 10;
                sum += digit * digit;
                n /= 10;
            }
            if (sum == 1) return true;
            if (sum == 4) return false;
            n = sum;
        }
    }

    int nextHappy(int n) {
        n++;
        while (!isHappy(n)) {
            n++;
        }
        return n;
    }
};
```

1. Create a helper function `isHappy` that checks if a given number `n` is a happy number.
2. Iterate from `n+1` onwards to find the next happy number:
   a. While `isHappy` returns false, increment `n` by 1.
3. Once a happy number is found, return it as the next smallest happy number.

This approach eliminates the recursive function `solve` and replaces it with a separate helper function `isHappy`, which simplifies the code and avoids potential stack overflow issues for large values of `n`.

Regarding space complexity, both the given code and the alternative approach have space complexity of O(1) since they don't use any additional data structures whose size depends on the input size.
"""

title = 'Data Structures'
description = 'Learn about arrays, linked lists, stacks, queues, trees, graphs, and more.'

cursor.execute(
    '''
    INSERT INTO QUESTIONS (title, description, markdown) VALUES (?, ?, ?)
''', (title, description, markdown))
conn.commit()
conn.close()