# Mathematics-projects
The given python code helps find out the probability distribution function or probability mass function of a given array of numbers.
A huge sample size of numbers are to be fed into the algorithm. It will classify whether the data is discrete or continuous.
A continuous distribution will have very less occurence of individual elements. Hence a dictionary finds out the occurence of each individual unique entry in the cell.
If the probability of the occurence of a particular number comes out to be >5%, the distribution is said to be discrete. Otherwise continuous.
If the distribution is discrete then probability mass function is compited via dictionary.
If the distribution is continuous then the numbers are rounded off to first decimal place.
Hence, all numbers in the range of 0.1 will be represented by the same pdf.
The product of pdf and length gives the probability. Since pdf is assumed to be constant over a small interval, pdfx0.1 gives the probability of the occurence of numbers in that particular interval.
The probability of the occurence of numbers in that interval can be computed via dictionary. Substitution in above formula will output the pdf.
Here the values at extreme intervals are not correct; an interval less than 0.1 has been rounded off.
To account for these errors scaling up of pdf is done at the ends.
