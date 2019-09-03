# RedName
Very simple python program that takes a file of line separated names as input,  
checks each names availability as a username on reddit using reddits username  
API and outputs two files, a list of those from names.txt which are available  
and a list of those which are not.  

## Usage
To use this tool, just list all the names you want to check on separate lines  
in the names.txt file, then double click "run.bat".

## Note
I slapped this together very quickly and before I even tried to find issues I  
noticed a few. For example, there is no check for invalid names etc., anything  
that isn't a perfectly valid reddit username that is or is not available will  
be completely ignored by the programs output.
