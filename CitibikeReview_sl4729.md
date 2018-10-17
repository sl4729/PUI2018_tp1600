### a. Verify Null and alternative hypotheses
	-Original Null hypothesis: The average number of daily trips using 24 hour passes or 3 day passes on weekends (E) in NYC during August 2018 is the same or lower than the average amount on weekdays (D) during the same time period with a significance level of .10. (Weekends=Saturday and Sunday).
	H0: E-D<=0  <br/>

	-Original Alternative Hypothese :The average number of daily trips using 24 hour passes or 3 day passes on weekends (E) during August 2018 is significantly higher than the average amount on weekdays (D) during this same period.
	H1: E-D>0  <br/>

	Comment: 
	The Null and alternative hypothesis are formulated correctly. 
	Suggestion:
	I was a little confused by the description "using the 24 hour passes or 3 day passes" because it is not in the original dataset. I would rephrase is to "The average number of daily trips from subscribers ". 
	Also, the origial idea was "Non-membership usage (likely driven by leasure bikers, tourists & visitors) is highest on weekends." It might make more sence if changing the null hypothesis to "The average number of daily trips from non-subscribers on weekends (E) in NYC during August 2018 is the same or lower than the average amount on weekdays (D) during the same time period with a significance level of .10. (Weekends=Saturday and Sunday) H0: E-D<=0  and the alternative hypothesis: The average number of daily trips from non-subscribers on weekends (E) during August 2018 is significantly higher than the average amount on weekdays (D) during this same period.
	H1: E-D>0  <br/>

### b. Verify that the data supports the project
	I think the data has the appropriate features to answer the question. The data could be further procesed. The hypothese concerns only the absolute number of trips from subscribers/non-subscribers, therefore the features like 'bikeid','tripduration','starttime''stoptime' could be dropped. <br/>

### c. Chose statistical test
	I think T-test would be appropriate to test the hypothesis. The data used to test the hypothesis is numerical, and the number of trips from two kinds of costomer(subscribers/non-subscribers) are unpaired. Also, there is difference between between these two groups, and theu are not linked or related with each other. So T-test is an appropriate test here. <br/>


	

