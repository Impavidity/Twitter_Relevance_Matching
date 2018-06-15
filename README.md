# Tweets Relevance Ranking with Representation Learning

## Task

Basically the task is relevance matching task. More specifically is to use neural model to rerank tweets based on the collection retrieved by statistical model such as Query Likelihood.

<img src="pictures/TaskOverview.png" width="800" />


## Dataset

Dataset for this task is from [TREC Microblog Tracks](https://trec.nist.gov/data/microblog.html) from 2011 to 2014.
In each year, there will be a set of queries (or called topics) provided by NIST for evaluation. For example,

> Evernote Hacked

Using the Query Likilihood Baseline, we could retrieve up to the top 1000 tweets. Example tweets are shown as follows.

>addicted to Evernote @url <br/>
>Your Evernote password has been hacked

There are judgements for a pool of tweets. For example, ***addicted to Evernote @url*** is not relevant and ***Your Evernote password has been hacked*** is relevant to the query.

We run four-fold cross-validation test split by year's data (i.e., train on three year's data, test on one year's data), and we sample 10 queries from each year in the training sets (in total 30 queries) as the validation set. 

<img src="pictures/cross-validation.png" width="400" />

- Statistics of dataset is shown as follows.

|Year|2011|2012|2013|2014|
|:--:|:--:|:--:|:--:|:--:|
|#queries|49|60|60|55|
|#tweets|39,780|49,879|46,192|41,579|
|#relevant|1,940|4,298|3,405|6,812|
|%relevant|4.87|8.62|7.37|16.38|

- Sampled validation query ID set for each fold

|2011|2012|2013|2014|
|:--:|:--:|:--:|:--:|
|3|53|123|185|
|8|58|130|190|
|11|64|138|203|
|12|74|140|204|
|13|86|143|206|
|17|93|146|207|
|19|97|152|209|
|34|100|158|214|
|40|102|167|217|
|41|107|168|221|







