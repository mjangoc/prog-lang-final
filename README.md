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

| Instruction/Op | Description |
| ------ | ------ |
| print | Print to console |
| input | prompt user for input |
| let | Declare and assign a variable |
| + | Add two numbers |
| * | Multiply two numbers |
| reverse | Reverse a string |
| repeat | Repeat a string N times |
| -> | Assign input to a variable (after prompt) |


## Writing Your Own Programs

Each line should use one of the supported commands:
- Use input to get values from the user:
  
   input "Prompt message" -> variableName
  
- Use let to define variables:
  
   let total = a + b
  
- Use print to display output:
  
   print total
  
- Use built-in fuctions like:
  
   let reversed = reverse name
  
   let spam = repeat char 5

## Transpiler wip

python transpiler.py programs/reversestring.txt reverse.c


fix cat, multiply, repeater
