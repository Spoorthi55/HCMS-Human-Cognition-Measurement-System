# questions.py
# HCMS V1.1 — Research-Valid Question Bank

QUESTIONS = [
    # ======================
    # VARIABLES
    # ======================
    {
        "id": "VAR_1",
        "concept": "Variables",
        "difficulty": "easy",
        "question": "x = 5\nx = x + 3\nprint(x)",
        "answer": "8",
        "misconceptions": ["value does not change"]
    },
    {
        "id": "VAR_2",
        "concept": "Variables",
        "difficulty": "easy",
        "question": "x = 4\nx = 2\nprint(x)",
        "answer": "2",
        "misconceptions": ["first assignment matters"]
    },
    {
        "id": "VAR_3",
        "concept": "Variables",
        "difficulty": "medium",
        "question": "a = 10\nb = a\na = 5\nprint(b)",
        "answer": "10",
        "misconceptions": ["variables stay linked"]
    },
    {
        "id": "VAR_4",
        "concept": "Variables",
        "difficulty": "medium",
        "question": "x = 1\nx = x + x\nprint(x)",
        "answer": "2",
        "misconceptions": ["double increment confusion"]
    },
    {
        "id": "VAR_5",
        "concept": "Variables",
        "difficulty": "hard",
        "question": "x = 3\ny = x + 2\nx = 10\nprint(y)",
        "answer": "5",
        "misconceptions": ["retroactive value change"]
    },

    # ======================
    # CONDITIONALS
    # ======================
    {
        "id": "COND_1",
        "concept": "Conditionals",
        "difficulty": "easy",
        "question": "x = 10\nif x > 5:\n    print('A')\nelse:\n    print('B')",
        "answer": "A",
        "misconceptions": ["condition ignored"]
    },
    {
        "id": "COND_2",
        "concept": "Conditionals",
        "difficulty": "easy",
        "question": "x = 3\nif x > 5:\n    print('A')\nelse:\n    print('B')",
        "answer": "B",
        "misconceptions": ["else misunderstood"]
    },
    {
        "id": "COND_3",
        "concept": "Conditionals",
        "difficulty": "medium",
        "question": "x = 5\nif x >= 5:\n    print('A')\nelse:\n    print('B')",
        "answer": "A",
        "misconceptions": ["greater vs greater-equal"]
    },
    {
        "id": "COND_4",
        "concept": "Conditionals",
        "difficulty": "medium",
        "question": "x = 0\nif x:\n    print('A')\nelse:\n    print('B')",
        "answer": "B",
        "misconceptions": ["truthiness misunderstanding"]
    },
    {
        "id": "COND_5",
        "concept": "Conditionals",
        "difficulty": "hard",
        "question": "x = -1\nif x > 0:\n    print('A')\nelif x == 0:\n    print('B')\nelse:\n    print('C')",
        "answer": "C",
        "misconceptions": ["elif logic confusion"]
    }
]
