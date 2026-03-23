# Project Report: AI-Assisted Development

## 1. Initial Approach
* **Understanding:** My strategy was to use a "scaffold-first" approach. By starting with a structured file containing `TODO` comments and stubs, I focused on implementing the core logic of Bubble Sort (swapping and boundaries) before worrying about the user interface or input validation.
* **Assumptions:** I initially assumed that connecting the local project to GitHub would be a single-command process. I also assumed that Python’s `split()` and `int()` functions would handle messy user input (like extra spaces) automatically without needing explicit `.strip()` calls.

## 2. Prompting & AI Interaction
* **Successes:** Providing the full "scaffold" code in the prompt worked best. It allowed the AI to understand the exact naming conventions and types required (like `List[int]` and `Optional`), resulting in code that integrated perfectly without needing manual refactoring. 
* **Failures:** When I first tried to push to GitHub, I encountered the `src refspec main does not match any` error. While I initially asked for the "push command," the AI didn't immediately realize I hadn't made an initial commit yet. It provided the push command again, which resulted in the same error because the local repository was still technically "empty" in Git's eyes.
* **Analysis:** These failures happened because of a lack of **state context**. The AI knew the command to push but didn't know the current state of my local Git history. This impacted my progress by creating a 10-minute loop of terminal errors until I explicitly shared the error log.

## 3. Key Learnings
* **Technical Skills:** * **Bubble Sort Optimization:** I mastered the "early-stop" logic using a boolean flag, which improves the best-case time complexity to $O(n)$.
    * **Git Workflow:** I learned that `git remote add` is only half the battle; you cannot push a branch until a commit exists to define that branch.
    * **Input Sanitization:** I practiced using `try-except` blocks to make the program "crash-proof" against non-integer user input.
* **AI Workflow:** In my next project, I will provide **error logs** and **terminal output** alongside my code queries immediately. I've realized that showing the "symptom" (the error) is just as important as showing the "goal" (the code).