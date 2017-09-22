---
layout: default
id: overview
---
{% include site-links.md %}

## Compiler: Practice First


### Overview


This course teaches compiler theory and engineering. You will study, in detail, core components of modern compilers, including: lexical analysis, parsing, abstract syntax tree construction, type checking, memory layout, intermediate representation, code generation, optimization, and garbage collection, etc.. Most importantly, you will study the interactions between theory and practice, and how to manage the complexity introduced by the interactions. 

This course is organized in three parts: lectures, paper readings, and labs. The lectures cover basic topics and familiarize you with the main concepts, and the paper readings familiarize you with the latest research progress in current literatures. The lab forces you to understand the concepts at a deep level, since you will build a working compiler from the ground up. After the lab you will understand the internals of a rather complex compiler and the compilation in general.

The compiler you will build, called Tiger, compiles a subset of the Java programming language, but in later part of this course, you will also have the chance to expand the compiler extensively. The major parts of the Tiger compiler are:

- Lexer and Parser
- Abstract Syntax Tree and Elaborator
- Code generators
- Garbage collector
- Optimizer
- Runtime and library

And there will be a final project in which you are encouraged to propose your own ideas and build them into your compiler. For each lab, we will provide skeleton code, but you will have to do all the hard work. You'll have design freedom for the details of some data structures and algorithms.