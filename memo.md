# Medical Expense Modeling: Stakeholder Memo

Adding age improved the linear regression model compared with the BMI-only baseline.
The BMI-only model had an R² of approximately 0.03943, while the two-feature model achieved approximately 0.11726.
This is an increase of 0.07782, or about 7.78 percentage points of explained variation.
RMSE also decreased from $11,864.41 to $11,373.64, although the remaining prediction errors are large.
These are in-sample results calculated on the same 1,338 observations used to fit the models, so they do not establish performance on new customers.

The Normal Equation and Gradient Descent produced nearly identical original-unit coefficients: an intercept of approximately -6,437.35, a BMI coefficient of 333.39, and an age coefficient of 241.90.
Both methods minimize the same ordinary least squares objective, and with a full-rank design matrix and converged Gradient Descent, they should reach the same solution.
The Normal Equation solves for the coefficients directly, while Gradient Descent approaches the solution iteratively after standardizing both features and then converting coefficients back to their original units.

The positive age coefficient means that, holding BMI constant, one additional year of age is associated with about $241.90 higher predicted medical expenses.
For example, a ten-year age difference corresponds to approximately $2,419 higher predicted expenses at the same BMI.
This association does not establish causation, and the negative intercept should not be interpreted as a realistic expense because age and BMI zero are outside the meaningful context of this model.

The two-feature model is not strong enough for deployment because roughly 88.27% of the observed variation remains unexplained.
Important information such as smoking status is omitted, and a good fit between the two optimization methods does not guarantee accurate business predictions.
Before deployment, I would evaluate additional predictors, use validation data for model selection and a separate test set for final evaluation, inspect errors across groups, and agree on acceptable error thresholds for the intended business use.
