CalculusOCR contribution guidelines
===============================

## Issue reporting/feature requests

* **Already reported**? Browse the [existing issues](https://github.com/JignasP/CalculusOCR/issues) to make sure your issue/feature hasn't been reported/requested.
* **Already fixed**? Check whether your issue/feature is already fixed/implemented.
* **Still relevant**? Check if the issue still exists in the latest release/beta version.
* **Can you fix it**? If you are a Python developer, you are always welcome to fix an issue or implement a feature yourself. PRs welcome! See [Code contribution](#code-contribution) for more info.
* **Is it in English**? Issues in other languages will be ignored unless someone translates them.
* **The template**: Fill it out, everyone wins. Your issue has a chance of getting fixed.

## Code contribution

### Guidelines

* Stick to [Pypi contribution guidelines](https://pypi.org/policy/acceptable-use-policy/).
* In particular **do not bring non-free software** into the project. Make sure you do not introduce any closed-source library.

### Before starting development

* If you want to help out with an existing bug report or feature request, **leave a comment** on that issue saying you want to try your hand at it.
* If there is no existing issue for what you want to work on, **open a new one**  describing the changes you are planning to introduce. This gives the team and the community a chance to give **feedback** before you spend time on something that is already in development, should be done differently, or should be avoided completely.
* Please show **intention to maintain your features** and code after you contribute a PR. Unmaintained code is a hassle for core developers. If you do not intend to maintain features you plan to contribute, please rethink your submission, or clearly state that in the PR description.
* Create PRs that cover only **one specific issue/solution/bug**. Do not create PRs that are huge monoliths and could have been split into multiple independent contributions.

### Creating a Pull Request (PR)

* Please **test** (compile and run) your code before submitting changes! Ideally, provide test feedback in the PR description. Untested code will **not** be merged!
* Respond if someone requests changes or otherwise raises issues about your PRs.
* Try to figure out yourself why builds on our CI fail.
* Make sure your PR is **up-to-date** with the rest of the code. Often, a simple click on "Update branch" will do the job, but if not, you must *rebase* your branch on the `main` branch manually and resolve the conflicts on your own. 
