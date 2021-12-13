- Regrade 12/31/21 - great job! 7/7 

This is looking good! One small thing: when you're calculating the median, you're starting at column index 3, which actually skips male10, so your medians are a little off (not a big deal). For the QQ plot, the expected distribution is not a normal distribution. Under the null hypothesis, the expected distribution of the p-values is a uniform distribution (think about it, for any given alpha, you would expect the same proportion of p-values to be below that alpha, just by chance). Currently, you're comparing your p-values to a normal distribution, which doesn't make a ton of sense. (-1)
When you're doing the FDR correction, you should be using an alpha of 0.1 rather than 0.05, but not a big deal. When you're controlling for sex, you shouldn't be doing separate analyses for male and female. Rather you should include sex as an additional covariate in your regression (this could be a column with 0s for male and 1s for females, for example). So you should still only get a single p-value for each transcript. (-0.5) I still need the comparison of significant genes between controlling for sex and not. And then your volcano plot should be based on the p-values you get from the regression controlling for sex (although the first volcano plot you have looks really good) (-0.5)

5/7