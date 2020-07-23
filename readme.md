# Behave Python project

This demonstrate how you can stand up a Behavior-Driven Development or BDD
project with Python 3.

## To run:
```shell script
behave --snippets features/google_search.feature 
behave  features/google_search.feature 
```

├── behave.ini
├── features
│   ├── environment.py
│   ├── google_search.feature
│   └── steps
│       └── google_search_steps.py
├── plain.output
└── readme.md
