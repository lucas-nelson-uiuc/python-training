# Python Training

Collection of bite-sized Python exercises to test common concepts and applications of the language.

This package is heavily inspired by the `rustlings` project. Although `python-training` cannot overlap entirely with `rustlings`, many of its ideas, philosophies, and applications can be seen across both projects.

### Getting Started

Section below not correct.

```
# install package
pip install python-training

# pull latest version from GitHub
git clone https://github.com/lucas-nelson-uiuc/python-training.git
```

### Completing Exercises

All chapters have a list of topics with exercises for the user to complete and can be found under each chapter's folder (`topics/<chapter>/exercises`). Each subtopic is its own script, containing a collection of `TODO` prompts for the user to complete. An example of a simple exercise looks like such:

```python
def name_of_problem():
    # TODO: instructions for solving the problem
    solution = ...
    return solution
```

> #### *The following feature is in-progress*

For all problems, the solution can be found tracing the same path in the `solutions` folder (`solutions/<chapter>/topic`). If you need to review the solution for a problem(s), rather than opening the file yourself, you can use the command line argument `pt --hint` to get a hint for the problem(s) requested.

```bash
# requesting a hint for a problem
pt --hint <topic_name>
pt --hint <topic_name>[<problem_name>]

# example: requesting a hint for the string problems
pt --hint strings

# example: requesting a hint for the string concatenation problem
pt --hint strings[string_concatenation]
```

### TODO

* Command line interface

* Integrate tests for package

    - `setup` can correctly create folders

    - `solutions` correctly answers respective question(s)

* Finish setting up GitHub repository for contributing/using

### Contributing

See link to `Contributing.md`
