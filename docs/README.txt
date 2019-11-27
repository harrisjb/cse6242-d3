This readme.txt provides an overview of the Project workspace

==============================================================================
1. DESCRIPTION - A description of the key components of the system
   Note: For each component descripbed below a detailed README.md is provided in
   the accompanying project folder.

   The project is composed of a set of logical units creating a pipeline for development.

   First is the **DOCS** Which provides details on key data elements of the dea-arcos
   dataset establishing a foundation on which to build insights and develop the code
   in downstream activities.

   Next is the **DATA PREP** here additional datasets from Center of Disease Control
   (CDC) and US Census (2010) are extracted from their source systems, prepossessed and
   ingested into the AWS component of the project for further analysis. Additionally
   other aspects of the raw dea-arcos data are cleaned and prepared for creating
   visualizations and simplifying downstream analysis.

   Next **DATA ANALYSIS** The data analysis leverages the outputs from data prep to run
   the analysis. Specifically, Geographically and Temporally Weighted Regression (GTWR).

   Next **WEBSITE WIDGETS** is used to create visualization components (mostly d3.js)
   independent of a specific website or presentation platform.

   Finally, the **WEBSITE** aggregates data from all the components to create a cohesive
   presentation of the findings.


==============================================================================
2. INSTALLATION - How to install and setup the code

   The Code for the project is available on GitHub. In addition to the source
   code the repository also contains documentation and many preprocessed files
   that can be used for further analysis and demos

   0. The Installation has two programming language prerequisites R and Python3.
      For development it is advised that you use an IDE. R Studio and
      PyCharm where used for much of this project.

   1. git clone https://github.com/harrisjb/cse6242-d3.git

   2. cd cse6242-d3

   3. ./data_analysis/packages_install.R # Installs additional required R packages

   4. pip install -r ./website/requirements.txt

   NOTE: This installation guide does not include the Big Data aspects of the
   project which are housed on Amazon Web Services (AWS) and require specific
   knowledge of AWS services including S3, AWS Glue, Athena, EC2, etc.

==============================================================================
3. EXECUTION - How to run a demo on the code

   DATA ANALYSIS
   1. The Data Analysis is best run from R Studio which allows you to see
   	  intermediate results and easily view the plots created to validate the
      consistency of the data under analysis.
   2. File/Open
      ./data_analysis/Temporally_Weighted_Regression_Analysis/OpioidMortality_GTWR analysis.R
      in R Studio
   3. source/Run
   4. Select Plots --> (Arrow to advance to next Plot)
   5. Review "./Mortality Outcome GTWR Model Outputs 2006-2012.csv"

   WEBSITE
   1. cd website
   2. ./run.sh
   3. open web browser to http://127.0.0.1:9000

   DATA PREP
   0. It may be important to note that the data for the Analysis and website
      is preprocessed from dea arcos, cdc, and the 2010 census. we do not provide
      execution description here but each directory has a readme.md with additional
      details.

==============================================================================
4. DEMO VIDEO  - How to install and run the code

   https://www.youtube.com/watch?v=Vg6EZ87eX3o