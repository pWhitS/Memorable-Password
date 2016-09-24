# Memorable-Password
This program generates memorable passwords, similar to the memorable password generator within Mac OSX Keychain application.

## How do I get the program?
- For now, you must clone this repo
```
$ git clone https://github.com/pWhitS/Memorable-Password
```
- Packaging will come in the future...

## But how do I use it?
- Use python (perfereably >v3.0) to run mempwd.py
- Help menu:
```
$ python mempwd.py -h  
usage: mempwd.py [-h] [-o OUTPUT] [-x] [-l] [-s] N  

Memorable Password Generator  
  
positional arguments:  
  N              Number of password characters  
  
optional arguments:  
  -h, --help     show this help message and exit  
  -o OUTPUT      Number of passwords to output (default 10)  
  -x, --exclude  Exclude special characters and uppercase. (Same as -ls)  
  -l             Exclude capitalization, lowercase only.  
  -s             Exclude special characters.  
```  
- Basic usage:  
```  
$ python mempwd.py 12 -o 5 -s
sit544backed
bearS3067siG
Doug758Glory
WrightlayerS
rack9899card
```

## Defaut Word List Statistics
```
Length	 - 	Count
1 	     | 	 52
2 	     | 	 160
3 	     | 	 1420
4 	     | 	 5272
5 	     | 	 10230
6 	     | 	 17706
7 	     | 	 23869
8 	     | 	 29989
9 	     | 	 32403
10 	     | 	 30878
11 	     | 	 26013
12 	     | 	 20462
13 	     | 	 14939
14 	     | 	 9765
15 	     | 	 5925
16 	     | 	 3377
17 	     | 	 1813
18 	     | 	 842
19 	     | 	 428
20 	     | 	 198
21 	     | 	 82
22 	     | 	 41
23 	     | 	 17
24 	     | 	 5
```
