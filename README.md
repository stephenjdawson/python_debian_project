# python_debian_project

# Start Time: 1:00 Pm April 02 2021
# Requirements --------------------------------------------------------------------
Develop a Python command line tool that takes the architecture (amd64, arm64, mips etc.) as an argument and downloads the compressed Contents file associated with it from a Debian mirror.
The program should parse the file and output the statistics of the top 10 packages that have the most files associated with them.

An example output could be:

./package_statistics.py amd64

1. <package name 1>         <number of files> 2. <package name 2>         <number of files> ......

10. <package name 10>         <number of files>

You can use the following Debian mirror

http://ftp.uk.debian.org/debian/dists/stable/main/. 

Please do try to follow Python's best practices in your solution. 
Hint: there are tools that can help you verify your code is compliant. In-line comments are appreciated.

It will be good if the code is accompanied by a 1-page report of the work that you have done including the time you actually spent working on it. 

# Step 1: Research -------------------------------------------------------------------------
# Downloaded Debian Contents File to look at the contents
# There are Debian content files e.g. Contents-amd64, and micro Debian e.g. Contents-udeb-arm64
# These files are compressed in a .gz format and must be unzipped before parsing. 

"Contents" indices
The files dists/$DIST/$COMP/Contents-$SARCH.gz (and dists/$DIST/$COMP/Contents-udeb-$SARCH.gz for udebs) are so called Contents indices. 
The variable $SARCH means either a binary architecture or the pseudo-architecture "source" that represents source packages. 
They are optional indices describing which files can be found in which packages. 
Prior to Debian wheezy, the files were located below "dists/$DIST/Contents-$SARCH.gz".
Contents indices begin with zero or more lines of free form text followed by a table mapping filenames to one or more packages. 
The table SHALL have two columns, separated by one or more spaces. 

The first row of the table SHOULD have the columns "FILE" and "LOCATION", 
the following rows shall have the following columns:

A filename relative to the root directory, without leading .
A list of qualified package names, separated by comma. 
A qualified package name has the form [[$AREA/]$SECTION/]$NAME, 
where $AREA is the archive area, $SECTION the package section, 
and $NAME the name of the package. 
Inclusion of the area in the name should be considered deprecated.

Clients should ignore lines not conforming to this scheme. 
Clients should correctly handle file names containing white space characters 
(possibly taking advantage of the fact that package names cannot include white space characters).

# 1: Need to parse second row to find how many packages
# Format is Section/Package
# As parsing, add counts to each package for how many rows
# Number of Rows for each package type is = number of files. 
# Packages can span multiple sections. 
# 2: Output top 10 largest packages and their files as described. 
# 3: Make sure to create tests for the code (especially for things like white space and $Area (deprecated))



