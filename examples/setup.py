from ganttouchthis import Date, Gantt, Priority, Project, Task

g = Gantt()
g.add_project(
    name="Python лучшие инструменты и практики",
    tasks="17,A",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=3,
)
g.add_project(
    name="Python Programming with Design Patterns",
    tasks="13",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Об'єктно-орієнтоване програмування",
    tasks="18,A",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Udemy C++ Masterclass",
    tasks="699",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Cogneethi -  Evolution Of Object Detection Networks",
    tasks="134",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="How to use C from Python? - #9",
    tasks="1",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Mastering Python Design Patterns.pdf",
    tasks="16",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Design Patterns in Python.pdf",
    tasks="8",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="NLP Wikipedia",
    tasks="105",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Как устроен Python. Гид для разработчиков, программистов и интересующихся [2019] Харрисон",
    tasks="27,B",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Advanced Guide to Python 3 Programming",
    tasks="41",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Gemalte Wörter",
    tasks="214",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="14",
    tasks="Open Data Structures.pdf",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Bash Pocket Reference. Help for Power Users and Sys Admins.pdf",
    tasks="18",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Advanced Python Programming.pdf",
    tasks="23",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Cherno C++ Playlist",
    tasks="100",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="C++. Das umfassende Handbuch",
    tasks="31,A",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Programming Principles and Practice Using C++",
    tasks="17",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Foundations of Programming Languages.pdf",
    tasks="9",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Python Developer’s Guide",
    tasks="20",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Learn Computer Vision Using OpenCV. With Deep Learning CNNs and RNNs",
    tasks="6",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Linguae per carmina",
    tasks="300",
    priority=Priority.MEDIUM,
    groups={"Language Study"},
    start=Date.today() + 3,
    interval=3,
)
g.add_project(
    name="Everything You Need to Ace Computer Science and Coding.pdf",
    tasks="39",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="NLP01) Speech and Language Processing (2023).pdf",
    tasks="26,C",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="NLP02) Speech and Language Processing (2008).djvu",
    tasks="25",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Python/C API",
    tasks="96",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Cómo piensa el mundo: Una historia global de la filosofía",
    tasks="28",
    priority=Priority.MEDIUM,
    groups={"Philosophy"},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Interactive Object-Oriented Programming with Java.pdf",
    tasks="16,C",
    priority=Priority.MEDIUM,
    groups={"Java"},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Core Java SE 9 for the Impatient.pdf",
    tasks="15",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="https://exercism.org/tracks/java",
    tasks="129",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Think Java (2e).pdf",
    tasks="17,D",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Java для всех.pdf",
    tasks="13,B",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="LingoDeer",
    tasks="44",
    priority=Priority.MEDIUM,
    groups={"Language Study"},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Fusha to Shami",
    tasks="33",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="https://uk.wikipedia.org/wiki/Обробка_природної_мови",
    tasks="1",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="NLP04) Deep Learning for NLP and Speech Recognition",
    tasks="13,L",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Sams Teach Yourself Java in 24 Hours.pdf",
    tasks="24,E",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Fundamentals of Java Programming.pdf",
    tasks="19",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Grundkurs Java",
    tasks="33,D",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Java Succinctly Part 1.pdf",
    tasks="9,A",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Neural Network Programming with Java.pdf",
    tasks="9,B",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Core Java Cheatsheet.pdf",
    tasks="1",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Learning Java.pdf",
    tasks="13,B",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Програмування на Java",
    tasks="87",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Head First Java.pdf",
    tasks="9,A",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Легкий способ выучить Java.pdf",
    tasks="11,A",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Hands-On Software Engineering with Java.pdf",
    tasks="15",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Introduction to Digital Electronics",
    tasks="12",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="NLP03) NLP (Eisenstein)",
    tasks="19,B",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="The Computer Science of TeX and LaTeX.pdf",
    tasks="7",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Transfer Learning for Natural Language Processing.pdf",
    tasks="11,B",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Code and Data for the Social Sciences. A Practitioner's Guide.pdf",
    tasks="8,A",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="The Healthy Programmer",
    tasks="12,A2",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="A Programmer's Guide to Computer Science. Volume I.pdf",
    tasks="14,B",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Julia Docs",
    tasks="108",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="How Software Works",
    tasks="9",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Clean Code in Python.pdf",
    tasks="10",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="NLP09) NLP and CL II (Kurdi)",
    tasks="4",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="NLP07) Advanced Natural Language Processing with TensorFlow 2.pdf",
    tasks="16",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Дискретная математика для программистов.pdf",
    tasks="9",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="NLP18) Taming Text.pdf",
    tasks="9",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="https://www.gnu.org/software/bash/manual/",
    tasks="14",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="NLP13) Practical Natural Language Processing.pdf",
    tasks="11",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Willensfreiheit",
    tasks="8",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Das Handwerk der Freiheit",
    tasks="11,A",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Elementary Math for Computer Science with Python.pdf",
    tasks="8,A",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="C and Python Applications.pdf",
    tasks="6,A",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Python. The True Book.pdf",
    tasks="8",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Python Concurrency with asyncio.pdf",
    tasks="14",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Профессиональная разработка на Python.pdf",
    tasks="12",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Introduction to Programming in Python. An Interdisciplinary Approach.pdf",
    tasks="4,B",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="CPython Internals.pdf",
    tasks="17",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Изучаем Python, том 2.pdf",
    tasks="26-41,D",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="A functional start to computing with Python.pdf",
    tasks="32",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Effective Python.pdf",
    tasks="10",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Fluent Python (2e).pdf",
    tasks="24",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Fluent Python (2015).pdf",
    tasks="21,B",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Python Fluente (2015).pdf",
    tasks="21,B",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Functional Programming in Python.pdf",
    tasks="4",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Секреты Python Pro.pdf",
    tasks="11,A",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Inside the Python Virtual Machine.pdf",
    tasks="12",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Чистый Python.pdf",
    tasks="9",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Путь Python.pdf",
    tasks="13",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Learn More Python 3 the Hard Way.pdf",
    tasks="0-52",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Learn Python 3 the Hard Way",
    tasks="0-52,B",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Advanced Python Development.pdf",
    tasks="12",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Python. Сборник упражнений.pdf",
    tasks="16",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Exploring CPython's Internals - Python Developer's Guide",
    tasks="10",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Three Keys to Leveling up Your Python.pdf",
    tasks="3",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Простой Python (2021).pdf",
    tasks="22,A5",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Python. Das umfassende Handbuch",
    tasks="40,A",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Learn Python Programing.pdf",
    tasks="15",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Основы Python (2021).pdf",
    tasks="21,A",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Машинное обучение без лишних слов.pdf",
    tasks="11",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Dual Numbers",
    tasks="1",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)  # https://www.youtube.com/watch?v=ceaNqdHdqtg
g.add_project(
    name="Python Glossary",
    tasks="1",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="HOG paper",
    tasks="1",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Detecting Faces (Viola Jones Algorithm) - Computerphile",
    tasks="1",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="ML Algorithms.jpg",
    tasks="1",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Git Cheat Sheet",
    tasks="1",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Page Segmentation for Historical Handwritten Documents Using Fully Convolutional Networks.pdf",
    tasks="1",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="https://uk.wikipedia.org/wiki/Інформатика#Штучний_інтелект",
    tasks="1",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="The Gospel of John in Greek and Latin",
    tasks="21",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="40 Algorithms Every Programmer Should Know (Python).pdf",
    tasks="40",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Modern C for Absolute Beginners",
    tasks="47,E",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Algorithmic Thinking. A Problem Based Introduction.pdf",
    tasks="8,C",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Beginning C++17.pdf",
    tasks="0-19",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Beginning C++20.pdf",
    tasks="0-21",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="100 примеров на Си.djvu",
    tasks="100",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="C Programming for Dummies.pdf",
    tasks="7",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Schrödinger programmiert C++",
    tasks="18",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="C Programming. A Self-Teaching Introduction.pdf",
    tasks="5,E",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Data Structures and Algorithms in Cpp.pdf",
    tasks="14,A",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="https://www.learncpp.com/",
    tasks="23,C",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Here's An Easier Way to Understand Pointer Math in C/C++ Programming - YouTube",
    tasks="1",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="The Linux Command Line",
    tasks="36",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="C++ на примерах.pdf",
    tasks="14,A",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Cpp for Mathematicians.pdf",
    tasks="15,C",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Accelerated C++.pdf",
    tasks="0-16,B",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="C++ by Dissection",
    tasks="11,D",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Beginning Cpp Programming.pdf",
    tasks="10",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Une introduction à Python 3.pdf",
    tasks="9,J",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="How Linux Works. What Every Superuser Should Know.pdf",
    tasks="17",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Введение в язык Си++.pdf",
    tasks="6",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools",
    tasks="1",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="C++ Tutorial 2021 - YouTube",
    tasks="1",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Язык программирование C++. Полное руководство.pdf",
    tasks="20,A",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="https://vcpkg.io/en/index.html",
    tasks="1",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="The C Programming Language 2e",
    tasks="7,C",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Lecture: Modern C++ (Summer 2018, Uni Bonn)",
    tasks="0-9",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="The Rook's Guide to Cpp.pdf",
    tasks="23",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Smaller C.pdf",
    tasks="7",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Уроки програмування на С++ для початківців / aCode",
    tasks="267",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Программирование на Java для начинающих.pdf",
    tasks="0-18",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Head First Design Patterns.pdf",
    tasks="14",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="NLP14) Transformers for Natural Language Processing.pdf",
    tasks="12",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Mythos Determinismus",
    tasks="8",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Шаблоны и практика глубокого обучения.pdf",
    tasks="14",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Использование Docker.pdf",
    tasks="13",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Computing with Data",
    tasks="15",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Шаблоны и практика глубокого обучения.pdf",
    tasks="14",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="https://sites.google.com/view/datascience-cheat-sheets",
    tasks="9,D",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Neural Networks and Deep Learning",
    tasks="9,A",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Introductory Mathematics: Algebra and Analysis (Smith)",
    tasks="8",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Clean Code (IT).pdf",
    tasks="17,C",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Clean Code. A Handbook of Agile Software Craftsmanship.pdf",
    tasks="17,C",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="MIT DL Course",
    tasks="8",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Introduction to Computer Organization. An Under the Hood Look at Hardware and x86-64 Assembly.pdf",
    tasks="21",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Україна - не Росія",
    tasks="30",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Hands-On Machine Learning with Cpp.pdf",
    tasks="13",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Modern CMake for Cpp.pdf",
    tasks="12,A",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Computer Science Illuminated",
    tasks="18",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="Computer Science - A Very Short Introduction",
    tasks="8",
    priority=Priority.MEDIUM,
    groups={""},
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)

g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
# 9,A
# A Concise Introduction to ML (Faul)

# Encyclopedia of Machine Learning and Data Mining.pdf
# 8
# Python FAQs
# 1
# ML Spider Diagram RU.jpg
# 1
# Taxonomy of Principal Distances.jpg
# .
# Linux intern
# 26,A6
# zsh Docs
# 38
# Python Standard Library
# 16,A
# All the Math You Missed
# 93
# Computing Handbook. Computer science and software engineering.pdf
# 14
# The Missing Semester of Your CS Education
# 15
# Computing with Data
# 25
# Building your Mouseless Development Environment
# 11
# NLP00) Natural Language Processing with Transformers.pdf
# 6
# Математика для Data Science [2021] Миронов, Минеева
# 1
# Intro to Github
# 13,A
# Machine Learning (Mitchell)
# 9
# Embeddings in Natural Language Processing. Theory and Advances in Vector Representation of
# 13
# Programming Languages. Principles and Paradigms
# 1
# Git Tutorial


# Week 12 – Practicum: Attention and the Transformer
# 13
# NLP12) NLP in Action.pdf
# 13,A6
# Обработка естественного языка в действии.pdf
# 7,A
# Modern Vim.pdf
# 16,A
# The Foundations of Mathematics (Ian Stewart)
# 16
# 3Blue1Brown Essence of Linear Algebra & Calculus & Neural Networks
# 35,B
# Гид по Computer Science.pdf
# 75
# Softwareengineering - Wie entwickelt man Software
# 24,A
# Code Craft - The Practice of Writing Excellent Code.pdf
# 0-9
# The Art of Clean Code.pdf

# Griechische Grammatik (Bornemann)
# A-Z
# Das lateinische Basisvokabular
# 0-7,A
# Introducción al sistema operativo GNU/Linux.pdf
# 4
# Design Patterns (Lasater).pdf
# 14
# Bin ich mein Gehirn?

# Самоучитель украинского языка
# 36
# Techtiefen
# 5
# Das illustrierte Kompendium der Philosophie
# 12
# Refactoring.pdf
# 35Lilian Weng Blog

# HelloChinese
# 14,D
# Programming Logic and Design, Comprehensive.pdf
# 6
# Learn TensorFlow 2.0.pdf
# 12
# Computer Systems - A Programmer's Perspective
# 8
# Practical Cryptography in Python. Learning Correct Cryptography by Example.pdf
# 32
# Ingeniería del software.pdf
# 1
# Sigmoid and Logit function | Logical Intuitions

# ix Developer - Machine Learning
# 1
# https://towardsdatascience.com/ai-papers-to-read-in-2022-c6edd4302247
# 1
# TF Certificate Handbook.pdf
# 11
# NLP26) Real-World Natural Language Processing.pdf
# 5
# NLP15) Audio Processing and Speech Recognition. Concepts, Techniques and Research Overviews.pdf
# 7

# Алгоритмы обработки текста. 125 задач с решениями.pdf

# Deep Learning from First Principles In Vectorized Python R and Octave.pdf
# 98
# Handbook of Linear Algebra
# 14,E
# Pattern Recognition and Machine Learning (Bishop)
# 31
# Наш творчий мозок.pdf
# 1
# An Introduction To Programs
# 1
# Lecture notes: Literature search and scientific reading
# 1
# C32 | SIFT | Scale Invariant Feature Transform | Computer Vision | Object detection | EvODN - YouTube
# 1
# Injecting fairness into machine-learning models

# Bert
# 1
# Learn Git Branching

# Код.pdf
# 25
# Code (Petzold)
# 24
# Python, например.pdf
# 18
# Learn Vim Tonight
# 15
# Philosophie des Orgasmus
# 20
# Dive into Deep Learning
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)
g.add_project(
    name="", tasks="", priority=Priority.MEDIUM, groups={""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1
)


# Machine Learning - An Applied Mathematics Introduction

# Introduction to Statistical Learning
# 12,A4
# The Healthy Programmer.pdf
# 16
# Грокаем глубокое обучение.pdf

# LPP 13-16
# 21
# NLP10) Neural Network Methods for NLP.pdf
# 13,I
# Programming from the Ground Up.pdf
# 4
# NLP08) NLP and CL I (Kurdi)
# 28,A
# Handbook of Mathematics
# 1
# Cython: The Best of Both Worlds.pdf
# 1
# Fast numerical computations with Cython.pdf
# 1
# Open letter
# 1
# Заблуждения и антишаблоны, относящиеся к devops.pdf
# 1
# Transformers
# 1

# https://marketplace.visualstudio.com/items?itemName=076923.python-image-preview
# 1
# Notation Sheet
# 1
# Deep Learning. A Comprehensive Overview.pdf
# 1
# nand2tetris 3
# 1
# https://sebastianraschka.com/faq/docs/logistic-why-sigmoid.html
# 1
# Linguistique computationnelle. Entre sciences cognitives et traitement automatique des langues.pdf
# 1
# nand2tetris 4
# 1
# Conditional Random Fields : Data Science Concepts - YouTube

# Attention is All You Need
# 1
# Cambridge NLP Notes.pdf
# 1
# Обработка естественного языка.pdf
# 1
# Современные методы обработки естественного языка.pdf
# 10
# But How Do It Know. The Basic Principles of Computers for Everyone.pdf
# 15
# CMake Cookbook

# Reinforcement Learning. An Introduction
# 27
# Align LPP
# 12
# NLP-01) Applied Natural Language Processing in the Enterprise.pdf
# 4
# Learn Bash the Hard Way.pdf
# 11
# Intro to Deep Learning (Skansi)
# 0-22,C
# First Year in Code
# ?
# C++20 Recipes.pdf
# ?
# Си на примерах. Практика
# ?
# Язык Си для начинающих
# ?
# Effective C
# ?
# https://hackingcpp.com/cpp/cheat_sheets.html
# ?
# Mastering C Pointers.pdf
# ?
# Modern C
# ?
# Язык Си для начинающих

# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)
# g.add_project(name="", tasks="", priority=Priority.MEDIUM, groups = {""}, start=Date.today() + 3, end=Date.today() + 60, cluster=1)


# 	Machine Learning Engineering in Action
# 	Machine Learning Engineering with MLFlow (Hank and (Elsie)
# 	Machine Learning Engineering.pdf
# 	Параллельные и высокопроизводительные вычисления.pdf
# 	Deep Learning Illustrated
# 	Deep Learning for Coders with Fastai and PyTorch
# 	Machine Learning Hands-on for Developers and Technical Professionals
# 	Mastering Machine Learning Algorithms
# 	Transfer Learning
# 	Math for Deep Learning. What You Need to Know.pdf
# 	Thoughtful Machine Learning with Python.pdf
# 	Глубокое обучение в картинках.pdf
# 	Redes neuronales & deep learning
# 	Data Scientists at Work.pdf
# 10,B	Python Language Reference
# 8	https://www.programiz.com/python-programming/methods/built-in/classmethod
# 6	ix Developer - Sichere Software entwickeln
# 13	Advanced Deep Learning with TensorFlow 2 and Keras.pdf
# 	Inteligencia artificial avanzada.pdf
# 7,C	Computer Science. An Interdisciplinary Approach.pdf
# 	Word2Vec
# 1	Git Handbook
# 1	Page Segmentation of Historical Document Images  with Convolutional Autoencoders.pdf
# 1	https://uk.wikipedia.org/wiki/Машинне_навчання
# 1	Logique, Linguistique et Informatique.pdf
# 1	Simple Explanation of LSTM | Deep Learning Tutorial 36 (Tensorflow, Keras & Python) - YouTube
# 16	Functional Python Programming. Discover the power of functional programming, generator functions, lazy evaluation, the built-in itertools library, and monads.pdf
# 14	The Missing README.pdf
# 26,J	Test-Driven Development with Python.pdf
# 6,A	Neural Networks and Deep Learning (Michael Nielsen)
# 15,C		Computer Vision Algorithms and Applications.pdf
# 19	Bewusstsein und freier Wille
# 19	Машинное обучение. Карманный справочник.pdf
# 13,A5	Elements of Computing Systems (2e)
# 8	Agile (PT).pdf
# 9	NLP Overview
# 8,Conc,D	Теоретический минимум по Computer Science
# 9,D	Computer Science Distilled
# 12,A3	Numbers and Functions: Steps into Analysis (Burn)
# 4	Object-oriented vs Functional Programming.pdf
# 25,A	Изучаем Python, том 1.pdf
# 1000Make list of top 1000 Chinese characters, all input codes, constituent radicals, character combinations, pronunciations, eventually example phrases
# 6	Big Data PT.pdf
# 21	Mastering Vim
# 16	Python Tutorial
# 12Dialogues Project
# 17,D	Learning the Vi and Vim Editors
# 8,A	Der freie Wille
# I,II,1-30,VIII	Машинное обучение. Паттерны проектирования.pdf
# 0-15	The Secret Life of Programs. Understand Computers, Craft Better Code.pdf
# 26	The Linux Philosophy for SysAdmins.pdf
# 27	https://book.pythontips.com/en/latest/index.html
# 20	The Python Book.pdf
# 19,K	Learn to Program with Assembly
# 19,В	Стандартная библиотека Python 3.pdf
# 19	https://pybind11.readthedocs.io/en/latest/
# 17	Beyond the Basic Stuff with Python. Best Practices.pdf
# 15		Читаемый код.pdf
# 15	Linux in a Nutshell.pdf
# 14,E	Паттерны разработки на Python. TDD, DDD и событийно-ориентированная архитектура.pdf
# 13	Serious Python.pdf
# 13	The Programmer's Brain. What Every Programmer Needs.pdf
# 12	3Blue1Brown Calculus
# 12	Full Speed Python.pdf
# 12	The Machine Learning Solutions Architect Handbook.pdf
# 6	Mastering Python for Web. A Beginner's Guide.pdf
# 10		Concise Computer Vision.pdf
# 10	Регулярные выражения.pdf
# 	Ukrainian. A Comprehensive Grammar
# 200	https://euler.stephan-brumme.com/
# 1	Deep Learning for Amharic Text-Image Recognition: Algorithm, Dataset and Application
# 9	Street Coder.pdf
# 1	Python 3.3-Tutorial auf Deutsch - überfliegen und wegwerfen
# -	nand2tetris 6
# 		https://zsh.sourceforge.io/Guide/zshguide.html
# 1	Episode 10: Deep Neural Networks in Julia with Flux.jl
# 6	Вища математика I. Підручник у 2 частинах.pdf
# 11	Ich denke zu viel
# 0-5,A	Программист-фанатик.pdf
# 10	Computing Systems (Elahi)
# 19	Элементарное введение в высшую математику.pdf
# 1	https://en.wikipedia.org/wiki/Template:Design_Patterns_patterns
# 		Add Pipeline books to Roadmap
# -	nand2tetris 7
# 1	Consolidate Learning Scripts & Keyboards and Carácteres y radicales chinos and HSK
# 25	Software Engineering.pdf
# 9	Ali Baba
# 5		https://docs.python.org/3/extending/
# 1	Emacs Tour
# 1	https://mimno.github.io/Mallet/index
# 1	https://github.com/chokkan/crfsuite
# 1	https://sourceforge.net/projects/hcrf/
# 1	http://crf.sourceforge.net/
# 1	https://github.com/yalesong/hCRF-light
# 1	http://flexcrfs.sourceforge.net/
# 1	[Code] How to use Facebook's DETR object detection algorithm in Python (Full Tutorial)
# 1	CV3DST - Transformers and DETR
# 1	Data: The Past, the Present and the Future
# 1	DETR - End to end object detection with transformers (ECCV2020)
# 1	DETR Paper arXiv Repo PwC
# 1	DETR: End-to-End Object Detection with Transformers (Paper Explained)
# 1	DETR: End-to-End Object Detection with Transformers | Paper Explained
# 1	How I Read a Paper: Facebook's DETR (Video Tutorial)
# 1	Networks: The Internet and Beyond
# 1	Regression Cheatsheet.jpg
# 9	Automated Machine Learning in Action.pdf
# 11	Прекрасный, опасный, кибербезопасный мир.pdf
# 24	Мозок - це ми.pdf
# 1	nand2tetris 2
# 1	Genealogy of Programming Languages.pdf
# 1	MMOD paper
# 1	Why do linear SVMs trained on HOG features perform so well?
# 1	ML Algorithms List.jpg
# -	nand2tetris 8
# 1	GibbsLDA++: A C/C++ Implementation of Latent Dirichlet Allocation (LDA)
# 1	CRFTagger: CRF English POS Chunker
# 1	CRFChunker: CRF English Phrase Chunker
# 1	nand2tetris 5
# 1	https://towardsdatascience.com/xgboost-an-intuitive-explanation-88eb32a48eff
# 35	Code Complete - A Practical Handbook of Software Construction.pdf
# 	The Data Science Design Manual
# 7	Практическая статистика для специалистов Data Science.pdf
# 1	https://www.analyticsinsight.net/top-10-java-projects-that-beginners-should-master-in-2022/
# 1	https://www.geeksforgeeks.org/image-processing-in-java-changing-orientation-of-image/?ref=rp
# 1	JTextPro: A Java-based Text Processing Toolkit
# 1	JWebPro: A Java-based Web Processing Toolkit
# 17	Introduction to Metric and Topological Spaces (Sutherland)
# 10	Nano Docs
# 15		Cogneethi - Classical CV - HOG and SIFT intuitions
# 1	Nano Cheatsheet
# 1	Computational Linguistics and Deep Learning.pdf
# 	Elmo
# 1	Reviewing Pull Requests
# 6	Computerlinguistik und Sprachtechnologie.pdf
# 89	https://exercism.org/tracks/bash
# 13	Flask Framework Cookbook.pdf
# 5	Ich denke, also will ich: Philosophie des freien Willens
# 1	Computers: A History
# 1	The Future of Computer Security
# 3	Система построения проектов CMake.pdf
# 8	Чистый Agile. Основы гибкости.pdf
# 19	Software Development, Design, and Coding.pdf
# 26	Software Engineering. Grundlagen, Menschen, Prozesse, Techniken.epub
# 28	Professional CMake. A Practical Guide.pdf
# 0-9,B	Scrum. Революционный метод управления проектами.pdf
# 15,A	Pro bash programming: scripting the GNU/Linux shell
# 15,B	Сценарии командной оболочки.pdf
# 5,A	Real-World Kanban.pdf
# 	Машинное обучение с участием человека.pdf
# 	GPT-2
# 	“Tabular data: Deep learning is not all you need.”
# 	Universal Language Model Fine-tuning for Text Classification
# 	Improving Language Understanding by Generative Pre-Training
# 	Learning an Executable Neural Semantic Parser
# 0-20	GEB 2-3, 5-8
# 		https://blog.codinghorror.com/recommended-reading-for-developers/
# 6,C	Introduction to Programming Languages. Programming in C, C++, Scheme, Prolog, g, C#, and SOA.pdf
# 12,I	Assembly Programming and Computer Architecture for Software Engineers.pdf
# 8	Computer Science: A Very Short Introduction
# 	200 frases - Noruego - Español
# 	Aprender yidis
# 	Colloquial Arabic (Levantine)
# 	Robust Python.pdf
# 	Full-Stack Python Security.pdf
# 	Modern Python Cookbook.pdf
# 	Linux Bible
# 	The TCP,IP Guide. A Comprehensive, Illustrated Internet Protocols Reference.pdf
# 67	Handbook of Data Structures and Applications.pdf
# 645	Encyclopedia of Algorithms.pdf
# 6	Mastering ML with Python in Six Steps
# 1	https://numpy.org/doc/stable/reference/c-api/index.html
# 32	Самоучитель Python.pdf
# 4,A	Introduction to Mathematical Thinking (Devlin)
# 0-15,C	Разработка конвейеров машинного обучения.pdf
# 16	Python HOWTOs
# 13	Functional Programming in Python (2019).pdf
# 46	Tacitus Germania
# 1	write clustering section of ML Cheatsheet & make PR
# 17,A	Write Great Code 2
# 16,B	Write Great Code 1
# 14	Object-Oriented Programming in Python.pdf
# 14	Python Object-Oriented Programming.pdf
# 71	Soft Skills.pdf
# 47,B	O Programador Pragmático.pdf
# 0-14,A	Идеальный программист. Как стать профессионалом разработки ПО
# 5	Optimizing Visual Studio Code for Python Development
# 31	Introducción a los Patrones de Diseño.pdf
# 42,Б	Python. Экспресс-курс.pdf
# 27,F	The Coder’s Apprentice. Learning Programming with Python 3.pdf
# 74	https://python-patterns.guide/
# 10	Visual Studio Code. End-To-End...
# 11	Visual Studio Code Distilled
# 12	Visual Studio Code for Python Programmers
# 29,A	C++ - das Übungsbuch
# 13,B	Микросервисы и контейнеры Docker.pdf
# 34,A	Совершенный код. Мастер-класс.pdf
# 53	Assimil Hindi
# 17		Cogneethi - Convolutional Neural Networks Basics & Intuitions
# 	Программирование GPU при помощи Python и CUDA.pdf
# 	Deep Learning with PyTorch Step-by-Step
# 	Neural Networks
# 	PyTorch Pocket Reference
# 	PyTorch Basics for Absolute Beginners.epub
# 	The Supervised Learning Workshop.pdf
# 	Глубокое обучение 1 (Гласснер).pdf
# 	Глубокое обучение 2 (Гласснер).pdf
# 	Data science from Scratch 2e.pdf
# 	Hands-On Python Deep Learning for the Web. Integrating neural network architectures to build smart web apps with Flask, Django, and TensorFlow.pdf
# 0-9	Программирование Cloud Native. Микросервисы, Docker и Kubernetes.pdf
# 0-58	Learn Java the Hard Way.pdf
# 20	https://exercism.org/tracks/vimscript
# 16,B	Hacking APIs Breaking Web Application Programming Interfaces.pdf
# 19	The Algorithm Design Manual
# 13	sed & awk 101 Hacks.pdf
# 15	GNU sed. Awesome Stream Editor.pdf
# 0-35,D	Introduction to Algorithms
# 8	First Course in Algorithms through Puzzles
# 16,C	Effective awk Programming. Universal Text Processing and Pattern Matching.pdf
# 6	Learning Shell Scripting with zsh.pdf
# 13,C	Sed & Awk.pdf
# 13,C	The Object-Oriented Thought Process.pdf
# 25	Learn Git the Hard Way.pdf
# 7	Git Essentials.pdf
# 8	How Open Source Ate Software.pdf
# 8	Mastering Git. A Beginner's Guide.pdf
# 9	Practical Git.pdf
# 11	Advanced Git.pdf
# 12	Git Version Control Cookbook.pdf
# 12	Git. Практическое руководство.pdf
# 15	Professional Git.pdf
# 19	Beginning Git and Github.pdf
# 20	GitHub for Dummies.pdf
# 20	Learn Git in a Month of Lunches.pdf
# 22	Mastering Git.pdf
# 61	Git Notes for Professionals.pdf
# -	nand2tetris 12
# 0-7	Git Succinctly.pdf
# 10,A3	Git - Book
# 10,C	Git для профессионального программиста.pdf
# 8,A	Head First Git.pdf
# 9,A	Pro Git.pdf
# 34	Чистая архитектура. Искусство разработки программного обеспечения.pdf
# 	Еще более эффективный Agile.pdf
# 	Карьера программиста.pdf
# 	Mathematics for Machine Learning
# 	“A ConvNet for the 2020s.”
# 	Unsupervised Compositionality Prediction of Nominal Compounds
# 	Automatic Inference of Sound Correspondence Patterns across Multiple Languages
# 	A Sequential Matching Framework for Multi-Turn Response Selection in Retrieval-Based Chatbots
# 	Parsing Chinese Sentences with Grammatical Relations
# 	300 verbos + Leer y escuchar: - Noruego + Español
# 	Modern Cpp Tutorial.pdf
# 	Программирование на С.pdf
# 	Программирование на языке Cpp.pdf
# 	Hands-On Machine Learning with C++
# 	C++ українською
# 	Cpp for Lazy Programmers.pdf
# 	Cpp20 for Programmers.pdf
# 	Discovering Modern C++
# 	Exploring C++20
# 	Corso di informatica 1. Linguaggio C e Cpp.pdf
# 	Corso di informatica 2. Linguaggio C e Cpp.pdf
# 	Tour of C++
# 	A Book on C
# 	The C++ Workshop
# 34,D		add Professional C++
# 	Guide to NumPy (2006).pdf
# 	Классические задачи Computer Science на языке Python.pdf
# 	https://exercism.org/tracks/python
# 	Tiny Python Projects.pdf
# 	Автоматизация рутинных задач с помощью Python.pdf
# 	Python. Сборник упражнений.pdf
# 	Python. Книга рецептов.pdf
# 	Однострочники Python лаконичный и содержательный код.pdf
# 	Architcture Patterns with Python
# 	Python. Разработка на основе тестирования.pdf
# 	INTO_IT: C Programmieren trainieren! - YouTube
# 	Le langage C
# 	Mastering C++ Programming Language.pdf
# 	Modern C Quick Syntax Reference
# 	Programmieren in C - YouTube C Tutorials Deutsch
# 	Sams Teach Yourself C++ in One Hour a Day (2022)
# 	The C++ Standard Library. A Tutorial and Reference.pdf
# 	https://exercism.org/tracks/cpp
# 	Conceitos de computação com o essencial de C++.pdf
# 	C++. Lernen und professionell anwenden.pdf
# 	C++20 for Programmers.pdf
# 	Экстремальный Си.pdf
# 	Экстремальный Си.pdf
# 	The C++ Programming Language
# 	100 algoritmos C++.pdf
# 	Algoritmos em Linguagem C.pdf
# 	Решение задач на современном C++.pdf
# 	Cpp Notes for Professionals.pdf
# 	Cpp Programming. Program Design Including Data Structures.pdf
# 	Design Patterns in Modern C++.pdf
# 	Design Patterns in Modern C++20.pdf
# 	Hands-On Design Patterns with Cpp.pdf
# 	Il linguaggio C (Deitel).pdf
# 	Open Data Structures (in C++).pdf
# 	Programming Principles and Practices C++.pdf
# 	Думай как программист - C++.pdf
# 	C++ для профи.pdf
# 	Guide to Competitive Programming.pdf
# 	C – kurz & gut
# 	Clean C++.pdf
# 	Оптимизация программ на C++.pdf
# 	Функциональное программирование на языке C++.pdf
# 	Алгоритмические трюки для программистов.pdf
# 	Beautiful Cpp. 30 Core Guidelines for Writing Clean, Safe, and Fast Code.pdf
# 	C und Linux
# 	Data Structures and Algorithm  Analysis in C++.pdf
# 	Effective C++ (140).pdf
# 	Effective Modern C++
# 	Expert C++.pdf
# 	Practical C++ Design
# 	Programación en C, C++, Java y UML.pdf
# 	Software Architecture with C++
# 	String Algorithms in C.pdf
# 	Безопасное программирование на C и C++.pdf
# 	Introduction to Programming in Java. An Interdisciplinary Approach.pdf
# 	Java Cookbook.pdf
# 	Java for Data Science.pdf
# 	Java Programming (Farrell).pdf
# 	Java Programming. From The Ground Up.pdf
# 	Java для начинающих.pdf
# 	Java полное руководство.pdf
# 	Java. A Beginner's Guide.pdf
# 	Java. Справочник разработчика.pdf
# 	Java.djvu
# 	Mastering Java. A Beginner's Guide.pdf
# 	Mastering Java. An Effective Project Based Approach (including Web).pdf
# 	Введение в объектно-ориентированный дизайн с Java.pdf
# 	Классические задачи Computer Science на языке Java.pdf
# 	Джава. Решение практических задач.pdf
# 	Java Pocket Guide
# 	Java by Comparison. Become a Java Craftsman in 70 Examples.pdf
# 	Java Succinctly Part 2.pdf
# 	Java and the Java Virtual Machine Definition, Verification, Validation.pdf
# 	Java Virtual Machine.pdf
# 	Modern Java in Action.pdf
# 	Principles of Computer Organization and Assembly Language Using the JavaTM Virtual Machine.pdf
# 	Programming for the Java Virtual Machine.pdf
# 	The Java® Virtual Machine Specification.pdf
# 	Well-Grounded Java Developer.pdf
# 	Система модулей Java.pdf
# 	Современный Java 2020.pdf
# 	Объектно-ориентированное программирование на Java. Платформа Java SE.pdf
# 	Структуры данных и алгоритмы Java.pdf
# 	Decompiling Java.pdf
# 	“A survey of transformers.”
# 	Avrim Blum and Tom Mitchell: Combining Labeled and Unlabeled Data with Co-Training, 1998.
# 	John Lafferty, Andrew McCallum, Fernando C.N. Pereira: Conditional Random Fields: Probabilistic Models for Segmenting and Labeling Sequence Data, ICML 2001.
# 	Charles Sutton, Andrew McCallum. An Introduction to Conditional Random Fields for Relational Learning.
# 	Kamal Nigam, et al.: Text Classification from Labeled and Unlabeled Documents using EM. Machine Learning, 1999.
# 	“A simple framework for contrastive learning of visual representations.”
# 	Kevin Knight: Bayesian Inference with Tears, 2009.
# 	Marco Tulio Ribeiro et al.: “Why Should I Trust You?”: Explaining the Predictions of Any Classifier, KDD 2016.
# 	Marco Tulio Ribeiro et al.: Beyond Accuracy: Behavioral Testing of NLP Models with CheckList, ACL 2020.
# 	Richard Socher, et al.: Dynamic Pooling and Unfolding Recursive Autoencoders for Paraphrase Detection, NIPS 2011.
# 	“Efficientnet: Rethinking model scaling for convolutional neural networks.”
# 	Ronan Collobert et al.: Natural Language Processing (almost) from Scratch, J. of Machine Learning Research, 2011.
# 	Richard Socher, et al.: Recursive Deep Models for Semantic Compositionality Over a Sentiment Treebank, EMNLP 2013.
# 	Xiang Zhang, Junbo Zhao, and Yann LeCun: Character-level Convolutional Networks for Text Classification, NIPS 2015.
# 	Yoon Kim: Convolutional Neural Networks for Sentence Classification, 2014.
# 	“Pushing the limits of narrow precision inferencing at cloud scale with microsoft floating point.”
# 	Christopher Olah: Understanding LSTM Networks, 2015.
# 	Matthew E. Peters, et al.: Deep contextualized word representations, 2018.
# 	Jacob Devlin, et al.: BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding, 2018.
# 	Yihan Liu et al. RoBERTa: A Robustly Optimized BERT Pretraining Approach, 2020.
# 	“AdderNet: Do we really need multiplications in deep learning?.”
# 	Peter F Brown, et al.: Class-Based n-gram Models of Natural Language, 1992.
# 	Tomas Mikolov, et al.: Efficient Estimation of Word Representations in Vector Space, 2013.
# 	Tomas Mikolov, et al.: Distributed Representations of Words and Phrases and their Compositionality, NIPS 2013.
# 	Quoc V. Le and Tomas Mikolov: Distributed Representations of Sentences and Documents, 2014.
# 	“Alias-free generative adversarial networks.”
# 	Jeffrey Pennington, et al.: GloVe: Global Vectors for Word Representation, 2014.
# 	Ryan Kiros, et al.: Skip-Thought Vectors, 2015.
# 	Piotr Bojanowski, et al.: Enriching Word Vectors with Subword Information, 2017.
# 	Daniel Cer et al.: Universal Sentence Encoder, 2018.
# 	“Transparency and reproducibility in artificial intelligence.”
# 	Thomas Hofmann: Probabilistic Latent Semantic Indexing, SIGIR 1999.
# 	David Blei, Andrew Y. Ng, and Michael I. Jordan: Latent Dirichlet Allocation, J. Machine Learning Research, 2003.
# 	Joshua Goodman: A bit of progress in language modeling, MSR Technical Report, 2001.
# 	Stanley F. Chen and Joshua Goodman: An Empirical Study of Smoothing Techniques for Language Modeling, ACL 2006.
# 	“On the Measure of Intelligence.”
# 	Yee Whye Teh: A Hierarchical Bayesian Language Model based on Pitman-Yor Processes, COLING/ACL 2006.
# 	Yee Whye Teh: A Bayesian interpretation of Interpolated Kneser-Ney, 2006.
# 	Yoshua Bengio, et al.: A Neural Probabilistic Language Model, J. of Machine Learning Research, 2003.
# 	Andrej Karpathy: The Unreasonable Effectiveness of Recurrent Neural Networks, 2015.
# 	Why do linear SVMs trained on HOG features perform so well?
# 	Yoon Kim, et al.: Character-Aware Neural Language Models, 2015.
# 	Alec Radford, et al.: Language Models are Unsupervised Multitask Learners, 2018.
# 	Donald Hindle and Mats Rooth. Structural Ambiguity and Lexical Relations, Computational Linguistics, 1993.
# 	Adwait Ratnaparkhi: A Maximum Entropy Model for Part-Of-Speech Tagging, EMNLP 1996.
# 	Eugene Charniak: A Maximum-Entropy-Inspired Parser, NAACL 2000.
# 	Michael Collins: Discriminative Training Methods for Hidden Markov Models: Theory and Experiments with Perceptron Algorithms, EMNLP 2002.
# 	Dan Klein and Christopher Manning: Accurate Unlexicalized Parsing, ACL 2003.
# 	Dan Klein and Christopher Manning: Corpus-Based Induction of Syntactic Structure: Models of Dependency and Constituency, ACL 2004.
# 	Joakim Nivre and Mario Scholz: Deterministic Dependency Parsing of English Text, COLING 2004.
# 	Ryan McDonald et al.: Non-Projective Dependency Parsing using Spanning-Tree Algorithms, EMNLP 2005.
# 	Daniel Andor et al.: Globally Normalized Transition-Based Neural Networks, 2016.
# 	Oriol Vinyals, et al.: Grammar as a Foreign Language, 2015.
# 	Marti A. Hearst: Automatic Acquisition of Hyponyms from Large Text Corpora, COLING 1992.
# 	Collins and Singer: Unsupervised Models for Named Entity Classification, EMNLP 1999.
# 	Patrick Pantel and Dekang Lin, Discovering Word Senses from Text, SIGKDD, 2002.
# 	Mike Mintz et al.: Distant supervision for relation extraction without labeled data, ACL 2009.
# 	Zhiheng Huang et al.: Bidirectional LSTM-CRF Models for Sequence Tagging, 2015.
# 	Xuezhe Ma and Eduard Hovy: End-to-end Sequence Labeling via Bi-directional LSTM-CNNs-CRF, ACL 2016.
# 	Peter F. Brown et al.: A Statistical Approach to Machine Translation, Computational Linguistics, 1990.
# 	Kevin Knight, Graehl Jonathan. Machine Transliteration. Computational Linguistics, 1992.
# 	Dekai Wu: Inversion Transduction Grammars and the Bilingual Parsing of Parallel Corpora, Computational Linguistics, 1997.
# 	Kevin Knight: A Statistical MT Tutorial Workbook, 1999.
# 	Kishore Papineni, et al.: BLEU: a Method for Automatic Evaluation of Machine Translation, ACL 2002.
# 	Philipp Koehn, Franz J Och, and Daniel Marcu: Statistical Phrase-Based Translation, NAACL 2003.
# 	Philip Resnik and Noah A. Smith: The Web as a Parallel Corpus, Computational Linguistics, 2003.
# 	Franz J Och and Hermann Ney: The Alignment-Template Approach to Statistical Machine Translation, Computational Linguistics, 2004.
# 	David Chiang. A Hierarchical Phrase-Based Model for Statistical Machine Translation, ACL 2005.
# 	Ilya Sutskever, Oriol Vinyals, and Quoc V. Le: Sequence to Sequence Learning with Neural Networks, NIPS 2014.
# 	Oriol Vinyals, Quoc Le: A Neural Conversation Model, 2015.
# 	Dzmitry Bahdanau, et al.: Neural Machine Translation by Jointly Learning to Align and Translate, 2014.
# 	Minh-Thang Luong, et al.: Effective Approaches to Attention-based Neural Machine Translation, 2015.
# 	Rico Sennrich et al.: Neural Machine Translation of Rare Words with Subword Units. ACL 2016.
# 	Yonghui Wu, et al.: Google’s Neural Machine Translation System: Bridging the Gap between Human and Machine Translation, 2016.
# 	Melvin Johnson, et al.: Google’s Multilingual Neural Machine Translation System: Enabling Zero-Shot Translation, 2016.
# 	Jonas Gehring, et al.: Convolutional Sequence to Sequence Learning, 2017.
# 	Ashish Vaswani, et al.: Attention Is All You Need, 2017.
# 	Vincent Ng: Supervised Noun Phrase Coreference Research: The First Fifteen Years, ACL 2010.
# 	Kenton Lee at al.: End-to-end Neural Coreference Resolution, EMNLP 2017.
# 	Kevin Knight and Daniel Marcu: Summarization beyond sentence extraction. Artificial Intelligence 139, 2002.
# 	James Clarke and Mirella Lapata: Modeling Compression with Discourse Constraints. EMNLP-CONLL 2007.
# 	Ryan McDonald: A Study of Global Inference Algorithms in Multi-Document Summarization, ECIR 2007.
# 	Wen-tau Yih et al.: Multi-Document Summarization by Maximizing Informative Content-Words. IJCAI 2007.
# 	Alexander M Rush, et al.: A Neural Attention Model for Sentence Summarization. EMNLP 2015.
# 	Abigail See et al.: Get To The Point: Summarization with Pointer-Generator Networks. ACL 2017.
# 	Pranav Rajpurkar et al.: SQuAD: 100,000+ Questions for Machine Comprehension of Text. EMNLP 2015.
# 	Minjoon Soo et al.: Bi-Directional Attention Flow for Machine Comprehension. ICLR 2015.
# 	Jiwei Li, et al.: Deep Reinforcement Learning for Dialogue Generation, EMNLP 2016.
# 	Marc’Aurelio Ranzato et al.: Sequence Level Training with Recurrent Neural Networks. ICLR 2016.
# 	Samuel R Bowman et al.: Generating sentences from a continuous space, CoNLL 2016.
# 	Lantao Yu, et al.: SeqGAN: Sequence Generative Adversarial Nets with Policy Gradient, AAAI 2017.
# 	CoNLL-X shared task on multilingual dependency parsing.
# 	Coarse-to-fine n-best parsing and MaxEnt discriminative reranking.
# 	The CoNLL-2010 shared task: learning to detect hedges and their scope in natural language text.
# 	WordNet: An electronic lexical database. 1998.
# 	Accurate unlexicalized parsing.
# 	Automatic retrieval and clustering of similar words.
# 	Building a large annotated corpus of English: The Penn Treebank.
# 	The proposition bank: An annotated corpus of semantic roles.
# 	BLEU: a method for automatic evaluation of machine translation.
# 	Improved Inference for Unlexicalized Parsing.
# 	Вища математика II. Підручник у 2 частинах.pdf
# 	3Blue1Brown Differential Equations
# 	Mathematik
# 	Artin - Algebra.pdf
# 	Algebra, Topology, Differential Calculus, and Optimization Theory for Computer Science and Machine Learning
# 	Principles of Mathematical Analysis (Rudin)
# 	Videos: Socratica Abstract Algebra Playlist
# 	Linear Algebra Done Right (Axler)
# 	Linear Algebra (Insel, Freidberg, Spence - problems)
# 	Videos: Sheldon Axler’s Playlist
# 	Introduction to Linear Algebra, Fourth Edition by Gilbert Strang
# 	Basic Linear Algebra (Blyth & Robertson)
# 	MIT Open Courseware Video Lectures - Linear Algebra by Gilbert Strang
# 	Geometry by Roger Fenn
# 	Metric Spaces (O'Searcoid)
# 	Measure, Integral and Probability (Capinski & Kopp, 2E)
# 	MIT OCW Measure and Integration
# 	A First Course in Probability (Ross)
# 	Schaum's Outline of Probability and Statistics
# 	Probability and Statistics by Example: Volume 1 (Suhov & Kelbert)
# 	Statistical Inference (Casella & Berger)
# 	Real Analysis: Lectures by Professor Francis Su
# 	Understanding Analysis (Abbott)
# 	Videos: MAT137 Playlist
# 	Real Analysis (Howie)
# 	Topology through Inquiry (Su & Starbird)
# 	Essential Topology (Crossley)
# 	Videos: WhyBMaths
# 	Foundations of Applied Mathematics.pdf
# 	https://pnp.mathematik.uni-stuttgart.de/igt/eiserm/lehre/Lineare-Algebra/
# 	Vector Calculus (Matthews)
# 	3Blue1Brown Neural Networks
# 	Statistical Rethinking 2022
# 	Measure Theory and Probability (MathematicalMonk)
# 	Mathematical Tripos examination questions in IB Statistics
# 	Div, Grad, Curl, and All That: An Informal Text on Vector Calculus (Schey)
# 	MIT OCW Multivariable Calculus
# 	ACME: Data Science Essentials →
# 	ACME: Foundations of Applied Mathematics, Volume 1. Mathematical Analysis.pdf
# 	ACME: Labs I
# 	ACME: Labs I.pdf
# 	ACME: Python Essentials.pdf
# 	ACME: README.pdf
# 	Think Bayes. Bayesian Statistics in Python.pdf
# 	Think stats.pdf
# 	Pure Mathematics for Beginners. A Rigorous Introduction to Logic, Set Theory, Abstract Algebra, Number Theory, Real Analysis, Topology, Complex Analysis, and Linear Algebra.pdf
# 	Байесовская статистика.pdf
# 	Classic Algebra by P.M. Cohn
# 	Matlab - A Practical Introduction to Programming and Problem Solving (Attaway 3E)
# 	Online Notes: MAT327 Course Notes
# 	Problems: MAT 327 Course Problems
# 	Videos: Point Set Topology Playlist
# 	Algebraic Topology Playlist
# 	Concrete Abstract Algebra: From Numbers to Gröbner Bases by N. Lauritzen
# 	Contemporary Abstract Algebra (Gallian)
# 	Introduction to Manifolds (Tu, for rigor)
# 	Groups (Jordan & Jordan)
# 	Schaum's Outline of Group Theory (Baumslag & Chandle)
# 	Groups, Rings and Fields (Wallace)
# 	Online Notes: MAT327 Course Notes <>
# 	ACME: Foundations of Applied Mathematics, Volume 2. Algorithms, Approximation, Optimization.pdf
# 	ACME: Labs II
# 	ACME: Labs II.pdf
# 	Elementary Differential Equations and Boundary Value Problems (Boyce & DiPrima)
# 	MIT Open CourseWare Video Lectures - Differential Equations by Arthur Mattuck
# 	Stability, Instability and Chaos: An Introduction to the Theory of Nonlinear Differential Equations (Glendinning)
# 	Differential Equations with Boundary Value Problems (Zill & Cullen)
# 	An Introduction to Ordinary Differential Equations (Robinson)
# 	Visual Complex Analysis (Needham, for intuition)
# 	Analysis of a Complex Kind (Petra Bonfert-Taylor)
# 	A Geometric Approach to Differential Forms (Bachman, for intuition)
# 	Differential Equations
# 	Ordinary Differential Equations: Analysis, Qualitative Theory and Control (Logemann & Ryan)
# 	Scalar, Vector, and Matrix Mathematics
# 16A	The Kubernetes Book.pdf
# 8	Consciousness: A Very Short Introduction
# 1	What Kind of Computation Is Cognition?
# 20	^ https://github.com/pdeitel/CPlusPlus20ForProgrammers
# 1	Manim tutorial | Introduction: What is Manim?
# 1	Make Videos Like 3Blue1Brown | Manim
# 1	How 3 Blue 1 Brown makes animations  | Manim Tutorial
# 1	Advice for using Manim | Grant Sanderson and Lex Fridman
# ---	Computational Thinking | MIT 18.S191/6.S083 Spring 2021
# ---	Computational Thinking | MIT 18.S191/6.S083 Spring 2023
# ---	Computational Thinking | MIT 18.S191/6.S083 Spring 2025
# ---	Computational Thinking | MIT 18.S191/6.S083 Spring 2027
# ---	Computational Thinking | MIT 18.S191/6.S083 Spring 2029
# ---	Computational Thinking | MIT 18.S191/6.S083 Spring 2031
# ---	Computational Thinking | MIT 18.S191/6.S083 Spring 2033
# ---	Computational Thinking | MIT 18.S191/6.S083 Spring 2035
# ---	Computational Thinking | MIT 18.S191/6.S083 Spring 2037
# ---	Computational Thinking | MIT 18.S191/6.S083 Spring 2039
# ---	Computational Thinking | MIT 18.S191/6.S083 Spring 2041
# ---	Computational Thinking | MIT 18.S191/6.S083 Spring 2043
# ---	Computational Thinking | MIT 18.S191/6.S083 Spring 2045
# ---	Computational Thinking | MIT 18.S191/6.S083 Spring 2047
# ---	Computational Thinking | MIT 18.S191/6.S083 Spring 2049
# ---	Computational Thinking | MIT 18.S191/6.S083 Spring 2051
# ---	Computational Thinking | MIT 18.S191/6.S083 Spring 2053
# ---	Computational Thinking | MIT 18.S191/6.S083 Spring 2055
# ---	Computational Thinking | MIT 18.S191/6.S083 Spring 2057
# ---	Computational Thinking | MIT 18.S191/6.S083 Spring 2059
# ---	Computational Thinking | MIT 18.S191/6.S083 Spring 2061
# ---	Computational Thinking | MIT 18.S191/6.S083 Spring 2063
# ---	Computational Thinking | MIT 18.S191/6.S083 Spring 2065
# ---	Computational Thinking | MIT 18.S191/6.S083 Spring 2067
# ---	Computational Thinking | MIT 18.S191/6.S083 Spring 2069
# ---	Data Science with Julia.pdf
# ---	Julia - Bit by Bit: Programming for Beginners (Undergraduate Topics in Computer Science)
# ---	Julia 1.0 Programming Dynamic and High-Performance Programming to Build Fast Scientific Applications.epub
# ---	Julia 1.7.pdf
# ---	Julia Express.pdf
# ---	Julia for Data Science.pdf
# ---	Julia for R Programmers.pdf
# ---	Julia Language. A Concise Tutorial.pdf
# ---	Julia Programming Projects
# ---	Julia.pdf
# ---	Learn Julia by building a number guessing game!
# ---	Learning Julia.pdf
# ---	Mastering Julia.pdf
# ---	Statistics with Julia.pdf
# ---	Осваиваем язык Julia.pdf
# ---	https://exercism.org/tracks/julia
# 1	https://docs.python.org/3/library/ctypes.html
# 1	Physics
# 1	PS MrW2G
# ---	PoissonNote.dvi - PoissonNote.pdf
# ---	Proof of existence and proof of uniqueness of determinant
# ---	Prove 8 statements in the key theorem of LA (All the Math You Missed, 1.6)
# ---	Operating system for beginners || Operating system basics - YouTube
# ---	https://wiki.archlinux.org/title/Installation_guide
# ---	https://linux-audit.com/elf-binaries-on-linux-understanding-and-analysis/
# ---	April 9 -  Comparing Programming Languages Part 3 - C, Rust, Java, Kotlin, Go, JS/TS, Python, and Ruby  (12 mins)
# ---	March 29 -  Comparing Programming Languages Part 2 - Memory Management and Concurrency  (10 mins)
# ---	March 26 -  Comparing Programming Languages Part 1 - Compilers and Type-Systems  (10 mins)
# ---	Compilers: Innovation from the Bottom-Up—Viral Shah & Keno Fischer on TechLifeSkills w/Tanmay Ep. 20
# ---	On Mathematical Maturity (1) Thomas Garrity - YouTube
# ---	Fast Inverse Square Root — A Quake III Algorithm - YouTube
# ---	Operating System Full Course | Operating System Tutorials for Beginners - YouTube
# ---	Assembler #1 Hello-World zur Maschinensprache
# ---	Assembler #2 Wie speichert man eine Konsoleneingabe?
# ---	Operating Systems: Crash Course Computer Science #18 - YouTube
# ---	Operating System Full Course || Operating System for IT Support - YouTube
# ---	https://www.youtube.com/watch?v=jAGIuobLp60
# ---	https://www.youtube.com/watch?v=LFKZLXVO-Dg
# ---	Neural Network from scratch-part 1 | AI Summer
# ---	https://contentlab.io/c-neural-network-in-a-weekend/
# ---	That unbelievable function that can compute EVERYTHING! An Adventure in Discrete Mathematics - YouTube
# ---	We're Building Computers Wrong - YouTube
# ---	https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-004-computation-structures-spring-2017/c10/
# ---	Turingmaschinen - YouTube
# ---	https://github.com/0xAX/asm
# ---	https://cs.lmu.edu/~ray/notes/nasmtutorial/
# ---	1000 Linux Questions & Answers
# ---	https://booking.ai/theres-more-to-experimentation-than-a-b-223fba846876
# ---	http://www.norvig.com/design-patterns/design-patterns.pdf
# ---	So you want to write an interpreter?
# ---	WebAssembly (WASM) verdrängt Docker?! // deutsch
# ---	https://fuchsia.dev/
# ---	https://medium.com/@brianwill/unix-userland-should-be-replaced-5605fe47cac0
# ---	https://medium.com/@brianwill
# ---	https://pilvinen.github.io/notes-on-why-oop-is-bad-and-how-to-solve-it.html
# ---	https://developer.ibm.com/articles/l-gas-nasm/
# ---	Games RL
# ---	What Happens when I Press a Key?
# ---	AES
# ---	OOP
# ---	Why Rust?
# ---	Railroad
# ---	Was sind Monaden? Funktionale Programmierung
# ---	Why would a python programmer learn rust when there are no jobs in it
# ---	https://github.com/gnulinuxpro/infra/
# ---	RabbitMQ Crash Course
# ---	RabbitMQ Introduction | RabbitMQ Tutorial for Beginners | What is RabbitMQ | RabbitMQ Message Broker
# ---	Configuration as Code in Bamboo - Atlassian Summit Europe 2017
# ---	https://www.freecodecamp.org/news/the-docker-handbook/
# ---	Microservices Architecture Design Patterns | 10 Design Principles | 26 Design Patterns 🔥 🔥 🔥 - YouTube
# ---	10 Architecture Patterns Used In Enterprise Software Development Today - YouTube
# ---	10 Design Patterns Explained in 10 Minutes - YouTube
# ---	RabbitMQ Crash Course - YouTube
# ---	Microservice APIs: With examples in Python (MEAP v10)
# ---	RabbitMQ in 5 minutes
# ---	https://www.youtube.com/watch?v=fl_AelgaWKE
# ---	Learn Docker in 7 Easy Steps - Full Beginner's Tutorial - YouTube
# ---	The 50 Most Popular Linux & Terminal Commands - Full Course for Beginners - YouTube
# ---	Docker Tutorial #1 - Warum ihr Docker braucht! - YouTube
# ---	Cloud Computing. Concepts and Technologies.epub
# ---	Cloud Native Python.pdf
# ---	Generic Pipelines Using Docker. The DevOps Guide to Building Reusable, Platform Agnostic CI_CD
# ---	Hands-On RESTful Python Web Services.pdf
# ---	Practical Web Scraping for Data Scientists.pdf
# ---	Python и DevOps.pdf
# ---	Python. Непрерывная интеграция и доставка.pdf
# ---	RabbitMQ Essentials.pdf
# ---	RabbitMQ in Depth.pdf
# ---	Web API Development with Python. A Beginner's Guide using Flask and FastAPI.pdf
# ---	Облачные архитектуры разработка устойчивых и экономичных облачных приложений.pdf
# ---	От монолита к микросервисам.pdf
# ---	Networks, Crowds, and Markets: Reasoning about a Highly Connected World.pdf
# ---	Learning at Lambert Labs
# ---	LaTeX 2e for class and package writers.pdf
# ---	LaTeX Users Guide and Reference Manual. A Document Preparation System (Lamport).pdf
# ---	TeX by Topic, A TeXnician's Reference.pdf
# ---	The TeXbook.pdf
# ---	.
# ---	Algorithms for Decision Making
# ---	Angewandte Mathematik 1 mit MATLAB und Julia.pdf
# ---	Angewandte Mathematik 2 mit MATLAB und Julia.pdf
# ---	Beginning Julia Programming for Engineers and Scientists.pdf
# ---	Efektywny Python 59 sposobow na lepszy kod.pdf
# ---	Foundation Dynamic Web Pages with Python.pdf
# ---	Getting Started with Julia Programming.pdf
# ---	Hands-on Design Patterns and Best Practices with Julia.pdf
# ---	https://julia.quantecon.org/intro.html
# ---	https://pnp.mathematik.uni-stuttgart.de/igt/eiserm/lehre/Topolywood/
# ---	Open Data Structures (in Java).pdf
# ---	Seven Languages in Seven Weeks.pdf
# ---	Seven More Languages in Seven Weeks.pdf
# ---	Understanding Cryptography.pdf
# ---	ГЕОМЕТРИЯ В КАРТИНКАХ.pdf
# ---	Коротко о языке программирования Julia.pdf
# ---	Шпаргалки для начинающего верстальщика HTML CSS.pdf
# ---	ЯЗЫК ПРОГРАММИРОВАНИЯ МАТЕМАТИЧЕСКИХ ВЫЧИСЛЕНИЙ JULIA. БАЗОВОЕ РУКОВОДСТВО.pdf
# ---	https://exercism.org/tracks/scala
# ---	https://exercism.org/tracks/go
# ---	ACOUSTIC PARAMETERS VERSUS PHONETIC FEATURES IN ASR.pdf
# ---	https://exercism.org/tracks/scheme
# ---	https://exercism.org/tracks/fortran
# ---	Modern Fortran.pdf
# ---	Das Gehirn
# ---	Kognitive Neurowissenschaften
# ---	Neurobiologie
# ---	Neuromythologie
# ---	Psycholinguistik - Neurolinguistik
# ---	Мозг, познание, разум I
# ---	Мозг, познание, разум II
# ---	Fascism: A Very Short Introduction
# ---	Free Will: A Very Short Introduction
# ---	Freedom Regained: The Possibility of Free Will
# ---	Gehirn und Geist Spezial
# ---	German Philosophy: A Very Short Introduction (Elsie)
# ---	History: A Very Short Introduction (Elsie)
# ---	Kant & Co. im Interview
# ---	Motherland: a philosophical history of Russia
# ---	The Palgrave Handbook of the Psychology of Sexuality and Gender.pdf
# ---	The Philosophy of Sex.pdf
# ---	Кухня Робинсона.djvu
# ---	Один на один с природой.pdf
# ---	Проста фізика.epub
# ---	Lehrbuch Kognitive Neurowissenschaften
# ---	Мозг, познание, разум
# ---	Философия DevOps.pdf
# ---	Осваиваем Kubernetes.pdf
# ---	Социальная инженерия и социальные хакеры.pdf
# ---	Субстанция мышления.pdf
# ---	МАТЕМАТИЧЕСКАЯ ЛОГИКА И ТЕОРИЯ АЛГОРИТМОВ.pdf
# ---	Программирование. Python. C++. Часть 1.djvu
# ---	Программирование. Python. C++. Часть 2.djvu
# ---	Программирование. Python. C++. Часть 3.djvu
# ---	Программирование. Python. C++. Часть 4.djvu
# ---	50 Shades of JavaScript.pdf
# ---	Aprendendo JavaScript.pdf
# ---	Beginning Topology
# ---	ES6 и не только.pdf
# ---	GNU Linux programación de sistemas.pdf
# ---	Hands-On System Programming with Linux.pdf
# ---	Introduction to Topology.pdf
# ---	Intuitive Concepts in Elementary Topology.pdf
# ---	JavaScript Succinctly.pdf
# ---	JavaScript для детей.pdf
# ---	JavaScript для профессиональных веб-разработчиков.pdf
# ---	JavaScript на примерах.pdf
# ---	JavaScript с нуля 2021.pdf
# ---	JavaScript. The Definitive Guide.pdf
# ---	JavaScript. Полное руководство.pdf
# ---	Professional JavaScript for Web Developers, 4th Edition.pdf
# ---	Programming Rust. Fast, Safe Systems Development.pdf
# ---	R in a Nutshell.pdf
# ---	Systems Programming in Unix/Linux.pdf
# ---	The Art of R Programming.pdf
# ---	The JavaScript Way.pdf
# ---	Topologie 2020
# ---	Topology Illustrated
# ---	Topology: A Very Short Introduction (Elsie)
# ---	TypeScript ES.pdf
# ---	Understanding Topology. A Practical Introduction.pdf
# ---	WebAssembly в действии.pdf
# ---	Искусство WebAssembly.pdf
# ---	Математика в огне.pdf
# ---	Наглядный CSS.pdf
# ---	Отзывчивый дизайн на HTML5 и CSS3 для любых устройств 3е.pdf
# ---	Познакомьтесь, JavaScript 2е (Симпсон).pdf
# ---	Программирование на Rust. Официальный гайд от команды разработчиков.pdf
# ---	Программируй & типизируй.pdf
# ---	Разработка веб-приложений.pdf
# ---	ТОПОЛОГІЯ МНОГОВИДІВ.pdf
# ---	https://exercism.org/tracks/r
# ---	https://exercism.org/tracks/javascript
# ---	Numerical Methods in Science and Engineering.pdf
# ---	Rediscovering JavaScript.pdf
# ---	Cassandra. The Definitive Guide.pdf
# ---	Graph Databases.pdf
# ---	Hadoop. The Definitive Guide.pdf
# ---	High Performance Spark.pdf
# ---	Learning Spark.pdf
# ---	Practical Machine Learning with H2O.pdf
# ---	Time Series Databases.pdf
# ---	An introduction to language processing with Perl and Prolog
# ---	An Overview of Lexical Semantics.pdf
# ---	Analytical Methods for Interpretable Ultradense Word Embeddings.pdf
# ---	Beginning Perl Programming.pdf
# ---	Beginning Rust.pdf
# ---	Kotlin в действии.pdf
# ---	Learning Perl the Hard Way.pdf
# ---	https://exercism.org/tracks/prolog
# ---	https://exercism.org/tracks/perl5
# ---	https://exercism.org/tracks/rust
# ---	Android Slides.pdf
# ---	Kotlin for Android App Development.pdf
# ---	Practical Android. 14 Complete Projects.pdf
# ---	https://exercism.org/tracks/lua
# ---	https://exercism.org/tracks/ocaml
# ---	https://exercism.org/tracks/wasm
# ---	https://exercism.org/tracks/kotlin
# ---	https://exercism.org/tracks/haskell
# ---	https://exercism.org/tracks/racket
# ---	https://exercism.org/tracks/elixir
# ---	https://exercism.org/tracks/erlang
# 21	An Introduction to Information Retrieval
# 10	An Introduction to Language (Fromkin)
# 26	CRC Handbook of NLP (2010)
# 11	A Practical Introduction to Phonetics
# 10,A	Acoustic Phonetics
# 39	Articulatory Phonetics
# 25	Cambridge Handbook of Formal Semantics
# 36,A	Comprehensive Articulatory Phonetics
# 9	Dictionary of Linguistics and Phonetics
# 11	Elements of Acoustical Phonetics
# 7	Elements of Formal Semantics
# 1	Embedding of Semantic Predications.pdf
# 103	Linguistic Fundamentals for NLP
# 1	A Novel Method of Extracting Topological Features from Word Embeddings.pdf
# 87	Essentials of Linguistics (Anderson)
# 1	go through https://cs-k.it/master/lecture/Grundlagen-der-Automatischen-Spracherkennung.html
# 13,iii	Head First Data Analysis.pdf
# 15	Introduction to Artificial Intelligence.pdf
# 20,A	Introduction to Language (Yule)
# 1	Langage naturel (résumé).pdf
# 10	Mathematical Linguistics
# 21.A2	Mathematics of Language
# 1		АВТОМАТИЧЕСКАЯ ОБРАБОТКА ТЕКСТОВ. ЗАДАЧИ, ПОДХОДЫ,  РЕСУРСЫ.pdf
# 9		NLP06) Natural Language Processing with PyTorch.pdf
# 9		NLP06) Знакомство с PyTorch
# 22		Oxford Handbook of CL and NLP (2010)
# 38,A		NLP20) Oxford Handbook of Computational Linguistics.pdf
# 42		NLP25) Speech and Audio Signal Processing. Processing and Perception of Speech and Music.pdf
# 18,A4		NLP17) Text-to-Speech Synthesis.pdf
# 15		NLP16) Automatic Speech Recognition - A Deep Learning Approach.pdf
# 22		NLP21) Handbook of Computational Linguistics and Natural Language Processing.pdf
# 13		NLP22) Spoken Language Processing.pdf
# 12,A		NLP19) Applied Text Analysis with Python.pdf
# 9		NLP23) Text Mining with R. a Tidy Approach.pdf
# 13		Psycholinguistics - The Key Concepts
# 29		Routledge Handbook of Semantics
# 13		Using Praat for Linguistic Research (Styler)
# 11		NLP11) Deep Learning in Natural Language Processing
# 9		NLP24) Text Mining in Practice with R.pdf
# 16		NLP05) Foundations of Statistical Natural Language Processing
# 11		The Sounds of the World's Languages
# 1		Document Image Analysis. Current Trends and Challenges in Graphics Recognition.pdf
# 1		https://github.com/doc-analysis
# 1		1) Rich feature hierarchies for accurate object detection and semantic segmentation.pdf
# 1		2) Fast R-CNN.pdf
# 1		3) Fast R-CNN Slides.pdf
# 1		4) Faster R-CNN. Towards Real-Time Object Detection with Region Proposal Networks.pdf
# 1		5) Mask R-CNN.pdf
# 1		Mask RCNN - How it Works - Intuition Tutorial | OpenCV Python | Computer Vision 2020
# 1		An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale
# 1		https://learnopencv.com/create-snapchat-instagram-filters-using-mediapipe/
# 1		https://learnopencv.com/deep-learning-based-object-detection-using-yolov3-with-opencv-python-c/
# 1		https://www.learnopencv.com/wp-content/uploads/2020/05/Computer-Vision-Resources.pdf?ck_subscriber_id=1680684172
# 1		Mask RCNN - How it Works - Intuition Tutorial | OpenCV Python | Computer Vision 2020
# 1		Vision Transformer in PyTorch
# 14		Advanced Computer Vision with Python - Full Course
# 12		Artificial Intelligence Programming with Python.pdf
# 1		https://omdena.com/blog/computer-vision-projects-github/
# 1		Lecture 11 | Detection and Segmentation
# 1		DETR: End-to-End Object Detection with Transformers (Paper Explained)
# 1		https://learnopencv.com/deep-learning-based-text-recognition-ocr-using-tesseract-and-opencv/
# 1		https://learnopencv.com/multi-person-pose-estimation-in-opencv-using-openpose/
# 1		https://homepages.inf.ed.ac.uk/rbf/HIPR2/guidecon.htm
# 1		Lecture 11 | Detection and Segmentation
# 1		An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale
# 1		Vision Transformer in PyTorch
# 1		https://www.width.ai/post/facial-detection-and-recognition-with-dlib
# 1		https://learnopencv.com/convolutional-neural-network-based-image-colorization-using-opencv/
# 1		https://github.com/spmallick/learnopencv/blob/master/README.md?ck_subscriber_id=1680684172
# 1		Fast R-CNN Slides.pdf
# 1		DETR: End-to-End Object Detection with Transformers (Paper Explained)
# 321		Computer Vision. A Reference Guide.pdf
# 31		Wikipedia Computer Vision
# 8		Hands-On Computer Vision with Julia .pdf
# 42		Convolutional Neural Networks (Course 4 of the Deep Learning Specialization)
# 12		Mastering Computer Vision with TensorFlow 2.x.pdf
# 21		OCR with OpenCV, Tesseract, and Python.pdf
# 12		Practical Machine Learning for Computer Vision.pdf
# 10,A		Learning OpenCV 4 Computer Vision with Python 3.pdf
# 16		Lecture Collection | Convolutional Neural Networks for Visual Recognition (Spring 2017)
# 20		OCR with OpenCV, Tesseract, and Python - Intro to OCR.pdf
# 10		Deep Learning for Vision Systems.pdf
# 11		Deep Learning in Computer Vision.pdf
# 13		Domain Adaptation in Computer Vision with Deep Learning.pdf
# 9,6,2007		Handbook of Image Processing and Computer Vision. Volume 1. From Energy to Image.pdf
# 5		Java и OpenCV.pdf
# 10		PyTorch Computer Vision Cookbook.pdf
# 12		TensorFlow 2.0 Computer Vision Cookbook.pdf
# 10		Биологическое и компьютерное зрение.pdf
# -	nand2tetris 9
# -	nand2tetris 10
# -	nand2tetris 11
# 7	Practical Docker with Python.pdf
# 10	The Docker Handbook
# 12	Descomplicando o Docker.pdf
# 13	Mastering Docker
# 15	BIOS.djvu
# 22	Learn Docker in a Month of Lunches
# 9	Docker Succinctly.pdf
# 10	Desconstruindo a Web.pdf
# 13	Docker in Action
# 37	Aprendizaje Docker.pdf
# 16,B	Docker на практике.pdf (Hank and (Elsie))
# 16,C	Docker in Practice
# 17,C	Docker Deep Dive.pdf
# 25,A	Docker para Desenvolvedores.pdf
# 10	Scrum Shortcuts without Cutting Corners.pdf
# 6	The GNU Make Book.pdf
# 5	A Course in Formal Languages, Automata, and Groups (Chiswell)
# 13	Sistemas computacionales.pdf
# 15	https://justinmeiners.github.io/lc3-vm/
# 16	Category Theory for Computing Science
# 16,F	GNU Make Manual
# 20,F	Rust Book
# 21	Eloquent JavaScript
# 13,B	Introduction to Logic Circuits and Logic Design with VHDL.pdf
# 6,B	Grundkurs Codierung Verschlüsselung, Kompression und Fehlerbeseitigung.pdf
# 	Linux Kernel in a Nutshell.pdf
# 	Low-Level Programming
# 	Web Development for Beginners.pdf
# 	Компиляторы.pdf
# 5	Ensamblador.pdf
# 6	Kryptologie Eine Einführung in die Wissenschaft vom Verschlüsseln, Verbergen und Verheimlichen.pdf
# 6	Scientific Computing. A Historical Perspective.pdf
# 8	2024	Bases de datos.pdf
# 8	How to Design, Build, & Program Your Own Working Computer System.pdf
# 9	Cryptography Algorithms.pdf
# 9	Fundamentos físicos de la informática.pdf
# 10	Exploring the Early Digital.pdf
# 10	How Cybersecurity Really Works.pdf
# 10	PostgreSQL. Основы языка SQL.pdf
# 10	Programming with POSIX threads.pdf
# 12	Beginning PostgresQL on the Cloud.pdf
# 12	Scala Book
# 16	Real-World Cryptography.pdf
# 14,B	An Introduction to Formal Languages and Automata
# 22,A	Основы технологий баз данных
# 24,A	Digital Computer Electronics
# 25,A9	Прикладная криптография.pdf
# 23	Happy Learn Haskell
# 0-14	Five Lines of Code
# 0-40	Haskell Report
# 13,B	Assembly Language Step-by-Step. Programming with Linux
# 7,A	How to Build a Working Digital Computer.pdf
# 9,B	Essentials of Programming Languages
# 	Intro to Automata Theory, Languages, and Computation (Hopcroft)
# 	Lenguaje ensamblador y programación para IBM PC y compatibles.pdf
# 	Mastering MySQL for Web. A Beginner's Guide.pdf
# 	Modern Parallel Programming with C++ and Assembly Language.pdf
# 	Touch of Class.pdf
# 	Tour of Scala
# 	UNIX Network Programming, Volume 1. The Sockets Networking API.pdf
# 	Web Security for Developers.pdf
# 	Yet Another Haskell Tutorial
# 	Алгебраические основы криптографии.pdf
# 6	Scalability Patterns.pdf
# 11	Algorithms, Languages, Automata, and Compilers
# 11	Refactoring at Scale.pdf
# 12	The Art of Assembly Language Programming
# 12	Програмування мовою асемблера. Навчальний посібник.pdf
# 13	Scalability Rules.pdf
# 14	Secure by Design.pdf
# 18	The Annotated Turing
# 16,E	The Art of 64-Bit Assembly
# 24	GNU Emacs Manual
# 0-16,A	Профессиональное программирование на ассемблере x64 с расширениями.pdf
# 0-43,A	Программирование на ассемблере х64. От начального уровня до профессионального.pdf
# 11,E	Code Reading. The Open Source Perspective.pdf
# 	Алгоритмы и модели вычисления.pdf
# 	Изучение сложных систем с помощью Python.pdf
# 	Математические основы информатики.pdf
# 3	Сетевые технологии. Основы веб дизайна.pdf
# 18	Assembler Lernen - Tutorial Deutsch
# 8,A	Fundamentals of Computer Architecture and Design.pdf
# 14,C	1400 задач по программированию.pdf
# 11,A	Introduction to Compiler Design.pdf
# 9	Kubernetes Succinctly.pdf
# 12	Cloud Native DevOps with Kubernetes (2019).pdf
# 14	Kubernetes – An Enterprise Guide.pdf
# 16	Cloud Native DevOps with Kubernetes.pdf
# 18	Kubernetes лучшие практики.pdf
# 22,D	Learn Kubernetes in a Month of Lunches.pdf
# 25,A	Kubernetes Patterns.pdf
# 6	Networking and Kubernetes.pdf
# 9	Diving Deep into Kubernetes Networking.pdf
# 97	97 Etudes RU.pdf
# 13,B	An Introduction to GCC. For the GNU Compilers GCC and G++.pdf
# 9	Learn Helm.pdf
# 8,B	Learning Helm.pdf
# 	Linux в действии.pdf
# 9	Seriously Good Software.pdf
# 11	Scala Programming Projects.pdf
# 12	Scala Design Patterns.pdf
# 11	Mastering RabbitMQ.pdf
# 10,A	Betriebssysteme (zweisprachig)
# 9,A	Introduction to the Theory of Formal Languages and Automata (Levelt)
# 8,A	Learning Algorithms Through Programming and Puzzle Solving.pdf
# 11	Грокаем алгоритмы
# 12	Объектно-ориентированный подход.pdf
# 13	Real-Time Operating Systems Book 1. The Theory.pdf
# 12	Cloud Computing (Ruparelia)
# 13	Cloud Computing Theory and Practice
# 8,D	Implementing Programming Languages. An Introduction to Compilers and Interpreters.pdf
# 14	О криптографии всерьез.pdf
# 1-20	Handbuch für Softwareentwickler
# 35,A4	Алгоритмы. Построение и анализ.pdf
# 14	Foundations of Computer Science
# 10,E	Arquitectura de computadores.pdf
# 13,B	Introduction to the Design and Analysis of Algorithms.pdf
# 16	Алгоритмы для начинающих.pdf
# 23	https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/video_galleries/lecture-videos/
# 60	Linux API. Исчерпывающее руководство.pdf
# 6	Algorithmen und Datenstrukturen (Sedgewick 2014).pdf
# 12,B	Compilers (Aho et al. 2E)
# 16	Linguaggi di Programmazione.pdf
# 17	Algoritmi. Lo spirito dell'informatica.pdf
# 32,B	Types and Programming Languages.pdf
# 14,C	Algorytmy, struktury danych i techniki programowania.pdf
# 29	Operating System - YouTube
# 5	Structure and Interpretation of Computer Programs
# 18	Programming Languages. Principles and Paradigms (Noonan and Tucker)
# 23	CS 377 Spring '14: Operating Systems - YouTube
# 10	Compiladores y interpretes.pdf
# 12,B	Compiladores 2e.pdf
# 0-37,F	Compilers
# 10,A	Computer Systems (Elahi).pdf
# 	Inside the Machine - An Illustrated Guide.pdf
# 24	Fundamentals of Software Architecture
# 11,C	Electronic Digital System Fundamentals.pdf
# 8	Графовые алгоритмы.pdf
# 8	Processor Microarchitecture
# 7,B	Вычислительные системы и ассемблер.djvu
# 12	Введение в рекурсивное программирование.pdf
# 9,C	Structured Computer Organization
# 26	Человеческий фактор успешные проекты и команды.pdf
# 17	https://exercism.org/tracks/x86-64-assembly/
# 21,C	Arquitetura e organização de computadores (Stallings).pdf
# 10	Advanced Topics in Types and Programming Languages.pdf
# 	PyTorch Recipes.pdf
# 	Глубокое обучение
# 	PyTorch Deep Learning Hands-On.pdf
# 	Foundations Of Data Science (2020).pdf
# 	Hands-On Machine Learning with Scikit-Learn and TensorFlow
# 	Deep Learning with TensorFlow 2 and Keras
# 	Deep Learning. From Basics to Practice. Volume 1 (Glassner 2022).pdf
# 	Deep Learning. From Basics to Practice. Volume 2 (Glassner 2022).pdf
# 	Introduction to Machine Learning (Alpaydin 4e)
# 	Learning Deep Learning.pdf
# 	Основы искусственного интеллекта в примерах на Python.pdf
# 	The TensorFlow Workshop.pdf
# 	Programming Machine Learning. From Coding to Deep Learning.pdf
# 	Applied Deep Learning with TensorFlow 2.pdf
# 	Artificial Intelligence with Python. Your complete guide to building intelligent apps using Python 3.x and TensorFlow 2
# 	Machine Learning mit Python
# 	Generative Deep Learning
# 	Deep Learning with TensorFlow 2 and Keras- Regression, ConvNets, GANs, RNNs, NLP, and more with TensorFlow 2
# 	Linear Algebra and Learning from Data.pdf
# 	Deep Learning with PyTorch
# 	Mastering PyTorch.pdf
# 	Deep Learning with Python. Learn Best Practices of Deep Learning Models with PyTorch.pdf
# 	AI and Machine Learning for Coders.pdf
# 	PyTorch Artificial Intelligence Fundamentals.pdf
# 	The Deep Learning with PyTorch Workshop.pdf
# 	Inside Deep Learning.pdf
# 	https://github.com/yunjey/pytorch-tutorial
# 	TensorFlow 2 Pocket Reference: Building and Deploying Machine Learning Models
# 	Developing Analytic Talent.pdf
# 	Machine Learning Bookcamp.pdf
# 	Machine Learning (Flach)
# 	Machine Learning Refined.pdf
# 	Machine Learning. An Algorithmic Perspective.pdf
# 	scikit-learn Cookbook.pdf
# 	An Overview of Statistical Learning Theory
# 	Deep Learning Approaches for  Low-Resource Natural Language Processing.pdf
# 	Statistical Learning Theory Notes (Liang)
# 	Learning from Data
# 	Machine Learning - An Algorithmic Perspective
# 	Introduction to Applied Linear Algebra Julia Companion
# 	Statistics with Julia
# 	Julia for Data Science
# 	Flux.jl Docs
# 	Artificial Intelligence, Machine Learning, and Deep Learning (Campesato)
# 	Practical Deep Learning for Cloud, Mobile, & Edge
# 	Deep Learning (Aggarwal)
# 	Understanding Machine Learning
# 	Foundations of Machine Learning
# 	Foundaions of Machine Learning
# 	Introduction to Machine Learning (Alpaydin)
# 	Deep Learning in Natural Language Processing
# 	Data Science with Julia
# 	Machine Learning: A Bayesian and Optimization Perspective
# 	Linear Algebra and Optimization for Machine Learning: A Textbook
# 	Alebra, Topology, Differential Calculus, and Optimization Theory for Computer Science and Machine Learning
# 	Deep Learning. A Visual Approach (Glassner).pdf
# 	Getting Started with Artificial Intelligence.pdf
# 	Inteligencia artificial.pdf
# 	Probabilistic Machine Learning.pdf
# 	Why Flux? The Elegant Julia Machine Learning Library
# 	Intro to Applied Linear Algebra.pdf
# 	Probabilistic Machine Learning: An Introduction
# 	Machine Learning: A Probabilistic Perspective
# 	Python Machine Learning Blueprints.pdf
# 	Python и наука о данных.pdf
# 	Data Science. Concepts and Practice.pdf
# 	Data Science at the Command Line.pdf
# 	Doing Data Science.pdf
# 	DL Technical Intro
# 	Антология машинного обучения. Важнейшие исследования в области ИИ.epub
# 	Крупномасштабное машинное обучение вместе с Python.pdf
# 	Building Machine Learning Pipelines.pdf
# 	Data science для карьериста.pdf
# 	Data Science Handbook (Shan et al.)
# 	The Data Science Handbook (Cady)
# 	Pragmatic AI
# 	Deep Learning (Goodfellow et al., 2016)
# 	Elements of Statistical Learning
# 	Machine Learning (Alpaydin 2020)
# 	Algorithms for Data Science.pdf
# 	Handbook of Data Intensive Computing
# 	Data Mining (Aggarwal)
# 	Understanding Complex Datasets
# 	Spark: The Definitive Guide (Chambers & Zaharia)
# 	Using MPI: Portable Parallel Programming with the Message-Passing Interface by (Gropp, Lusk, and Skjellum)
# 	Programming Massively Parallel Processors (Kirk and Hwu)
# 	CUDA for Engineers (Storti & Yurtoglu)
# 	Fundamentals of Machine Learning for Predictive Data Analysis.pdf
# 	Probabilistic Machine Learning. Advanced Topics - Supplementary Materials.pdf
# 	Probabilistic Machine Learning. Advanced Topics.pdf
# 	The Kaggle Book.pdf
# 	Data Clustering
# 	Practical Machine Learning. A New Look at Anomaly Detection.pdf
# 	Practical Machine Learning. Innovations in Recommendation.pdf
# 	Анализ данных в науке и технике.pdf
# 	Как вытащить из данных максимум. Навыки аналитики для неспециалистов.pdf
# 	Разработка беспилотных транспортных средств.pdf
# 	Глубокое обучение с подкреплением на Python. OpenAI Gym и TensorFlow для профи.pdf
# 	Глубокое обучение с подкреплением.pdf
# 	Deep Reinforcement Learning. Das umfassende Praxis-Handbuch
# 	Алгоритмы обучения с подкреплением на Python.pdf
# 	Deep Learning for Robot Perception and Cognition.pdf
# 	R Deep Learning. Essentials.pdf
# 	Scaling Up Machine Learning. Parallel and Distributed Approaches.pdf
# 	Машинное обучение: алгоритмы для бизнеса.pdf
# 	Machine Learning and Data Science Blueprints for Finance.pdf
# 	Artificial Intelligence (Norvig)
# 	Linear Algebra and Learning from Data
# 	Aprender Noruego
# 	> 100 frases positivas + cumplidos - Noruego + Español - (Hablante nativo)
# 	Imparare 200 frasi in Cinese
# 2023	Word Translation Graph Project
# 	Modismos diversos (borrador)
# 	Database of Figurative Language
# 	Argot
# 2024	Wikiquote
# 	Parallel Translations Projects
# 	Proverbs Project
# 	https://zh.wikipedia.org/wiki/深度学习
# 	https://zh.wikipedia.org/wiki/计算机科学
# 	> Aprender Idiomas con Chris
# 	> Assimil Ancient Greek
# 	> Assimil HI
# 	> Assimil HR
# 	> Assimil PL
# 	> Assimil ZH
# 	> Build Your Arabic Vocabulary
# 	> https://archive.org/details/AssimilArabicWithEase
# 	> Modismos diversos (borrador)
# 	>Assimil NL
# 	200 frases - Télugu - Español
