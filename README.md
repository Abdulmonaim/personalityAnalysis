# Personality Analysis Project 2018

This project is my first Python program, developed to assist in analyzing personalities based on user input. As a part of an educational initiative with my 14-year-old students, we embarked on this journey to learn Python programming, utilizing the Qt framework for the graphical user interface.

## Features

### 1. Password Validation

The project includes a function `password_validation` to validate the strength of user passwords. It checks for the presence of lowercase letters, uppercase letters, digits, and special characters ('@', '$', '_'). The password must be at least 8 characters long and meet all criteria for successful validation.

### 2. Email Validation

The `email_validation` function uses the `email_validator` library to validate the format of user-provided email addresses. It returns the validated email address or an error message in case of invalid emails.

### 3. Questionnaire and Classification

The `classified_answers` function provides a set of predefined answers categorized into Extroversion/Introversion, Sensing/Intuition, Thinking/Feeling, and Judging/Perceiving traits. Users answer a set of questions, and their responses are used to determine their personality type.

### 4. User Signup

The `signup` function allows users to sign up by providing their name, email, password, and answers to the personality questionnaire. The collected data is stored in a file named `user_data.txt`.

### 5. Personality Analysis

The `analysis` function analyzes user responses and determines their personality type based on trait probabilities.

### 6. Result Email Notification

The `email_result` function sends an email to the user with their personality analysis results, including an introduction to their personality type, strengths, weaknesses, suggested career paths, and tips for personal growth.

### 7. Additional Functions

- `lin`: Extracts lines from a file based on the question number.
- `read`: Reads questions from multiple files based on the question number.
- `append_letters`: Combines the analyzed personality traits into a single string.
- `get_personality_traits`: Retrieves information about personality traits, career suggestions, and tips from corresponding files.
