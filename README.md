To create a new branch in Git, add a file to that branch, and then push the changes to the remote repository,
you can follow these steps:

> 1. git branch new_branch_name
> 2. git checkout new_branch_name
> 3. git add your_ne_file
> 4. git commit -m "Add new_file.txt to new branch"
> 5. git push origin new_branch_name
> 
> 
> (Note: you can combine previous steps (1 and 2) with this command:)
> git checkout -b new_branch_name
> 
> 
> If this is the first time pushing this branch, you may need to use the --set-upstream option:
>> git push --set-upstream origin new_branch_name 
> 
> To Undo pushes that already done
> git reset --soft HEAD~1
> git push origin main --force


small changes to the main branch readme