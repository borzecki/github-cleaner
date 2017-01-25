
# github-cleaner


    cleaning service for your dirty pull requests



## Installation

Make sure you have python and python-pip installed.
From the project folder run:

```
sudo pip install -r requirements.txt
```

## Configuration

This tool uses `PyGithub` library for communication with GitHub. Authentication is handled by providing environmental variable `GITHUB_TOKEN` which should be generated using instructions from [github help pages](https://help.github.com/articles/creating-an-access-token-for-command-line-use/).

```
export GITHUB_TOKEN='{TOKEN}'
```

## Usage

In order to clean your pull requests you'll also need to provide repository name and define filter function.

### Hint

You can use this super secret command to get a list of all your repositories.

```
python github-cleaner list_repos
```

### Provide filter function

Last step is to provide a function which will determine whether comment should be deleted.
To do this simply overwrite method `should_delete`.

```python
def should_delete(comment):
    return any([
        'Killer feature, ship it immediately' in comment.body,
        comment.user.login == 'borzecki'
    ]),
```

Now simply run this command with chosen repository:
```
python github-cleaner clean_pulls --name={REPOSITORY_NAME}
```
