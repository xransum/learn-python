# Introduction to Programming

## Overview

**Note:** If you are familiarized with this section already, then you can skip it.

This section may seem a bit overwhelming and that's fine, it's a lot of information that might not entirely click until a little later down the road. However, even though it's being included, it's not entirely required. The information is very good to know to gather a better understanding of what it is you're doing.

Here you will learn the fundamental blocks of what programming is, its origin, and the different types.

## Table of Contents

- [Introduction to Programming](#introduction-to-programming)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [The Beginning of Computers](#the-beginning-of-computers)
  - [Introducing the Central Processing Unit](#introducing-the-central-processing-unit)
  - [The Birth of Programming Languages](#the-birth-of-programming-languages)
  - [The Types of Programming Languages](#the-types-of-programming-languages)
  - [Hierarchy of Programming Language Types](#hierarchy-of-programming-language-types)
  - [Language Compilation Process](#language-compilation-process)
  - [Language Execution Methods](#language-execution-methods)

## The Beginning of Computers

Before the advent of electronic computers, the term "computer" was used to describe human mathematicians and scientists who meticulously performed extensive mathematical calculations. These "human computers" were indispensable for tasks in fields like astronomy, engineering, and physics, where precision and accuracy were paramount. They manually computed complex equations and generated mathematical tables that were vital for scientific and navigational advancements.

The evolution of the first electronic computers marked a transformative moment in computing history. Early electronic machines like the ENIAC and the Colossus were developed during World War II to automate complex calculations and codebreaking, respectively. These early computers were massive, room-filling devices that significantly sped up computations. As technology progressed, there came the introduction of the Central Processing Unit.

## Introducing the Central Processing Unit

The Central Processing Unit (CPU) has one prime objective, similar to a conductor in an orchestra. It orchestrates the intricate dance of data within a computer system. Just like a conductor meticulously guides each musician's performance to create a harmonious symphony, to a CPU the musician's would be the hardware components, the CPU coordinates the execution of instructions, ensuring the computer's various components work in harmony to accomplish tasks.

The CPU is often likened to the "brain" of the computer, and for good reason. Much like the human brain processes and interprets information from our senses, the CPU interprets instructions written in programming languages and translates them into a series of electrical signals and binary operations. With relation to the symphony, this process is similar to translating a complex novel into a sequence of musical notes and cues for a symphony.

As technology advanced further, CPUs became faster and more powerful, enabling the execution of increasingly complex tasks. They became the driving force behind the digital revolution, powering everything from scientific simulations and video games to the operation of our everyday devices, seamlessly translating human intentions into computer actions. The evolution of CPUs was fundamental in transforming computers from room-sized calculating machines into the compact, high-speed devices we rely on today.

## The Birth of Programming Languages

In the early days of programming, instructing computers resembled the ancient quest to discover the secret of making fire. Early programmers grappled with the fundamental components of computing, represented by the raw binary code of 0s and 1s. This primitive binary code was akin to the basic materials required for starting a fire.

Just as the earliest fire-making was a series of primal gestures and grunts, manually typing out endless strings of 0s and 1s soon proved impractical and laborious. It was akin to repeating the same primitive actions every time one needed to create fire. This challenge gave rise to the development of the three fundamental programming languages: **High-level language**, **Low-level language**, and **Machine language**.

## The Types of Programming Languages

Before delving into the hierarchy and compilation of programming languages, it's essential to understand the origins and the fundamental principles that underpin this complex landscape. Programming languages are the means by which humans communicate their instructions to computers, and this journey started with the most basic form of communication, much like the early quest to make fire from primal gestures.

1. **Binary (Primitive Actions)**: In the realm of binary, computers communicated using the most primitive actions, much like early humans' gestures for fire-making. Binary represents the rawest form of instructions, mirroring the instinctual movements involved in kindling fire.

2. **Machine Language (Symbolic Drawings)**: Machine language, the next stage of complexity, can be likened to sharing the knowledge of fire-making through symbolic drawings. The CPU interprets specific sequences of binary as if it's decoding symbolic representations of the fire-making process. This represents a significant leap toward conveying complexity while maintaining a direct connection to the machine, similar to transitioning from gestures to symbolic drawings in the context of fire-making.

3. **Assembly Language (Written Instructions)**: Assembly language resembles a set of written instructions for fire-making. It's as if early humans discovered writing and employed simple characters to convey the process of creating fire. In the computing realm, assembly language uses mnemonic codes and symbols to make instructions more readable, much like the act of documenting the steps for making fire.

4. **High-level Language (Descriptive Speech)**: High-level languages are comparable to a well-composed narrative describing the fire-making process. Just as human language evolved to express intricate ideas, high-level languages provide a rich vocabulary of words and phrases to articulate complex tasks. The CPU interprets these descriptions as a series of intricate instructions, similar to the transition from simple gestures to crafting a well-composed narrative in the context of fire-making. The CPU becomes a master of the language, translating human-friendly expressions into intricate operations.

## Hierarchy of Programming Language Types

Programming languages exist on a spectrum, ranging from those that are closest to human understanding and expression to those that are most directly understood by the computer's central processing unit (CPU). This hierarchy helps us understand the varying levels of abstraction and complexity in the programming world, and it plays a crucial role in how we create and communicate instructions to computers.

1. **High-Level Languages**: These are the most human-readable and abstract programming languages, aligning closely with the natural way we express tasks. Notable examples include Python, Java, C++, and numerous others.

2. **Assembly Language**: Assembly language serves as a low-level programming language offering a symbolic representation of machine code instructions. It occupies an intermediary position between high-level languages and machine code, with different computer architectures having their specific assembly languages (e.g., x86 Assembly, ARM Assembly).

3. **Low-Level Languages**:
   - **Machine Code / Binary Code**: This stands as the lowest-level programming language, comprising binary instructions directly comprehensible by the CPU. It lacks human readability and represents the most elemental form of programming language.
   - **Assembly Code**: Assembly code is the specific code written by programmers using assembly language. It still falls under the category of low-level language but is more human-readable than machine code.

## Language Compilation Process

To bring our programming concepts to life in the realm of machines, we need a bridge between human-readable code and the binary instructions that computers can execute. This is where the compilation process comes into play, acting as a transformative step that takes our high-level or assembly code and converts it into the language of the machine, making it executable by the CPU.

- High-Level Languages can be directly compiled or interpreted into machine code, bypassing assembly.
- Assembly Language is often assembled directly into machine code, negating the need for an intermediary low-level language.
- High-Level Languages can pass through assembly language, but they typically don't regress to high-level or low-level languages. Instead, they transition to machine code, which the CPU executes.

## Language Execution Methods

Understanding how different programming languages are executed is fundamental. Whether through compilation or interpretation, the choice of execution method has profound implications on how our code operates. This topic delves into the various strategies used to run programs, shedding light on the distinct characteristics and trade-offs between these methods.

- **Compiled Languages**: These languages necessitate a compiler to transform human-readable source code into machine code or an intermediate code. Notable examples of compiled languages encompass C, C++, and Rust. The compiler generates a binary executable file for execution on the target platform.

- **Interpreted Languages**: Interpreted languages dispense with compilation, relying instead on an interpreter to read the source code and execute it directly. Prominent examples of interpreted languages encompass Python, JavaScript, and Ruby. These languages commonly employ interpreters to execute code line by line.

- **Hybrid Languages**: Certain languages blend elements of both compilation and interpretation. For instance, Java undergoes initial compilation into intermediate bytecode, which is subsequently interpreted by the Java Virtual Machine (JVM). Similarly, C# code is compiled into Common Intermediate Language (CIL) code, executed by the Common Language Runtime (CLR).

- **Just-in-Time (JIT) Compilation**: Some languages, such as Java and C#, employ JIT compilation. They first compile code into bytecode or intermediate code, with the bytecode subsequently converted into native machine code just before execution. This approach combines aspects of both compilation and interpretation.

- **Scripting Languages**: Scripting languages, like Perl and PHP, often lean toward interpretation. They find application in specific tasks like process automation and web development. However, certain scripting languages can also be used in conjunction with compilers, depending on the specific use case.

[Next: Getting Started with Python](./02-introduction-to-python.md)
