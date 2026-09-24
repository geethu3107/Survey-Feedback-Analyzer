# Survey Feedback Analyzer

A Python-based text analysis project that processes survey feedback stored in a dictionary of lists. The project demonstrates core Python programming concepts including loops, conditionals, string manipulation, functions, sets, and basic data analysis.

## Project Overview

The **Survey Feedback Analyzer** allows users to add survey feedback, clean textual responses, and extract simple insights from the collected data.

The project starts with 10 preloaded feedback entries and allows the user to add additional feedback interactively.

## Features

* Stores survey data using a dictionary of lists
* Allows users to add new feedback entries
* Automatically generates serial numbers for new entries
* Collects:

  * Name
  * Written feedback
  * Rating from 1–5
* Cleans feedback text by:

  * Removing `.`, `,`, `!`, and `?`
  * Removing extra spaces
  * Removing leading and trailing spaces
  * Converting text to lowercase
* Counts the number of feedbacks containing specific words
* Calculates the average rating
* Identifies the longest feedback based on word count
* Extracts unique words used across all feedback
* Optionally sorts feedback entries by rating from highest to lowest

## Python Concepts Used

* Dictionary of lists
* Lists
* Loops
* Conditional statements
* User input
* String methods
* `.replace()`
* `.split()`
* `' '.join()`
* `.lower()`
* Sets
* User-defined functions
* `zip()`
* `sorted()`
* Lambda functions

## Word Count Analysis

The project includes a function:

```python
count_word_in_feedbacks(word)
```

It performs a case-insensitive search and returns the number of feedback entries containing the specified word.

The function is used to analyze:

* `good`
* `poor`
* `excellent`

## Sample Insights

The program produces:

* Final cleaned feedback data
* Average rating
* Longest feedback and its word count
* Unique words across all feedback
* Feedback entries sorted by rating

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/geethu3107/Survey-Feedback-Analyzer.git
```

### 2. Navigate to the project folder

```bash
cd Survey-Feedback-Analyzer
```

### 3. Run the Python program

```bash
python survey_feedback_analyzer.py
```

## Input Example

The program asks:

```text
How many more feedbacks you want to add: 2
Enter name: Arun
Your feedback here: Very good service
Your rating pls: 5
```

The entered feedback is appended to the existing survey data and processed along with the preloaded feedback.

## Project Objective

This project was developed as a practical exercise to strengthen Python programming fundamentals and understand the basic workflow of collecting, cleaning, and analyzing textual data.
