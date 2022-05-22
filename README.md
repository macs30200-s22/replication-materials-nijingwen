[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6483892.svg)](https://doi.org/10.5281/zenodo.6483892)

# MACS30200_Project: Jingwen Ni
#### RQ: How covid19 impacts on unemployment rate of provinces in China?
#### Hypothesis: Covid19 will promote umemployment rate of provinces in 2020
#### Data source: 
1. National Bureau of Statistics: http://www.stats.gov.cn/ : scraping
2. Harvard: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/MR5IJN : download csv
                 
#### Title：The study of covid19's impacts of unemployment in China on provinces' level in 2020 by using regression and time series model.![image]

#### Introduction:
Covid19, later renamed as Coronavirus, gripped China since the beginning of 2020(Qiu et al.2020). Wuhan in Hubei province was the first city where was found covid19 cases in China. Covid19 spread rapidly over the world and brought unignorable crisis in both economics and medical systems and by the end of November in 2021, there were more than 63 million reported cases and 1.4 million deaths over the world (Brodeur, Gray, Islam, Bhuiyan 2021). Because Covid19 is a respiratory infectious disease, countries published several policies about social distance, quarantine to reduce covid19 infections. This contagious disease changed the world from economics and politics throughout the history (Ceylan, Ozkan, Mulazimogullari, 2020). In China, government took enforce measures that locking down the cities which has covid cases which slowdown the economics activities considerably. 
The cost of the covid19 was burden on China’s economics. The control measures to prevent the covid19 leaded 2.7% loss of China’s annual gross domestic product. From BBC news, From January 23rd, Wuhan was locked down for 72 days which means no one can exit and enter this city. Citizens in Wuhan cannot get out of their home. They can only stay and wait for necessities delivery which was arranged by government. To the nationwide, China also took actions: for instance, The risk classification for each country is based on the principle of formulating guidelines for classification and implementing the strategy of "internal prevention of spread and external prevention of import" to reduce the possible impact of imported cases on China. Establish a joint prevention and control mechanism at ports of entry, organize the Civil Aviation Administration, customs, public security, health, foreign affairs, border control, airports, and other departments to coordinate the information, identity registration, health monitoring, emergency response and other related work. Due to covid19, both exports and imports were limited which leaded many businesses got into trouble. They had to cut the number of employees to reduce operations expenses. Hence in this case, the unemployment rate should increase. 
In another case, the unemployment could decrease because of more remote jobs were provided during the covid19 period. Many women who were a housewife and gave up their jobs to take care of their families, could have a chance to balance their work and families. In addition, because of the remote option, people did not need to worry about the relocation problem so that they can have more options for applying jobs which would decrease the unemployment rate. 
China, a socialist country, which labor markets reformed and transformed into a market-driven market system. After the reformation, people were not limited by “Hukou”, a certification of their birthplace and they were not allowed to work in outside of the birthplace before the reformation, so that there were a lot of migrant-workers those affected by Covid19, the quarantine and lock-down policies. Unemployment was a historical problem and become more serious with time in China because China is a populous country. From United Nations, the world population was 7.6 billion and the population of Mainland was 1.39 billion which was 18.3% of the world while China only has 7.059% land area share of the world. From January 1996 to September 2002, the unemployment of urban residents increased from 6.1% to 11.1% (Giles, Park, Zhang, 2004). In economics, unemployment was a significant factor which would lead to poverty and income disparity in China. In 1999, urban unemployment was a major cause of urban poverty, and the growing urban poverty became a significant factor which worsen the urban inequality. This inequality in China has increasing influence on migrant households (Xue, Zhong, 2003). In addition to economic perspective, unemployment would also cause psychological and health problems. The unemployed group could have greater symptoms like depression and anxiety than employed group. Moreover, as central of policy debate and aggregate resource utilization, unemployment was also an important indicator (Gali, Smets, Wouters 2022). Furthermore, unemployed group was more likely to visit a physician than employed group (Linn, Sandifer, Stein, 2011). Accordingly, unemployment in China was worth to putting efforts on. 
There are 31 provinces in China, the policy about covid were various and depend on their own situation. In addition, because of the geographic differences, the policy could also be affected. In previous study, scholars analyzed the covid19’s effects on unemployment in different races, and gender group in United States. And they found the effects of covid 19 on unemployment were significant different on races and genders (Gezici, Ozay, 2020). In China, there were scholars studied the covid impacts on nationwide level in 2020 because it is obvious that the unemployment rate increased in 2020 compared with previous years. In Brazil, researchers found the burden of covid 19 is greater in areas with high social deprivation. Until August 6th 2020, Bahia has 179139 confirmed cases, and 3767 deaths. There was a spatial association between the epidemiological indicators and SDI been observed. 22 municipalities had the priority for incidence which was 1.6 times higher than state rate. And there were 40 cities which had 1.2 times higher death rate than the state one while they also had 4.1 times higher than the state rate (Souza, Carmo, Machado, 2020). It motivated me to study about the covid19 impacts on unemployment on province level in China instead of study the impacts on nationwide level. The unemployment rate of provinces has different trends, and some fluctuations were caused by seasonal, structural etc and could be affected by other factors. Covid19 would not disappear in China and in the world rapidly. Even though only one country over the world has the disease, the covid 19 never ends. Accordingly, to face, solve, and predict the social problems from Covid, the study needs to analyze how much fluctuations was caused by covid19. 
To study the research question, how covid19 affected unemployment rate in China on province level in 2020, I utilized both regression and time series model to make prediction and analyze the results with the dataset scrapping from National Bureau of Statistics of China. Before starting the work, the hypothesis I had is covid19 will promote unemployment rate in China by province level in 2020. The regression model can show the feature importance and the causal effects between covid19 and unemployment. From regression model, one unit of confirmed increasing will lead to 0.066 unit increase in unemployment, which prove the hypothesis that covid will promote unemployment rate of provinces in China. The time series can predict unemployment by avoiding using control variables’ data which could be affected by covid. I found the covid impacts were various based on geographical reasons and then lead to different impacts on unemployment rate of provinces. 
	The limitation of the dataset also cannot be ignored. In the regression model, the selection of control variables was not comprehensive. The dataset of control variables was scraping from Chinese government which could not be the true value. Besides, the time series makes prediction by trends over time so it cannot consider the special cases in the model like policy impact. The strengths of the research are using two different models for studying the impacts of covid and clearly show the initial finding by data visualization on Tableau.


The code is written in Python 3.9.7 and all of its dependencies can be installed by running the following in the terminal (with the requirements.txt file included in this repository):

```
pip install -r requirements.txt
```
#### Preprocessing data: Run Data Preprocessing of MACS30200_finalproject.ipynb
1. Check and drop NA: No NA Value
2. Feature selection: draw heatmap of correlation with seaborns 
3. data scaling: scale features to avoid bias
4. combine the column name with scaled array of features with dictionary

#### Model: OLS regression, Time series, linear regression
1. Firstly, I use time series to predict the unemployment rate in 2020. Figure 6 is the head of the graph. In figure 6, the x axis is time, the y axis is province’s unemployment. The whole sheet will have 31 separate graphs of 31 provinces. 
2. Secondly, To see whether covid is statistically significant in the gap value between the predicted and true unemployment rate in China of different provinces, I utilized OLS regression to see the p value. 
3. Thirdly, To test the hypothesis, I divided the test into nationwide part and provinces’ part. I calculate the coefficient of variables of the nationwide by linear regression; On the provinces level, from the coefficient of time series model. There are 31 provinces which have different outcomes!



#### Initial Outcome: 
partially consistent with Hypothesis. In nationwide, the covid19 promoted the unemployment rate. On province level, covid19 increase the unemployment rate in 22 provinces and the unemployment in 9 provinces are reduced. The covid19 imopacts also has geographically difference that it is larger on west-northern part than east western part of China. 

##### 1: Time series model predicted the unemployment rate for each province if covid19 never existed.
<img src="https://github.com/macs30200-s22/replication-materials-nijingwen/blob/main/figure/time_series.png" width=60% height=60%>


##### 2: The covid has positive relation with the gap_value. More covid will lead to larger predicted gap between true value and predicted value. 
<img src="https://github.com/macs30200-s22/replication-materials-nijingwen/blob/main/figure/feature_2020.png" width=60% height=60%>


##### 3: The covid19 impacts also has geographically difference that it is larger on west-northern part than east western part of China. 
<img src="https://github.com/macs30200-s22/replication-materials-nijingwen/blob/main/figure/geo_gap.png" width=60% height=60%>


##### 4: Through the OLS regression for gap_value summary, the p value of deaths and recovery is smaller than 0.05 which is statistically significant
<img src="https://github.com/macs30200-s22/replication-materials-nijingwen/blob/main/figure/covid_OLS_sig.png" width=60% height=60%>

##### 5: Through the linear regression for nationwide, the coefficient of covid19 recovery and confirmed are positive and of deaths are negative
<img src="https://github.com/macs30200-s22/replication-materials-nijingwen/blob/main/figure/coefficient.png" width=60% height=60%>

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
