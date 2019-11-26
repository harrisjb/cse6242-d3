1.	DESCRIPTION - Describe the package in a few paragraphs

2.	INSTALLATION - How to install and setup your code
   The Code for the project is available on GitHub. In addition to the source
   code the repository also contains documentation and many preprocessed files
   that can be used for further analysis and demos

   0. The Installation has two programming language prerequisites R and Python3.
      For development it is advised that you also use an IDE. R Studio and
      PyCharm where used for much of this project.
   1. git clone https://github.com/harrisjb/cse6242-d3.git
   2. cd cse6242-d3
   3. ./Data_Analysis/packages_install.R # Installs additional required R packages
   4. pip install -r ./website/requirements.txt

   NOTE: This installation guide does not include the Big Data aspects of the
   project which are housed on Amazon Web Services (AWS) and require specific
   knowledge of AWS services including S3, AWS Glue, Athena, EC2, etc.

3.	EXECUTION - How to run a demo on your code

   DATA ANALYSIS
   1. The Data Analysis is best run from R Studio which allows you to see
   	  intermediate results and easily view the plots created to validate the
      consistency of the data under analysis.
   2. File/Open ./Data_Analysis/OpioidMortality_GTWR analysis.R in R Studio
   3. source/Run
   4. Select Plots --> (Arrow to advance to next Plot)
   5. Review ./Mortality Outcome GTWR Model Outputs 2006-2012.csv

   WEBSITE
   1. cd website
   2. ./run.sh
   3. open web browser to http://127.0.0.1:9000
