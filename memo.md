# Assignment 2 Memo

Adding age improved the linear regression model compared with the BMI-only baseline. The BMI-only model had an R² of approximately 0.0394, while the two-feature model achieved an R² of approximately 0.1173. This is an improvement of about 0.0779, or 7.79 percentage points in explained variation. Therefore, age provides additional predictive information beyond BMI alone.

The Normal Equation and Gradient Descent produced nearly identical model weights. Both methods estimated an intercept of approximately -6437.35, a BMI coefficient of 333.39, and an age coefficient of 241.90. This agreement is expected because both methods are optimizing the same ordinary least squares objective. The Normal Equation solves for the coefficients directly, while Gradient Descent approaches the same solution iteratively.

The positive age coefficient means that, holding BMI constant, an additional year of age is associated with about a $241.90 increase in predicted medical expenses. In plain language, older individuals in this dataset tend to have higher predicted medical costs even when BMI remains the same.

Although adding age improves the model, the two-feature model is not strong enough for deployment. An R² of about 0.1173 means that most of the variation in medical expenses is still unexplained. Important predictors such as smoking status, region, and other health or demographic factors are not included. Therefore, I would treat this model as a useful baseline and add stronger features before considering business deployment.