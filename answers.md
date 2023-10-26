# Quiz questions

This is only a "quiz" in the loosest sense that it's asking questions whose
answers will be part of your grade. Please use *any resources you want*, as
long as you list those resources (e.g. peers, websites, etc.)

## Navigating logs

1. What is the SHA for the last commit made by Prof. Xanda on the branch
xanda_0000_movie_processing?
(For this and future questions, the first 5 characters is plenty - neither
Git nor I need the whole SHA.)
9b257

2. What is the SHA for the last commit associated with line 9 of this file?
b2ed3

3. What did line 12 of this file say in commit d1d83?
```
2. I should really finish writing this.
```

4. What changed between commit e474c and 82045?
```
diff --git a/process_movie_data.py b/process_movie_data.py
index 71f23e1..13b0caa 100644
--- a/process_movie_data.py
+++ b/process_movie_data.py
@@ -15,9 +15,9 @@ def find_top_5(filename):
         rows = [r for r in csvr]
     
     # Sort data and get top 5
-    gross_sort = lambda x : x["Gross"]
+    gross_sort = lambda x : int(x["Gross"])
     rows.sort(key=gross_sort)
-    top_five = rows[:-5:-1]
+    top_five = rows[:-6:-1]
 
     # Print out results
     for row in top_five:
```

It looks like we added an int cast to gross_sort and included an earlier element in top_five

## Predicting merges

Assume at the start of each of these three questions that your
branch for switching to a top-10 list was called `top_ten`
and your branch generalizing to any number of movies was called `top_N`.
Predict the behavior of these three possible operations - you don't
have to provide a full `diff` but you should describe at a high level
what changes would happen.

These questions are supposed to be separate paths, not cumulative;
for example, you should *not* assume that the operations of 5 were run
before 6. When testing outcomes later in the lab, you should make sure to
revert back to the state of the branch before you started these questions.

5. What do you think would happen if you ran the following commands?
What branches would change, and how?
```
git checkout test
git merge top_N
```
Move head of test to top_N, "adding" changes accordingly.

6. What do you think would happen if you ran the following commands?
What branches would change, and how?
```
git checkout top_ten
git merge test
```
Add changes from test to top_ten, i.e. rename quiz.md to answers.md. Test remains unchanged.

7. What do you think would happen if you ran the following commands?
What branches would change, and how?
```
git checkout test
git rebase top_ten
git rebase top_N
```

Changes are retroactively appplied such that the final commit history appears as test (answers.md change) -> top_N (because rebased second) -> top_ten -> test, with the changes of all preceeding elements applied to following elements.

Conflict between top_N and top_ten in function signature and doc comments.

