-----------------------------------------
# Contents

* [Books](#books)
  - [General Overview](#general-overview)
  - [Introductory](#introductory)
  - [Advanced](#advanced)
* [Papers](#papers)
* [Courses](#courses)
* [Tutorials](#tutorials)
* [Comipler related Tools](#compiler-related-tools)
  + [Powerful languages&compilers](#powerful-languages--compilers)
  + [Lex&Yacc](#lexyacc)
  + [Educational and Toy Projects](#educational-and-toy-projects)
  + [Automata](#automata)
  
-----------------------------------------
# Books

## General Overview

  * [Computer Systems: A Programmer’s Perspective, R. Bryant, D. O'Hallaron](https://www.amazon.com/dp/9332573905) - Comprehensive treatement of Computer Systems including Compilers, Interpreters and Runtimes.
  * [Elements of Computing Systems, N. Nisan, S. Schocken](https://www.amazon.com/dp/0262640686) - How to build a computer starting with Nand Logic Gates and then move to Machine Code, Assemblers, Compilers and Operating Systems.
  * [SICP, H. Abelson, G. Sussman](https://mitpress.mit.edu/sicp/full-text/book/book.html) - Structure and Interpretation of Computer Programs.
    + Other editions: [HTML5/EPUB version](https://sarabander.github.io/sicp/).

## Introductory

  * [Basics of Compiler Design, T. Mogensen](http://www.diku.dk/hjemmesider/ansatte/torbenm/Basics/) - Short and concise book on the basic concepts behind Compiler Design.
  * [Beautiful Racket, M. But­t­er­ick](http://beautifulracket.com) - How to make your own Programming Language with Racket.
  * [Build Your Own Lisp, D. Holden](http://www.buildyourownlisp.com) - Learn C and build your own Lisp programming language in 1000 lines of code.
  * [Compilers: Principles, Techniques, and Tools, A. Aho, M. Lam, R. Sethi, J. Ullman](https://www.amazon.com/dp/0321486811) - The infamous Dragons Book, a classic textbook on Compiler Construction.
  * [Crafting Interpreters, B. Nystrom](http://www.craftinginterpreters.com/) - Everything you need to learn to build an interpreted, full-featured, efficient scripting language.
    + [GitHub Repo](https://github.com/munificent/craftinginterpreters).
    + Discussions: [HN](https://news.ycombinator.com/item?id=13406081).
  * [Create Your Own Programming Language](http://createyourproglang.com/) - Very short book on building your own programming language with video tutorials and source code projects for 3 example programming languages.
    + Discussions: [HN](https://news.ycombinator.com/item?id=813133).
  * [Engineering a Compiler, K. Cooper, L. Torczon](https://www.amazon.com/dp/012088478X) - Modern comprehensive textbook on Compilers Construction. It covers SSA Form and recent research on Machine Code Generation.
  * [Essentials of Programming Languages, D. Friedman & M. Wand](https://www.amazon.com/dp/0262062798) - Fundamental concepts of programming languages with a focus on Semantics, Interpretation and CPS (Continuation Passing Style).
  * [Language Implementation Patterns, T. Parr](https://www.amazon.com/dp/193435645X) - Learn the patterns behind building programming languages and build an interpreter yourself, using ANTLR.
  * [Modern Compiler Implementation in ML, A. Appel](https://www.cs.princeton.edu/~appel/modern/ml/).
    + Other editions: [MCI in C](https://www.cs.princeton.edu/~appel/modern/c/), [MCI in Java](https://www.cs.princeton.edu/~appel/modern/java/).
  * [Programming Language Pragmatics, M. Scott](https://www.amazon.com/dp/0123745144).
  * [Programming Languages: Application and Interpretation, S. Krishnamurthi](http://cs.brown.edu/courses/cs173/2012/book/).
    + [PDF](http://cs.brown.edu/courses/cs173/2012/book/book.pdf).
  * [Programming Languages: Theory and Practice](http://people.cs.uchicago.edu/~blume/classes/aut2008/proglang/text/offline.pdf).
  * [Project Oberon, N. Wirth & J. Gutknecht](http://people.inf.ethz.ch/wirth/ProjectOberon1992.pdf).
    + Other editions: [2013 Edition](http://www.cs.cmu.edu/~fp/courses/15312-f04/handouts/).
  * [The BEAM Book](https://github.com/happi/theBeamBook) - Description of the ERTS (Erlang Runtime System) and the BEAM Virtual Machine.
  * [Virtual Machines, Smith and Nait](https://www.amazon.com/dp/1558609105).
  * [Virtual Machines, Iain Craig](https://www.amazon.com/dp/1852339691).
  * [Writing an Interpreter in Go, T. Ball](https://interpreterbook.com/).
  * [Writing Compilers and Interpreters: A Software Engineering Approach](https://www.amazon.com/dp/0470177071).
    + Other editions: [Writing Compilers and Interpreters: An Applied Approach Using C++](https://www.amazon.com/dp/0471113530), [Writing Compilers and Interpreters: An Applied Approach Using C](https://www.amazon.com/dp/0471555800).


## Advanced

  * [Advanced Compiler Design and Implementation, S. Muchnick](https://www.amazon.com/dp/1558603204).
  * [Advanced Topics in Types and Programming Languages, B. Pierce](https://www.amazon.com/dp/0262162288).
  * [A Retargetable C Compiler: Design and Implementation, D. Hanson](https://www.amazon.com/dp/0805316701).
  * [Building an Optimizing Compiler, B. Morgan](https://www.amazon.com/dp/155558179X).
  * [Compiling with Continuations, A. Appel](https://www.amazon.com/dp/052103311X).
  * [Design Concepts in Programming Languages, F. Turbak, D. Gifford, M. Sheldon](https://www.amazon.com/dp/0262201755) - also contains some introductory level material.
  * [Instruction Level Parallelism, A. Aiken, U. Banerjee, A. Kejariwal, A. Nicolau](https://www.amazon.com/dp/1489977953).
  * [Linkers and Loaders](https://www.amazon.com/dp/1558604960).
  * [Optimizing Compilers for Modern Architectures, R. Allen & K. Kennedy](https://www.amazon.com/dp/1558602860/).
  * [Parsing Techniques: A Practical Guide](https://www.amazon.com/dp/038720248X).
    + [1st Edition, PDF](https://dickgrune.com/Books/PTAPG_1st_Edition/).
  * [The Garbage Collection Handbook: The Art of Automatic Memory Management, R. Jones, A. Hosking, E. Moss](https://www.amazon.com/dp/1420082795).
  * [The Implemetation of Functional Programming Langauges, S. P. Jones](https://www.microsoft.com/en-us/research/wp-content/uploads/1987/01/slpj-book-1987-small.pdf).
  * [The SSA Book, Springer, Zadeck](http://ssabook.gforge.inria.fr/latest/book.pdf).
  * [Types and Programming Languages, B. Pierce](https://www.amazon.com/dp/0262162091).
  * [Warren's Abstract Machine - Prolog in Haskell, H. Aït-Kaci](https://mitpress.mit.edu/books/warrens-abstract-machine).

# Papers
## Papers on education, discussing， introduction, etc.
  * [A Brief History of JIT Compilation, J. Aycock](http://eecs.ucf.edu/~dcm/Teaching/COT4810-Spring2011/Literature/JustInTimeCompilation.pdf).
  * [A Flexible Prolog Interpreter in Python, C. Bolz & M. Leuschel](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.103.1886&rep=rep1&type=pdf).
  * [A Graph Higher-Order IR, R. Leißa, M. Koster & S. Hack](http://compilers.cs.uni-saarland.de/papers/lkh15_cgo.pdf).
  * [A Micro-Manual for LISP - Not the Whole Truth, J. McCarthy](https://www.uraimo.com/files/MicroManual-LISP.pdf).
    + Other editions: [Neat and nice typeset](https://github.com/jaseemabid/micromanual).
  * [A Prolog Interpreter in Python, C. Bolz](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.121.8625&rep=rep1&type=pdf).
  * [A Simple Multi-Processor Computer Based on Subleq, O. Mazonka, A. Kolodin](https://arxiv.org/abs/1106.2593).
  * [An Evil Copy: How the Loader Betrays You](http://www.cse.psu.edu/~trj1/papers/ndss17.pdf) - About security issues related to Dynamic Loading.
  * [An Incremental Approach to Compiler Construction](http://scheme2006.cs.uchicago.edu/11-ghuloum.pdf).
  * [Compiler Construction Using Scheme, E. Hilsdale, J. Ashley, R. Dybvig & D. Friedman](https://www.cs.indiana.edu/~dyb/pubs/fple95.pdf).
  * [Compiling with Continuations: Continued, A. Kennedy](https://www.microsoft.com/en-us/research/wp-content/uploads/2007/10/compilingwithcontinuationscontinued.pdf).
  * [Definitional Interpreters for Higher-Order Programming Languages, J. Reynolds](http://www.cs.uml.edu/~giam/91.531/Textbooks/definterp.pdf).
  * [Draining the Swamp: Micro Virtual Machines as Solid Foundation for Languauage Development, K. Wang, Y. Lin, S. Blackburn, M. Norrish & A. Hosking](http://drops.dagstuhl.de/opus/volltexte/2015/5034/pdf/24.pdf).
  * [Engineering Definitional Interpreters, J. Midtgaard, N. Ramsey, B. Larsen](https://www.cs.tufts.edu/~nr/pubs/interps.pdf).
  * [Garbage Collection in an Uncooperative Environment, H. Boehm, M. Weiser](https://pdfs.semanticscholar.org/6434/aa10f3745dcf959cfca9c379aae120396724.pdf?_ga=2.133026126.1710272003.1495044697-300816831.1495044697).
  * [Machine Code Obfuscation via Instruction Set Reduction and CFG Linearization, C. Jonischkeit](https://kirschju.re/static/ba_jonischkeit_2016.pdf).
  * [`MOV` is Turing-Complete, S. Dolan](https://www.cl.cam.ac.uk/~sd601/papers/mov.pdf).
    + Discussions: [HN](https://news.ycombinator.com/item?id=6309631), [Reddit](https://redd.it/1nft0x).
  * [Nanopass Framework for Commercial Compiler Development, A. Keep & R. Dybvig](https://www.cs.indiana.edu/~dyb/pubs/commercial-nanopass.pdf).
  * [Nanopass Framework for Compiler Education, D. Sarkar, O. Waddell & R. Dybvig](https://www.cs.indiana.edu/~dyb/pubs/nano-jfp.pdf).
  * [Notes on Graph Algorithms Used in Optimizing Compilers, C. Offner](http://www.cs.umb.edu/%7Eoffner/files/flow_graph.pdf).
  * [Packrat Parsing Thesis on PEG, B. Ford](https://pdos.csail.mit.edu/~baford/packrat/thesis/).
  * [PEG-based transformer provides front-end, middle-end and back-end stages in a simple Compiler, I. Piumarta](http://www.vpri.org/pdf/tr2010003_PEG.pdf).
  * [Pycket: A Tracing JIT for a Functional Language](http://homes.soic.indiana.edu/samth/pycket-draft.pdf).
  * [PyPy’s Approach to VM Construction, A. Rigo & S. Pedroni](http://www.csc.lsu.edu/~gb/csc7700/Reading/pypy-vm-construction.pdf).
  * [RABBIT: A Compiler for SCHEME, G. Steele](http://repository.readscheme.org/ftp/papers/ai-lab-pubs/AITR-474.pdf).
  * [Simple and Efficient Construction of SSA Form](http://compilers.cs.uni-saarland.de/projects/ssaconstr/).
  * [SSA-based Register Allocation, S. Hack & G. Goos](http://compilers.cs.uni-saarland.de/projects/ssara/).
  * [The Essence of Compiling with Continuations, C. Flanagan, A. Sabry, B. Duba & M. Felleisen](https://users.soe.ucsc.edu/~cormac/papers/pldi93.pdf).
  * [The Page-Faults Weird Machine: Lessons in Instruction-less Computation, J. Bangert, S. Bratus, R. Shapiro, S. Smith](https://www.usenix.org/system/files/conference/woot13/woot13-bangert.pdf).
  * [Trace-based JIT Compilation for Lazy Functional Languages, T. Schilling](http://files.catwell.info/misc/mirror/tracing-jit-haskell-schilling.pdf).
  * [Using Datalog with Binary Decision Diagrams for Program Analysis, J. Whaley, D. Avots, M. Carbin & M. Lam](https://people.csail.mit.edu/mcarbin/papers/aplas05.pdf).

# Courses
## Courses about Formal Languages and Automata Theory
- [CS162 in University of California, Irvine](http://www.ics.uci.edu/~goodrich/teach/cs162/)

## Courses about Compiler Principle
  * [Compilers Construction, Cambridge](http://www.cl.cam.ac.uk/teaching/1516/CompConstr/materials.html) - Introduction to compiler construction course from the University of Cambridge.
  * [Compiler Construction for Undergrads, RICE University](https://www.clear.rice.edu/comp412/Lectures/) - Introduction to compiler construction and language translators course from the RICE University.
  * Compilers Theory, Stanford - [YouTube](https://www.youtube.com/playlist?list=PLLH73N9cB21VSVEX1aSRlNTufaLK1dTAI), [Stanford.edu](https://lagunita.stanford.edu/courses/Engineering/Compilers/Fall2014/), [Class Notes](http://web.stanford.edu/class/cs143/) -Introduction to Compilers theory and construction course from Stanford.
  * [Design and Construction of Compilers, University of Texas](https://lambda.uta.edu/cse5317/) - Design and construction of compilers including lexical analysis, parsing, code generation techniques, error analysis and simple code optimizations.
    + Lecture Notes: [PDF](https://lambda.uta.edu/cse5317/notes.pdf), [HTML](https://lambda.uta.edu/cse5317/long/long.html).
  * [DSL Design and Implementation Summer School](http://vjovanov.github.io/dsldi-summer-school/) - Summer School program on the topics of DSL Design and Implementation hosted by the EPFL University.
  * [Foundations of Programming Languages](http://www.cs.cmu.edu/~fp/courses/15312-f04/) - Concepts that underlie the design, definition, implementation and use of modern programming languages from a formal standpoint.
  * [Nand2Tetris: How to Build a Computer from First Principles, Part 2](https://www.coursera.org/learn/nand2tetris2) - This 2nd part of the Nand2Tetris course covers basic language design and elementary compiler construction concepts in addition to many other topics on a basic level.
  * [NPTEL's Principles of Compiler Design Course](https://www.youtube.com/playlist?list=PLbMVogVj5nJQNjkHZgwuAlfQ9tzmQDxjA) - Introductory course from NPTEL on Compiler Design.
  * [NPTEL's Compiler Design Course](http://nptel.ac.in/courses/106108052/32) - Slightly more advanced course than their Principles of Compiler Design course, covers SSA Form to a good degree.
    + [YouTube Video Playlist](https://www.youtube.com/playlist?list=PLbMVogVj5nJTmKzaSlCpGgi7qxgcRRs8h).
  * [Programming Languages: Part A, by Grossman](https://www.coursera.org/learn/programming-languages) - Part 1 of a 3-part course series to the basic concepts of programming languages, with a strong emphasis on functional programming.
  * [Programming Languages: Part B, by Grossman](https://www.coursera.org/learn/programming-languages-part-b) - Part 2 of a 3-part course series to the basic concepts of programming languages, with a strong emphasis on functional programming.
  * [Programming Languages: Part C, by Grossman](https://www.coursera.org/learn/programming-languages-part-c) - Part 3 of a 3-part course series to the basic concepts of programming languages, with a strong emphasis on functional programming.
  * [Types, Logic, Semantics, and Verification from Oregon University's Summer School](https://www.cs.uoregon.edu/research/summerschool/summer15/curriculum.html) - Summer School program that consists of 80 minute lectures presented by internationally recognized leaders in programming languages and formal reasoning research.
  * [Virtual Machines and Managed Runtimes, UCB CS294](http://www.wolczko.com/CS294/) - Introductory course on Virtual Machines and Managed Runtimes from the University of Berkeley.
  * [Virtual Machines Summer School 2016 (VMSS 2016)](http://soft-dev.org/events/vmss16/) - VMSS is a Summer School program that aims to give an overview of the field, targeted at early career researchers.
    + [YouTube Videos Playlist](https://www.youtube.com/playlist?list=PLJq3XDLIJkib2h2fObomdFRZrQeJg4UIW).


# Tutorials

  * [A Tutorial Implementation of a Dependently Typed Lambda Calculus](https://www.andres-loeh.de/LambdaPi/).
  * [A Beginner's Guide to Linkers](http://www.lurklurk.org/linkers/linkers.html) - Tutorial for helping C & C++ programmers understand the essentials of what the linker does.
  * [Algorithm W Step By Step](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.65.7733&rep=rep1&type=pdf).
  * [Building a LISP from scratch with Swift](https://www.uraimo.com/2017/02/05/building-a-lisp-from-scratch-with-swift/).
  * [Compiler Optmization Tutorial](https://www.youtube.com/watch?v=SfV8aRX0YY0).
  * [Hindley-Damas-Milner Tutorial](https://github.com/quchen/articles/tree/master/hindley-milner) - Extensively documented walkthrough for typechecking a basic functional language using the Hindley-Damas-Milner algorithm.
  * [How I Wrote a Programming Language, and How You Can Too](https://medium.com/@william01110111/the-programming-language-pipeline-91d3f449c919).
    + Discussions: [Reddit](https://redd.it/62ixbc).
  * [Implementing a JIT Compiled Language with Haskell and LLVM](http://www.stephendiehl.com/llvm/).
  * [Kaleidoscope: Implementing a Language with LLVM in Objective Caml](http://llvm.org/docs/tutorial/index.html#kaleidoscope-implementing-a-language-with-llvm-in-objective-caml).
  * [Let’s Build A Simple Interpreter](https://ruslanspivak.com/lsbasi-part1/).
  * [Lisperator](http://lisperator.net/pltut/) - How to implement a programming language in JavaScript.
  * [Little Lisp Interpreter](https://maryrosecook.com/blog/post/little-lisp-interpreter) - Interpreter that supports function invocation, lambdas, lets, ifs, numbers, strings, a few library functions, and lists in under 120 lines of JavaScript.
    + [GitHub Repository](https://github.com/maryrosecook/littlelisp).
  * [`lis.py`, v1: (How to Write a (Lisp) Interpreter (in Python))](http://norvig.com/lispy.html) - Tutorial by Peter Norvig on writing a simple Lisp interpreter.
  * [`lis.py`, v2: An ((Even Better) Lisp) Interpreter (in Python)](http://norvig.com/lispy2.html) - Follow-up tutorial by Peter Norvig on making `lis.py` slightly better.
  * [LLVM Tutorial: Implementing Kaleidoscope](http://releases.llvm.org/3.6.2/docs/tutorial/LangImpl1.html).
    + [Python version with LLVMPY](http://www.llvmpy.org/llvmpy-doc/dev/doc/kaleidoscope/index.html).
  * [Metacompiler Tutorial, Part 1](http://www.bayfronttechnologies.com/mc_tutorial.html).
  * [Project: A Programming Language](http://eloquentjavascript.net/11_language.html) - Chapter 11 from the book _Eloquent JavaScript_, 2nd Edition.
  * [Write You a Haskell](http://dev.stephendiehl.com/fun/).
  * [Writing a Language in Truffel](http://cesquivias.github.io/tags/truffle.html) - Interpreter development tutorial using Truffel, by Cristian Esquivias.
  
# Compiler Related Tools

## Powerful Languages & Compilers
- [GCC, the GNU Compiler Collection](http://gcc.gnu.org/)
- [The LLVM Compiler Infrastructure](http://llvm.org/)
- [Rust a systems programming language wants to replace C/C++](https://www.rust-lang.org/en-US/)
- [Python is a programming language that lets you work quickly](https://www.python.org/)
- [OpenJDK is the open-source implementation of the Java](http://openjdk.java.net/)
- [kotlin - a language which is 100% interoperable with Java Android](https://kotlinlang.org/)

## LEX/YACC
- [Python Lex-Yacc](http://www.dabeaz.com/ply/)
- [ANTLR (ANother Tool for Language Recognition)--a powerful parser generator](http://www.antlr.org/)
- [JFlex is a lexical analyzer generator written in Java](http://jflex.de/)
- [byaccj is a parser generator written in Java](byaccj.sourceforge.net)

## Educational and Toy Projects
  * [C4](https://github.com/rswier/c4) - mini C Language Compiler in 4 Functions.
  * [8cc](https://github.com/rui314/8cc) - C Compiler supporting all C11 language features
  * [Black](http://www.is.ocha.ac.jp/~asai/Black/) - Scheme interpreter for the Reflective Programming Language "Black", by Kenichi Asai's.
    + Other sources: [GitHub Mirror](https://github.com/readevalprintlove/black).
    + Discussions: [HN](https://news.ycombinator.com/item?id=8558822).
  * [CarpVM](https://github.com/tekknolagi/carp) - Experimental VM implementation in C.
  * [Charly](https://github.com/charly-lang/charly) - Interpreter for a dynamically typed language written in Crystal.
  * [Dale](https://github.com/tomhrr/dale) - Lisp-flavoured C: a system programming language.
  * [Eschelle](https://github.com/Eschelle/Eschelle) - Open source cross platform multi-paradigm language with VM & JIT
  * [Gecho](https://github.com/tekknolagi/gecho) - Simple-stack language implementation in C.
  * [gocaml](https://github.com/rhysd/gocaml) - Minimal functional programming language implementation in Go and LLVM.
  * [Hython](https://github.com/mattgreen/hython) - Haskell-powered Python 3 interpreter.
    + Discussions: [Reddit](https://redd.it/46f8j4).
  * [llgo](https://github.com/llvm-mirror/llgo) - Go frontend for LLVM written in Go.
  * [Mal's Interpreter](https://github.com/kanaka/mal) - Clojure-inspired Lisp interpreter implemented in 64 languages.
  * [MetaScala](https://github.com/lihaoyi/Metascala) - Metacircular JVM implementation in Scala.
  * [mini-js](https://github.com/maierfelix/mini-js) - Experimental self-hosted JavaScript compiler in 1K LoC.
  * [MunVM](https://github.com/MunVM/MunVM) - Lua VM & Compiler in C.
  * [MY-BASIC](https://github.com/paladin-t/my_basic) - An embeddable BASIC dialect interpreter in C with modern paradigms.
  * [Poprc](https://github.com/HackerFoo/poprc) - Compiler for the Popr Language.
  * [PyCOOLC](https://github.com/aalhour/PyCOOLC) - Compiler for the COOL Programming Language written in Python 3.
  * [RabbitVM](https://github.com/rabbitvm/rabbit) - RISC-based VM implementation in C.
  * [stack_cpu](https://github.com/dsturnbull/stack_cpu) - Stack-machine simulator.
  * [The Super Tiny Compiler](https://github.com/thejameskyle/the-super-tiny-compiler) - Tiny educational compiler project in JavaScript.
    + Discussions: [HN](https://news.ycombinator.com/item?id=11395656).
  * [tinyc.c](http://www.iro.umontreal.ca/~felipe/IFT2030-Automne2002/Complements/tinyc.c) - Tiny-C language compiler in C.
  * [tisp](https://github.com/raviqqe/tisp) - "Time is Space" Programming Language Interpreter.

## Automata
