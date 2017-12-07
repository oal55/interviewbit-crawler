# README

Here are the python scripts I used to fetch all my solutions on [interviewbit]
and store them locally with a well-structured manner.

[interviewbit]: https://www.interviewbit.com

## Setup

You can either clone the repository with 
`git clone https://github.com/norubai/interviewbit-crawler.git`, or download
all the scripts \& put them in the same directory.


Scripts are written in python 3.6 syntax. If you don't have a python 3.6 
interpreter and want to use the scripts, you can either:
1. Download python 3.6(recommended, up-to-date is the new sexy)
    * For debian distros, you may want to take a look at [here][linux_link]
    * For macintosh machines, [macpython][macos_link] 
    * For windows, refer to [using python on windows][windows_link] 
2. Modify the source code so that it works with the version you have
installed.
    * If you have a python3.5 interpreter, this should be a fairly easy task
  for you. If you find \& remove(or modify) all the f-strings(literal string
  interpolations), the scripts should run without any problems.
    * If you have a python2x interpreter, pray to god for strength, patience and
  mental clarity. Nay, It's still not rocket science, but you need to do more
  work in order to get the scripts work for you.

[linux_link]: https://askubuntu.com/a/865569/595315
[macos_link]: https://docs.python.org/3/using/mac.html
[windows_link]: https://docs.python.org/3/using/windows.html

## How to Use

Open `conf-example.py`. Assign your email address and your password to commented
out `USERNAME_VAL` and `PASSWORD_VAL` variables as strings. You need to
change this file's name to conf.py before running `crawl` script.

Now you can run the script, and the output should look something like:


```
Logging into https://www.interviewbit.com/users/sign_in/
Login successful.
Fetching: https://www.interviewbit.com/courses/programming/topics/arrays/
Fetching: https://www.interviewbit.com/courses/programming/topics/math/
Fetching: https://www.interviewbit.com/courses/programming/topics/binary-search/
Fetching: https://www.interviewbit.com/courses/programming/topics/strings/
Fetching: https://www.interviewbit.com/courses/programming/topics/hashing/
Fetching: https://www.interviewbit.com/courses/programming/topics/trees/

Fetching topic:Arrays
	problem: max-distance.cpp                                  ...done
	problem: max-non-negative-subarray.cpp                     ...done
	problem: repeat-and-missing-number-array.cpp               ...done
	problem: largest-number.cpp                                ...done

Fetching topic:Math
	problem: excel-column-title.cpp                            ...done
	problem: palindrome-integer.cpp                            ...done
	problem: sorted-permutation-rank-with-repeats.cpp          ...done
	problem: sum-of-pairwise-hamming-distance.cpp              ...done

Fetching topic:Binary Search
	problem: search-for-a-range.cpp                            ...done
	problem: sorted-insert-position.cpp                        ...done
	problem: matrix-search.cpp                                 ...done

Fetching topic:Strings
	problem: roman-to-integer.cpp                              ...done
	problem: implement-strstr.cpp                              ...done
	problem: multiply-strings.cpp                              ...done
Fetching topic:Hashing
	problem: substring-concatenation.cpp                       ...done
	problem: anagrams.cpp                                      ...done
	problem: diffk-ii.cpp                                      ...done
Fetching topic:Trees
	problem: balanced-binary-tree.cpp                          ...done
	problem: sorted-array-to-balanced-bst.cpp                  ...done
	problem: seats.cpp                                         ...done

Everything's done.
Number of solved problems:20
```

**Note:** Above block is not a real output. It's just there to give you an
idea of how the script's output format looks like. I deleted quite some lines
from the original output so that it could fit here.

Once the script finishes running, you should see an `interviewbit` directory
in the same folder with the `crawl` script. `interviewbit` directory should
have a subdirectory for every topic, and every topic should consist of 
the problems you solved. 

```
interviewbit

    Arrays
        largest-number.cpp
        max-distance.cpp
        max-non-negative-subarray.cpp
        repeat-and-missing-number-array.cpp

    Binary Search
        matrix-search.cpp
        search-for-a-range.cpp
        sorted-insert-position.cpp

    Hashing
        anagrams.cpp
        diffk-ii.cpp
        substring-concatenation.cpp

    Math
        excel-column-title.cpp
        palindrome-integer.cpp
        sorted-permutation-rank-with-repeats.cpp
        sum-of-pairwise-hamming-distance.cpp

    Strings
        implement-strstr.cpp
        multiply-strings.cpp
        roman-to-integer.cpp

    Trees
        balanced-binary-tree.cpp
        seats.cpp
        sorted-array-to-balanced-bst.cpp
```