# JangLang Interpreter

This is a simple interpreter for a custom programming language called **JangLang**, written in Python. It supports basic input/output, variables, math, string manipulation, and more.

## How to Run

Uh, make sure you have Python installed.

## Language Overview

JangLang is a line-by-line interpreted language that uses human-readable syntax. It supports the following features:

    Variables (let)

    User input (input)

    Output to the screen (print)

    Basic math (+, *)

    Built-in functions: reverse, repeat

## Supported Keywords

| Instruction/Op | Description | Example |
| ------ | ------ | ------ |
| print | Print to console | Use print to display output: print total |
| input | prompt user for input | Use input to get values from the user: input "Prompt message" -> variableName |
| let | Declare and assign a variable | Use let to define variables: let total = a + b |
| + | Add two numbers |
| * | Multiply two numbers |
| reverse | Reverse a string | Use built-in fuctions like: let reversed = reverse name |
| repeat | Repeat a string N times | Use built-in fuctions like: let spam = repeat char 5 |
| -> | Assign input to a variable (after prompt) |  Use input to get values from the user: input "Prompt message" -> variableName |

- 
  


## Transpiler wip

python transpiler.py programs/reversestring.txt reverse.c


fix cat, multiply, repeater
