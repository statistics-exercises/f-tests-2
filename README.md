# Ratio of variances

Now that we have established that you remember how to estimate the sample variance we are in a position to introduce the hypothesis tests we are going to study this week.  In these tests, we are always going to be sampling from two different distributions.  The null hypothesis is that the variances of the two distributions are in a certain ratio.  The alternative hypothesis, meanwhile, is that the ratio of the variances does not take/is less than/is more than the specified value.  In other words, a null and alternative hypothesis for this type of test might be:

![](https://render.githubusercontent.com/render/math?math=H_0:\frac{\sigma_1^2}{\sigma_2^2}=\lambda_0\qquad\qquad\H_1:\frac{\sigma_1^2}{\sigma_2^2}\ne\lambda_0)

Obviously, we cannot extract the exact values for the variances by sampling. We instead need to estimate the sample variances from the samples of the two distribution using:

![](https://render.githubusercontent.com/render/math?math=s^2=\frac{n}{n-1}\left[\frac{1}{n}\sum_{i=1}^nX_i^2-\left(\frac{1}{n}\sum_{i=1}^nX_i\right)^2\right])

With the sample variances, ![](https://render.githubusercontent.com/render/math?math=S_1^2) and ![](https://render.githubusercontent.com/render/math?math=S_2^2), calculated for the two sets of data using the formula above, we can then introduce the following test statistic:

![](https://render.githubusercontent.com/render/math?math=F=\frac{\left(\frac{S_1^2}{\sigma_1^2}\right)}{\left(\frac{S_2^2}{\sigma_2^2}\right)}=\frac{1}{\lambda_0}\frac{S_1^2}{S_2^2})

In the next couple of tasks, you are going to write code to sample from this random variable.  We are then going to characterise the distribution for this random variable.  The remainder of the tasks will then show you how we can use this distribution to perform hypothesis tests.

__To complete this task you will thus need to complete the function called `gen_f_variable`__.  This function takes two inputs `N1` and `N2`.  These numbers are the numbers of samples to take from the two distributions whose variances are being compared.  I have already started the function for you by generating `N1` standard normal random variables and storing them in a NumPy array called `sample1` and by generating `N2` standard normal random variables and storing them in the NumPy array called `sample2`.  To complete the function you will need to calculate `F` from this data using the formula above.  The value of `F` should then be returned from the function.  Please note that the elements in `sample1` and `sample2` are all standard normal random variables.  As such ![](https://render.githubusercontent.com/render/math?math=\sigma_1=\sigma_2) and hence ![](https://render.githubusercontent.com/render/math?math=\lambda_0=1).

Once you complete the function and run the code a graph showing a series of samples of the random variable `F` will be generated.
    
