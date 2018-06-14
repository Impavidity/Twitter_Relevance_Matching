# Tweets Relevance Ranking with Representation Learning

## Task

Basically the task is relevance matching task. More specifically is to use neural model to rerank tweets based on the collection retrieved by statistical model such as Query Likelihood.

![Task Overview](pictures/TaskOverview.png | width=250)

## Dataset

Dataset for this task is from [TREC Microblog Tracks](https://trec.nist.gov/data/microblog.html) from 2011 to 2014.
In each year, there will be a set of queries (or called topics) provided by NIST for evaluation. For example,

> Evernote Hacked

Using the Query Likilihood Baseline, we could retrieve up to the top 1000 tweets. Example tweets are shown as follows.

> addicted to Evernote @url
> Your Evernote password has been hacked

There are judgements for a pool of tweets. For example, *addicted to Evernote @url* is not relevant and *Your Evernote password has been hacked* is relevant to the query.






