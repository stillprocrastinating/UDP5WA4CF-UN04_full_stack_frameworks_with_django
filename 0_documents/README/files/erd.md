<!-- # Entity Relationship Diagram


## Questions

|Key|Name|Type|
|-|-|-|
|PrimaryKey|id|CharField(20)|
|Slug|slug|AutoSlugField()|
||learning_objective|IntegerField(choices)|
||type|IntegerField(choices)|
||number|IntegerField()|
||question|TextField()|
|Not included in this version of the app|image|CloudinaryField('image')|
||sub_number|IntegerField()|
||sub_answer_number_individual|IntegerField()|
||sub_correct_answer_individual|IntegerField()|
|ForeignKey|author|User, related_name="question_author"|


## Tests

|Key|Name|Type|
|-|-|-|
|PrimaryKey|id|CharField(20)|
|Slug|slug|AutoSlugField()|
||date|DateField()|
||type|IntegerField(choices)|
||participant_number|IntegerField()|
|ForeignKey|tester|User, related_name="tester"|
|ForeignKey(ManyToMany)|t_questions|Question|


## Answers

|Key|Name|Type|
|-|-|-|
|PrimaryKey|id|AutoField()|
|ForeignKey|question_id|Question, related_name="question_answers"|
|ForeignKey|test_id|Test, related_name="test_answers"|
||answer1|IntegerField()|
||answer2|IntegerField()|
||answer3|IntegerField(blank=True)|
||answer4|IntegerField(blank=True)|
||answer5|IntegerField(blank=True)|

---
---

# Initial plans


## Entity relationship diagram

Master table columns:
- question_type
- answer_options
- correct_answer
- test_date
- test_type
- participant_number
- correct_choice_frequency
- incorrect_choice_frequency
- [calculation] correct_choice_percentage
- [calculation] incorrect_choice_percentage


### Tables

questions
- id
- learning_objective
- type
- answer_number
- correct_answer

tests
- id
- date
- type
- participant_number

~~participants~~ -\-> GDPR

answers
- id
- [FK] question_id
- [FK] test_id
- option
- correct_option_frequency
- incorrect_option_frequency

[CTE] flagging
- [questions] learning_objective
- [questions] type
- [answers] option
- [answers] correct_option_frequency
- [answers] incorrect_option_frequency
- [tests] participant_number
- [calculation] correct_option_percentage
- [calculation] incorrect_option_percentage
- [calculation] flag -->
