[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6483892.svg)](https://doi.org/10.5281/zenodo.6483892)

# MACS30200_Project: Jingwen Ni
#### RQ: How covid19 impacts on unemployment rate of provinces in China?
#### Hypothesis: Covid19 will promote umemployment rate of provinces in 2020
#### Data source: 
1. National Bureau of Statistics: http://www.stats.gov.cn/ : scraping
2. Harvard: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/MR5IJN : download csv
                 
#### Title：The study of covid19's impacts of unemployment in China on provinces' level in 2020 by using regression and time series model.![image]


The code is written in Python 3.9.7 and all of its dependencies can be installed by running the following in the terminal (with the requirements.txt file included in this repository):

```
pip install -r requirements.txt
```

#### Collect Data
1. The data of control variables are scraped from NBS of China by using the Data Scrap.py
2. The data of covid is down load from Harvard. 
3. All data are stored in DATA folder

#### Preprocessing data: Run Data Preprocessing of MACS30200_finalproject.ipynb

1. Check and drop NA: No NA Value
2. Feature selection: draw heatmap of correlation with seaborns 
3. data scaling: scale features to avoid bias
4. combine the column name with scaled array of features with dictionary

#### Model: OLS regression, Time series, linear regression
1. Firstly, I use time series to predict the unemployment rate in 2020. Figure 1 is the head of the graph. In figure 1, the x axis is time, the y axis is province’s unemployment. The whole sheet will have 31 separate graphs of 31 provinces. 
2. Secondly, To see whether covid is statistically significant in the gap value between the predicted and true unemployment rate in China of different provinces, I utilized OLS regression to see the p value. 
3. Thirdly, To test the hypothesis, I divided the test into nationwide part and provinces’ part. I calculate the coefficient of variables of the nationwide by linear regression; On the provinces level, from the coefficient of time series model. There are 31 provinces which have different outcomes!

Time series:
In the Covid.twb file in the main board.

OLS regression and linear regression
In the MACS30200_finalproject.ipynb


#### Initial Outcome: 
partially consistent with Hypothesis. In nationwide, the covid19 promoted the unemployment rate. On province level, covid19 increase the unemployment rate in 22 provinces and the unemployment in 9 provinces are reduced. The covid19 imopacts also has geographically difference that it is larger on west-northern part than east western part of China. 

##### 1: Time series model predicted the unemployment rate for each province if covid19 never existed.
<img src="https://github.com/macs30200-s22/replication-materials-nijingwen/blob/main/figure/time_series1.png" width=60% height=60%>


##### 2: The covid19 impacts also has geographically difference that it is larger on Northwest part than Southeast part of China. 
<img src="https://github.com/macs30200-s22/replication-materials-nijingwen/blob/main/figure/geo_gap.png" width=60% height=60%>


##### 3: Through the OLS regression for gap_value summary, the p value of deaths and recovery is smaller than 0.05 which is statistically significant
<img src="https://github.com/macs30200-s22/replication-materials-nijingwen/blob/main/figure/covid_OLS_sig1.png" width=60% height=60%>

##### 4: Through the linear regression for nationwide, the coefficient of covid19 recovery and confirmed are positive and of deaths are negative
<img src="https://github.com/macs30200-s22/replication-materials-nijingwen/blob/main/figure/coefficient1.png" width=60% height=60%>

#### Conclusion:
The research question was answered by the prediction of unemployment rate by time series model and the p value of OLS regression model. The p value of covid19 deaths cases and recovery cases are less than 0.05 which mean statistically significant in the gap of predicted and true unemployment rate that covid 19 has large impacts on unemployment rate in China on provinces’ level. In addition, to test the hypothesis that the covid 19 will promote the unemployment. I used linear regression model to test the nationwide level and time series to test for the provinces’ level. On nationwide level, the covid19 promoted the unemployment rate and on provinces level, covid19 promoted unemployment in 22 provinces and decrease the unemployment rate in 9 provinces. 




#### Cite me:
@misc{nijingwen,
  author = {Ni, Jingwen},
  title = {Covid19 impacts on umployment rate of provinces in China},
  year = {2022},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/macs30200-s22/replication-materials-nijingwen}}
  }
