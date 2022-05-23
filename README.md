# sample-trust-schema

### Set up antlr-4 (for linux)

0. Pre-requisite: Java

1. Download
```
$ cd /usr/local/lib
$ curl -O https://www.antlr.org/download/antlr-4.9-complete.jar
```
Or just download in browser from website:
    [https://www.antlr.org/download.html](https://www.antlr.org/download.html)
and put it somewhere rational like `/usr/local/lib`.

2. Add `antlr-4.9-complete.jar` to your `CLASSPATH`:
```
$ export CLASSPATH=".:/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH"
```

3. (optional) Create aliases for the ANTLR Tool, and `TestRig`.
```
$ alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.Tool'

$ alias grun='java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.gui.TestRig'
```

### Run this project

1. execute generate.sh file . It will take the grammer file, TSP.g4 as input and generate the lexer and perser files.
```
./generate.sh
```

2. Run the driver python program and add a sample policy file as argument.

```
python3 TSP.py <input_file> <output_file>
```


### Evaluation

0. Pre-requisite: NLTK ; To install NLTK, use the following command:
    ```
    >>> import nltk
    >>> nltk.download()
    ```
    
1. To generate the repeated schema (where just one component changes in each publication), run the following program:
    ```
    python3 schema_generator.py
    ```
    It will: 
        a. create all the necessary schemas, 
        b. compile them using Van's schemacompile, Simplified version and No compression version
        c. Write all the evaluation metrics (e.g., number of publications, s chema size etc.) in "result.csv file.
        
 2. In similar way, to generate the repeated schema (where all the components will be distinct, run the following program:
     ```
    python3 non_repeated.py
    ```
