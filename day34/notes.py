# API endpoints, API parameters
# User interface inside a class
# type hints

# some of the text from API was formatted weird,
# for instance ' , these are called HTML entities
# to unescape: import html, then html.unescape()

# to use a type of argument, import its class
# (self, quiz: QuizBrain)
# - this gives a warning when passing arg

# "type hints" - we can suggest ourselves which type a var is
age: int
name: str
# IDE will warn it expects int
def police_check(age: int) -> bool:
    pass

# output is specified with an arrow

