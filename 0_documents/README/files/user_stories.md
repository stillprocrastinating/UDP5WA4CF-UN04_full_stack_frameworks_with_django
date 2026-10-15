<!-- # User stories

| # | Description | Goal(s) |
|-|-|-|
| 1 | As an admin, I want edit functionality for test questions. | Build a `Question()` class to model CRUD functions for admins. |
| 2 | As a tester, I want to edit tests I host. | Build a `Test()` class to model CRUD functions.<br>Utilise `django.allauth` to manage login capabilities for `Test()`. |
| 3 | As a tester, I want to edit test answers of my students. | Build an `Answer()` class to model CRUD functions.<br>Utilise `django.allauth` to manage login capabilities for `Answer()`. |
| 4 | As a student, I want to be able to prepare for which questions may occur on the test. | Utilise `django.allauth` to manage login capabilities, disallowed to students, to allow students to see the questions in their entirety, without providing the answers. |
| 5 | As a tester, I want to be able to see which questions are more difficult than others. | Build a `calculateDifficultyQuestion()` function which classifies `Question()` based on the frequency of correct `Answer()`. |
| 6 | As a tester, I want to be able to tell the difference between a question being difficult because it is difficult or because I am teaching it poorly. | Build a `calculateWarningQuestion()` function which classifies `Question()` based on the frequency of specific incorrect `Answer()`. |
| 7 | As a tester, I want to be able to see which tests were more difficult than others. | Build a `calculateDifficultyTest()` function which pulls from `calculateDifficultyQuestion()` per `Test()`. |


## Progress

| Complete | # | Goal |
|-|-|-|
| :ballot_box_with_check: | 1.1 | Build a `Question()` class to model CRUD functions for admins. |
| :ballot_box_with_check: | 2.1 | Build a `Test()` class to model CRUD functions. |
| :ballot_box_with_check: | 2.2 | Utilise `django.allauth` to manage login capabilities for `Test()`. |
| :ballot_box_with_check: | 3.1 | Build an `Answer()` class to model CRUD functions. |
| :ballot_box_with_check: | 3.2 | Utilise `django.allauth` to manage login capabilities for `Answer()`. |
| :ballot_box_with_check: | 4.1 | Utilise `django.allauth` to manage login capabilities, disallowed to students, to allow students to see the questions in their entirety, without providing the answers straight away. |
| :ballot_box_with_check: | 5.1 | Build a `calculateDifficultyQuestion()` function which classifies `Question()` based on the frequency of correct `Answer()`. |
| :ballot_box_with_check: | 6.1 | Build a `calculateWarningQuestion()` function which classifies `Question()` based on the frequency of specific incorrect `Answer()`. |
| :ballot_box_with_check: | 7.1 | Build a `calculateDifficultyTest()` function which pulls from `calculateDifficultyQuestion()` per `Test()`. |


## Future plans

- As an admin, I want to upgrade this project to include all question types and learning modules (not just multiple choice questions for the _Ethics 1_ module).
- As an admin, I want verification for the testers so that not any layperson may create an account.
- As an admin, I want the testers to see question warnings only for their personal tests, not anyone elses' tests.
    <!-- For the purposes of the milestone project, this is silly, for the real thing: Utilise {% if user.is_authenticated and test.tester == user %} -\->
- As a tester, I want potential students to be able to reach my course information and email address.
- As a tester, I want to be able to compare my statistics against everyone elses statistics (average/cumulative, not personal).
- As a tester, I want to be able to see my statistics in a graphical format for ease of understanding.
- As a tester, it can be wearisome to create novel tests which aren't too easy or difficult, so a test generator could be useful.
- As a user, some of the site may be difficult to understand the purpose of certain features, question mark icons for interactive explanations could be helpful. -->
