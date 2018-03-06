Python3 Word-Count Script
---

This script allows you to get the word-count of a page

## Usage

1. Clone this repository
2. Add your URLs to urls.txt
3. run `python word_count.py`

## More Accurate Results

In order to get more accurate results, a "comp" (compensate) feature was added.

First find the average difference of wordcount between this script and the actual value:

1. Crawl 4-10 pages on a website using this script and record the wordcounts.
2. Manually find the word count of those pages using a tool like [wordcounter.net](http://wordcounter.net).
3. Get an average difference between the word counts in step 1 and step 2

Next, you could add a compensation value to a URL by using comma separated values:

ex. *This would set a compensation value of 300*.

```
https://my-cool-article.com/,300
```

**But I have a ton of URLS!!**

No worries. If you have a bunch of URLs, use `,!` on the first URL to set a global compensation.

ex. *In this example, all URLs will have a compensation of 300*.

```
https://article1.com,!300
https://article2.com
https://article3.com
```

ex. In this example, Article two and three have a compensation of 300, while article1 has 0.

```
https://article1.com
https://article2.com,!300
https://article3.com
```

## Setting a Custom Timeout

By default, this script sleeps for 100 milliseconds in between checking URLs.

You could set a custom amount by editing the `timeout` variable in the script.
