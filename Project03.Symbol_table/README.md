## How to build the Scanner/Lexer/Tokenizer

I use Python3 as the runtime for ANTLR, so you'd better make sure that you have all the environments set up. Check [this](https://github.com/antlr/antlr4/blob/master/doc/python-target.md) if you want to use python too.

After you have configured your computer, you may run the commands followed:


```sh
> antlr4 -Dlanguage=Python3 Micro.g4
```

⚠️ It is `Python3` rather than `python3`. **Note** the capitalization issue here

## How to run a single test

I have written the `test_scanner.py` file to check a single file.

```sh
> python test_scanner.py <path/to/your/file.micro>
```

## How to run all tests

```sh
> bash run_all_tests.sh
```
If you see the `ALL PASS!!!`, you did it right : )   🎉🎉🎉