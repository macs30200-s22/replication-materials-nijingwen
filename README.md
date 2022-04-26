[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6483892.svg)](https://doi.org/10.5281/zenodo.6483892)

# MACS30200_Project: Jingwen Ni
#### RQ: How covid19 impacts on unemployment rate of provinces in China?
#### Hypothesis: Covid19 will promote umemployment rate of provinces in 2020
#### Data source: 
1. National Bureau of Statistics: http://www.stats.gov.cn/ : scraping
2. Harvard: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/MR5IJN : download
                 

##### Introduction:
The goal of the project is to figure out the impact of covid 19 on unemployment rate each province in China. The hypothesis is Covid19 will promote umemployment rate of provinces in 2020. I will use GDP to measure development level, CPI to measure price level, the graduation number university, and the college (Note: college is for students who failed entered the university in China) to measure education level, the death rate and born rate to measure the change of province’s population and residence population, the increase income of first industry, the increase income of second industry, the increase income of third industry as control variables. To measure the impact of covid19, I will use the number of covid19 confirmed, the number of deaths, the number of recoveries of each province in 2020 to as my dependent variable.

The code is written in Python 3.9.7 and all of its dependencies can be installed by running the following in the terminal (with the requirements.txt file included in this repository):

```
pip install -r requirements.txt
```
##### Preprocessing data: Run Data Preprocessing of MACS30200_finalproject.ipynb
1. Check and drop NA: No NA Value
2. Feature selection: draw heatmap of correlation with seaborns 
3. data scaling: scale features to avoid bias
4. combine the column name with scaled array of features with dictionary

##### Model: Linear Regression


##### Initial Outcome: Consistent with Hypothesis

###### 1
<img src="https://github.com/macs30200-s22/replication-materials-nijingwen/blob/main/figure/2008_2019_fea_imp.png" width=60% height=60%>


###### 2
<img src="https://github.com/macs30200-s22/replication-materials-nijingwen/blob/main/figure/gap.png" width=60% height=60%>

###### 3
<img src="https://github.com/macs30200-s22/replication-materials-nijingwen/blob/main/figure/covid_OLS_sig.png" width=60% height=60%>

##### Cite me:
@misc{nijingwen,
  author = {Ni, Jingwen},
  title = {Covid19 impacts on umployment rate of provinces in China},
  year = {2022},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/macs30200-s22/replication-materials-nijingwen}}
  }
