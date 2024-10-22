This repository uses Python 3.11, Pytest 7.1.1, and Selenium 4.8.2 to run three tests on the following URL: https://www.google.com/finance

1) Load URL and confirm its page title contains "Google Finance" to confirm pageload and domain
2) Parse the selection of six stocks in the You Might Be Interested section of the page to get the stock ticker symbols, then compare those against a static data set to determine differences between each set. This test checks the symbols found in the YMBI set and prints out the symbols not in the static data set
3) Using the same logic as test #2, this performs the same element-parsing and comparison, but the result prints out the symbols in the static data set that do not appear in the YMBI section

This test suite is set up to function with GitHub Actions in the following way:
  * run - all (runs all three tests)
  * run - ymbi_set (runs test #2)
  * run - test_set (runs test #3)

This test is also configured to run daily through a cron configuration in config.yml, currently set to run at 00:00 PST (07:00 UTC)
