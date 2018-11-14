# Stemmer

This project is a dictionary lookup that will return Chinese translations and part-of-speech tags for English queries. The program also incorporates a rule-based stemmer so that results for words with grammatical suffixes are also be returned. For example, a search query of 'studying' will additionally return results for 'study'.

## Requirements

* Python version: 3.5.1

## Start Developing

After cloning the repository:

* Setting up the environment：
    - `cd nlp-first`
    - Create a virtual environmnet: `python3 -m venv virtual-environment`
    - `cd virtual-environment/bin`
    - Enter `source activate` to start the virtual environment
    - `cd ../..` (to return to the `nlp-first` folder)
    - Install the project dependencies：`pip install –r requirements.txt`

* Start the program:
    - Ensure that you are inside `nlp-first` and that your virtual environment is running
    - Enter `python __main__.py`
    - Following the prompt in the terminal, enter an English word. The program will then output the results.
    - To stop the program, enter `1`.
    - Deactivate your virtual environment by entering `deactivate`
