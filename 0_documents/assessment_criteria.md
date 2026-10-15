<!-- # Project Requirements

## Main Technologies

- HTML, CSS, JavaScript, Python+Django
- Relational database (recommending MySQL or Postgres)
- Any additional libraries and external APIs

## Mandatory Requirements

A project violating any of these requirements will FAIL

1. Data handling: Build a Relational Database backed project for a web application that allows users to store and manipulate data records about a particular domain.
2. Database structure: Put some effort into designing a database structure well-suited for your domain. Make sure to put some thought into the relationships between records of different entities.
3. User functionality: Create functionality for users to create, locate, display, edit and delete records (CRUD functionality).
4. Use of technologies: Use HTML and custom CSS for the website's front-end.
5. Structure: Incorporate a main navigation menu and structured layout (you might want to use Bootstrap to accomplish this).
6. Documentation: Write a README.md file for your project that explains what the project does and the value that it provides to its users.
7. Version control: Use Git & GitHub for version control.
8. Attribution: Maintain clear separation between code written by you and code from external sources (e.g. libraries or tutorials). Attribute any code from external sources to its source via comments above the code and (for larger dependencies) in the README.
9. Deployment: Deploy the final version of your code to a hosting platform such as Heroku.
10. Make sure to not include any passwords or secret keys in the project repository.


---


# Unit 3: Back End Development

Level:          5  
Credit value:   22  
GLH:            153  
Unit number:    D/650/3529  
Unit aim:       This unit aims to provide learners with the knowledge and skills needed to build a back end application. Topics covered include data storage and data management using relational databases.

This unit has 5 learning outcomes.


## Learning outcome 1

Design, develop, and implement a back end for a web application using [Python](https://www.python.org/) and a framework.


### Pass criteria

1. Design a front end for a data-driven web application which meets accessibility guidelines, follows the principles of UX design, meets its' given purpose, and provides a set of user interactions.
1. Implement custom HTML and CSS code to create a responsive full-stack application consisting of one or more HTML pages with relevant responses to user actions and a set of data manipulation functions.
1. Build a database-backed web application which allows users to store and manipulate data records about a particular domain.
1. Design a database structure which is relevant to the domain, including relationships between records of different entities.
1. Design and implement test procedures (automated or manual) to assess functionality, usability, responsiveness, and data management within the full stack web application.
1. Write [Python](https://www.python.org/) code which is consistent in style and conforms to the [PEP8](https://pep8.org/) style (or another explicitly mentioned style guide, such as [Google](https://google.github.io/styleguide/pyguide.html)s') and validated HTML and CSS code.
1. Write [Python](https://www.python.org/) logic to demonstrate profociency in the language.
1. Include functions with compound statements such as if conditions and/or loops in [Python](https://www.python.org/) code.
1. Write code which meets minimum standards for readablity (comments, indentation, consistent and meaningful naming conventions).
1. Name files consistently and descriptively, without spaces or capitalisation to allow for cross-platform compatibility.


### Merit criteria

1. Design a front end for a full stack application following the principles of UX design which meets accessibility guidelines, is easy to navigate, and allows the user to find information and resources intuitively.
1. Design a full stack application which lets the user initiate and control actions and gives immediate and full feedback on data processes.
1. Implement a full stack application whose purpose is immediately evident to a new user and which provides a good solution to the users' demands and expectations.
1. Create templates, writing code which demonstrates understanding of template syntax, logic, and usage.
1. Write robust code which is free of errors in all parts of the application.
1. Fully document the results of well-planned testing procedures (automated or manual) to assess the websites' functionality, usability, and responsiveness. Include evaluation of bugs found and their fixes and explanation of any bugs which are left unfixed.


## Learning outcome 2

Model and manage data.


### Pass criteria

1. Design a data model which fits the purpose of the project.
1. Develop the model into a usable relational database where data is stored in a consistent and well-organised manner.


### Merit criteria

1. Describe the data schema fully in the [README](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main#entity-relationship-diagrams) file.
1. Maintain database configuration in a single location where it can be changed easily.
1. Maintain a [Procfile](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/blob/main/procfile), [requirements.txt](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/blob/main/requirements.txt) file, [settings](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/blob/main/0_settings/settings.py) file.


## Learning outcome 3

Query and manipulate data.


### Pass criteria

1. Create functionality for users to create, locate, display, edit, and delete records.


### Merit criteria

1. Implement working Create, Read, Update, and Delete (CRUD).
1. Check that Create, Read, Update, and Delete (CRUD) actions are immediately reflected in the user interface.


## Learning outcome 4

Deploy a full stack web application to a cloud platform.


### Pass criteria

1. Deploy a final version of the full stack application code to a cloud-based hosting platform (e.g. [Heroku](https://www.heroku.com/)) and test to ensure it matches the development version.
1. Ensure that final deployed code is free of commented out code and has no broken internal links.
1. Document the deployment process in a [README](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main#how-to) file which also explains the applications' purpose and the value which it provides to its' users.


### Merit criteria

1. Commit often for each individual feature/fix, ensuring that commits are small, well-defined, and have clear descriptive messages.
1. Fully document the deployment procedure in a section in a [README](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main#how-to) file, written using consistent and effective markdown formatting which is well-structured, easy to follow, and has few grammatical errors.


## Learning outcome 5

Identify and apply security features.


### Pass criteria

1. Use [Git](https://git-scm.com/) and [GitHub](https://github.com/) for version control of a full stack web application up to deployment, using commit messages to document the development process.
1. Commit final code which is free of any passwords or secret keys, to the repository and to the hosting platform.
1. Use environment variables, or files which are in [gitignore](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/blob/main/.gitignore) to hide all secret keys.
1. Ensure that DEBUG mode is turned off in production versions.


### Merit criteria

1. Present a clear rationale for the development of the project, in the [README](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main#justification), demonstrating that it has a clear, well-defined purpose addressing the needs of a particular target audience (or multiple related audiences), explaining the data, and explaining the security features considered.


## Additional guidance for Merit

__To achieve mertit, learners need to meet the assessment criteria outlined above for a pass and a merit.__

__The following additional guidance describes characteristics of performance at MERIT.__

The learner has a clear rationale for the development of this project and has produced a fully functioning, well-documented, database backed, full stack application for a real life audience, with a full set of CRUD (creation, reading, updating, and deletion of data records) features. There are a range of features, including creation, location, deletion, and updating of data records. Data validation and user feedback are all evident in the code and the working application. Templates have been used to correctly produce working features. There are no logic errors in the code and the application functions as expected.

The finished project has a clear, well-defined purpose addressing the needs of a particular target audience (or multiple related audiences) and a particular data domain. Its' purpose would be immediately evident to a new ser without having to look at supporting documentation. The user is kept informed of progress and actions through feedback and, where large data sets are being uploaded, progress indicators. The design of the web application follows the principles of UX design and accessibility guidelines and the site is fully responsive.

Data is fully modelled and matches the schema. The schema design is documented in the [README](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main#entity-relationship-diagrams). Data store configuration is kept in a single location and can be changed easily. Configuration and [settings](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/blob/main/0_settings/settings.py) files are well-organised and there are different versions for different branches.

Code is well-organised and easy to follow and the application has been fully tested, following a manual testing procedure, with no obvious errors left in the code.

The development process is clearly evident through commit messages. The projects' documentation provides a clear rationale for the development of this project and covers all stages of the development life cycle.

The application is robust and deals with external errors gracefully (user input, API calls, asynchronous processes).


## Characteristics of performance at Distinction

To achieve a distinction, a learner will have achieved all pass and merit criteria, as described above, and will demonstrate characteristics of high level performance as described below:

The learner has documented a clear, justified, rationale for a real world application and a comprehensive explanation of how it will be developed. The development of the project has resulted in a fully-functioning, interactive, full stack application, with well-designed data and a full set of CRUD data operations. The learner shows a clear understanding of data modelling techniques and of the relationship between the back end and front end.

The finished project is judged to be publishable in its' current form with a professional grade user interface and functionality and interaction adhering to current practice. There are no logic errors in the code. Where there is a clear breach of accepted design/UX principles, or of accepted good practice in code organisation, these are fully justified, appropriate, and acceptable to the target user. It clearly matches the design and demonstrates the characteristics of craftsmanship in the code. The database schema is representative of complex user stories and there is a fully documented and full set of data operations which are fit for purpose in relation to the domain. The resulting application is original and not a copy of any walkthrough projects encountered in the unit.


### Amplifications & craftsmanship

#### Design

The design of the web application demonstrates the main principles of good UX design.


##### Information hierarchy

- Semantic markup is used to convey structure - all information displayed on the site is presented in an organised fashion with each piece of information being easy to find.
- All information displayed on the site is presented in an organised fashion with each piece of information being easy to find.
- All resources on the site are easy to find, allowing users to navigate the layout of the site intuitively.
- Information is presented and categorised in terms of its' priority.


##### User control

- All interaction with the site would be likely to produce a positive emotional response within the user. This is down to the flow of information layout, use of colour, clear and unamgiguous navigation structures and all interaction feedback.
- When displaying media files, the site avoids aggressive automatic pop-ups and autoplay of audio; instead letting the user initiate and control such actions.
- Users who direct to a non-existant page or resource are redirected back to the main page without having to use browser navigation buttons.
- Users are never asked for information which the application already has (e.g. a contact form does not ask a logged in user for an email address).
- The user is shown progress indicators and feedback on transactions.
- Errors resulting from user or data actions are reported to the user.


##### Consistency

- Evident across all pages/sections and covers interactivity as well as design.
- Consistency across all data operations, including in the reporting.


##### Confirmation

- User and data actions are confirmed where appropriate, feedback is given at all times.


##### Accessibility

- There is clear conformity to accessibility guidelines across all pages/sections and in all interactivity.


##### 
Any design decisions which contravene accepted user interaction, user experience design principles are identified and described (comments in code and/or a section in the [README](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main#design)).


#### Development and implementation

Code demonstrates characteristics of 'clean code'.


##### Consistent and appropriate naming conventions within code and in file naming, e.g.

- File names, class names, function names, and variable names are descriptive and consistent.
- For cross-platform compatability, file and directory names will not have spaces in them and will be lower-case only.
- All HTML attributes, CSS rules, code variables, and function names are consistent in format, follow standards for the language, and are appropriate and meaningful.
- App urls are consistent.


##### File structure

- Whenever relevant, files are grouped in directories by file type (e.g. an assets directory will contain all static files and code may be organised into sub-directories such as CSS, JavaScript, etc.).
- There is a clear separation between custom code and any external files (for example, library files are all inside a directory named `libraries`)
- Files are named consistently and descriptively, without spaces or capitalisation to allow for cross-platform compatability.


##### Readability

- Code is indented in a consistent manner to ease readability and there are no unnecessary repeated blank lines (and never more than 2).
- id / class (CSS and JavaScript) / function / variable names clearly indicate their purpose.
- All code is split into well-defined and commented sections.
- Semantic markup is used to structure HTML code.
- HTML, CSS, JavaScript, and [Python](https://www.python.org/) are kept in separate, linked files.
- CSS files are linked in the HTML files' `<head>` element.
- Non-trivial JavaScript code files are linked at the bottom of the `<body>` element (or bottom of `<head>` element if needs loaded before the `<body>` HTML).


##### Defensive design

- All input data is validated (e.g. presence check, format check, range check).
- Internal errors are handled gracefully, and users are notified of the problem where appropriate.


##### Comments

- All custom code files include clear and relevent comments explaining the purpose of code segments.


##### Compliant code

- HTML code passes through [the official W3C validator](https://validator.w3.org/) with no issues.
- CSS code passes through [the official (Jigsaw) validator](https://jigsaw.w3.org/css-validator/) with no issues.
- JavaScript code passes through a linter (e.g. [jshint.com](https://jshint.com/)) with no major issues.
- [Python](https://www.python.org/) code is consistent in style and conforms to the [PEP8](https://pep8.org/) style guide (or another explicitly mentioned style guide, such as [Google](https://google.github.io/styleguide/pyguide.html)s').


##### Robust code

- No logic errors are found when running code.
- Errors caused by user actions are handled.
- Where used, API calls which fail to execute or return data will be handled gracefully, with the site users notified in an obvious way.
- Inputs are validated when necessary.
- Navigating between pages via the back/forward buttons can never break the site. There are no broken links.
- User actions do not cause internal errors on the page or in the console.


#### The full design...
... is implemented providing __a good solution to the users' demands and expectations__ and __with consideration for security__.


##### __Real world application__

- Clearly understandable site-specific content is used rather than [_Lorem ipsum_](https://loremipsum.org) placeholder text.
- All links to external pages open in a separate tab when clicked.
- The final application is aligned to the [user stories](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/blob/main/0_documents/README/files/user_stories.md) presented at the start of the project.


##### Testing procedures are...
... comprehensive, with a good level of coverage, and have clearly been followed. All noticable errors have been corrected or documented.


##### __Framework conventions__ are followed and used correctly

Flask:
- Controllers.
- Models.
- Views.
- Configuration and settings files are well organised.


##### __Security features__ and practice are evidenced

- Passwords are secret keys are stored in environment variables or in files which are in [.gitignore](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/blob/main/.gitignore), and are never committed to the repository.
- Any functionality requiring login is available only to logged-in users.
- User permissions and levels of access are appropriate (e.g. a non-admin user would not be able to edit another users' post).


##### __Data__ is well structured

- Data is fully modelled and matches the schema.
- Data store configuration is kept in a single location where it can be changed easily.
- Data is well-structured.
- All CRUD functionality is present and working and actions are immediately reflected in the front end.


##### Configuration and dependencies...
... files are kept up to date. Separate versions/branches of these are commits where relevant. Data store configuration is kept in a single location and can be changed easily. The data store is not accessible to the regular user without going through the code.


##### All noticable errors have been corrected or documented

- Navigating betwen pages via the back/forward buttons can never break the site. There are no broken links.
- User actions do not cause internal errors on the page or in the console.


##### Version control software is used effectively

- All code is managed in [Git](https://git-scm.com/) with well-described commit messages.
- There is a separate, well-defined commit for each individual feature/fix.
- There are no very large commits which make it harder to understand the development process and could lead the assessor to suspect plagiarism.


##### The full application development process is documented

- The purpose of the application is clearly described in the [README](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main#justification).
- The projects' documentation describes the UX design work undertaken for this project and the reasoning behind it.
    - Wireframes
    - Mockups
    - Diagrams
    - Etc, created as part of the design process are included in the project.
- There is a clear separation between code written by the learner and code from external sources (e.g. libraries or tutorials). All code from external sources is attributed to its' source via comments above the code and (for larger dependencies) in the [README](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main#libraries).
- The data schema is clear, comprehensive, and easy to follow.
- The data schema is fully documented in the [README](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main#entity-relationship-diagrams) file.
- A manual testing procedure is fully documented either in the [README](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main#manual-testing) or a [separate file](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/blob/main/0_documents/README/files/tests/manual.md).
- The deployment procedure is fully documented in a section in the [README](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main#how-to) file.
- Clear, well-described, explanatory commit messages describe the development process.
- The [README](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/blob/main/README.md) is well-structured and easy to follow.
- The [README](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/blob/main/README.md) file is written in markdown and uses markdown formatting consistently and effectively.
- Project documentation and the applications' user interface have few errors in spelling and grammar. -->
