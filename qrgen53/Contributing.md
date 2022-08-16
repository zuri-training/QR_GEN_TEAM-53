# Contributing to this project

We would love your contributions to the `QR GEN` project. Please review the following guidelines before contributing
in order to make the contribution process easy and uniform for all the contributors. You can also propose changes to
these guidelines by updating this file and submitting a pull request.

- [I have a question...](#have-a-question)
- [I found a bug...](#found-a-bug)
- [I have a feature request...](#have-a-feature-request)
- [I have a contribution to share...](#have-a-contribution)

# Have a question?

Ask your question in the team's Slack channel.

# Found a bug

1. Check if the [issues](https://github.com/zuri-training/QR_GEN_TEAM-53/issues) tab to see if it has already been
   reported, or fixed.

2. If the issue has not been created or
   fixed, [create](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue#creating-an-issue-from-a-repository)
   a new [issue](https://github.com/zuri-training/QR_GEN_TEAM-53/issues/new) .

   When creating a new issue, please **provide as much information as possible** so the problem
   can be easily found, and then fixed. The issue should also **contain a descriptive title and a
   brief summary**. If you have a potential solution to the problem already, feel free
   to submit
   a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)
   with your proposed solution to the problem, or you can also explain your solution in the issue description.

# Have a feature request?

All feature requests should be started by adding the feature, with all necessary information - including your name, to
the document containing all proposed features in the team's Slack channel description. After doing this,
an [issue](https://github.com/zuri-training/QR_GEN_TEAM-53/issues/new) can be submitted documenting the proposed
feature.

# Have a contribution to make?

1. [Fork](https://help.github.com/articles/fork-a-repo)
   the [QR_gen repository](https://github.com/zuri-training/QR_GEN_TEAM-53).

2. Clone your forked copy of the repository.

    ```
    git clone https://github.com/<your-github-username>/QR_GEN_TEAM-53.git
    ```

3. Check the current remote repository for your fork.

    ```
    git remote -v

    <!--- What you should see -->
    > origin  https://github.com/<your-github-username>/QR_GEN_TEAM-53.git (fetch)
    > origin  https://github.com/<your-github-username>/QR_GEN_TEAM-53.git (push)
    ```

4. Add a new remote _upstream_ repository.

    ```
    git remote add upstream https://github.com/zuri-training/QR_GEN_TEAM-53.git
    ```

5. Verify the new upstream repository has been added.

    ```
    git remote -v

    <!--- What you should see -->
    > origin  https://github.com/<your-github-username>/QR_GEN_TEAM-53.git (fetch)
    > origin  https://github.com/<your-github-username>/QR_GEN_TEAM-53.git (push)
    > upstream        https://github.com/zuri-training/QR_GEN_TEAM-53.git (fetch)
    > upstream        https://github.com/zuri-training/QR_GEN_TEAM-53.git (push)
    ```

6. Sync your fork with the upstream repository.

    ```
    git fetch upstream
    ...

    git merge upstream/main
    ...
    ```

7. Create a new branch and switch to the newly created branch.

    ```
    git checkout -b <name_of_your_new_branch>
    ```

8. Make your desired changes to the code in the repository.

9. Add all new and updated files to the staging area.

    ```
    git add .
    ```

10. Commit the new changes.

    ```
    git commit -m "<descriptive_commit_message>"
    ```

11. Switch back to the `main` branch.

    ```
    git checkout main
    ```

    After running the `git checkout` command, **repeat step 6** to ensure your fork and the upstream repository are
    still in sync.

12. Push the committed changes in your current branch to the remote repository.

    ```
    git push -u origin <your_branch_name>
    ```

13. [Create a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)
    .

## Run locally.

If you want to run locally,then you can use the following command to run locally on your machine:

Clone the project

```
  git clone git@github.com:zuri-training/QR_GEN_TEAM-53.git
```

Go to the project directory

```
  cd QR_GEN_TEAM-53.git
```

Create a Virtual Environment

```
python -m venv venv
```

Activate Virtual Environment

```
venv\scripts\activate
```

Install Dependencies

```
  pip install -r requirements.txt
```

make migrations

```
python manage.py makemigrations
```

Migrate the database

```
python manage.py migrate
```

create superuser

```
python manage.py createsuperuser
```

Finally, Start The Server.

```
python manage.py runserver
```

*important*
Always pull before making new changes
After making changes Do not merge,push the branch you made changes on to the repo,and then make a pull request on github




