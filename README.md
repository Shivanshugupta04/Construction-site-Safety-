Project Details:
Overview
We will be working on a “Con-Safety” project. In this, we will create a
solution for our customers (project manager of the construction site)
to check site safety for their laborers before starting their work at any
construction site. Using this project, they can reduce the risk of
occurrence of accidents on the site. To implement this, we will train
Classical Machine Learning models those will get input by asking a
few relevant questions related to the construction site from the project
manager. Based on the answers given by project site manager, ML
models will predict that how much it is safe to work on that site. If our
models predicts the high safety percentage then laborers can start
their work. However, in case of low safety value predicted by our
trained models, working on that site will be considered as “Not Safe” because of the high chances for happening accidents. In such case of
low safety percentage, our model will find where they are lacking in
safety and based on that it will suggest some precautionary steps to
be taken to prevent accidents that may occur in the future. Problem Statement
What we have:
Data-Set: There are mainly 4 kinds of accidents take place on
construction sites. These four types are Fall, Electrocution, Struck by
and caught by. To work with models, the very first thing is data which
we have web scrapped from OSHA. OSHA is an organization that
works for labor safety and assures safe and healthy working
conditions for the workers. Features: From scrapped data, we have reports of accidents those
happened on construction sites. From those reports, we have
extracted some important keywords those are acting as input features
for our Classical Machine Learning models. Target: Here, we have three different targets which are:
1. Accident type(Fall, Electrocution, Struck by and Caught by)
2. Injury type(Fracture, Dislocation, Burn, Amputation, etc.)
3. Severity(Fatal, Non-Fatal)
Using above features, we have trained three models those are
predicting relevant results for all three targets with different classes. What we need to do:
So we have enough data, by which, our model can predict that in
some particular site a particular type of accident may happen. But what about the safe side? Our model should also predict that a
particular site is safe to work.
 1. Data creation:
Now we have to work on considering some particular
situations where we can say that the construction site is safe to
work. While creating the data set of safe cases, we have to focus
on relevant keywords which we can pass in our models. As per the data-set, here we only have data of accident
reports, not for safe conditions, because OSHA is having reports
for accidents only, and according to our requirement we also
need data where it can show the safe cases. As our model is
trained on unsafe data cases, so it always predicts that our site
is unsafe and after training our models again on dataset having
both safe and unsafe cases, we can increase the accuracy of our
model.So, on the behalf of previous data, we have to create
sample data, which is having a target value as ‘safe site’ or less
possibility of an accident. For an instance, when every
precaution was taken and the site was inspected very well at
that time the workers are safe. Another instance may be, there is a possibility like
something is missing during the inspection, like the ladder is
perfect and the worker is also wearing a harness, but the
landing surface may be uneven, so while working, if the worker
leans away from the ladder, he may fall, but this time the
situation is not risky. In this scenario, our model should predict
that this situation is ‘less risky’ or some small accident may
happen. Until now we have data for accidental situations, now we
have to create data for less risky and safe situations, so that we
can balance the data among “fatal”, “non-fatal/high risky”, “low
risk”, “safe” classes. In data creation, we will use some useful keywords, and
based on those keywords, we will fix the target value as well.
2. Creating different models and selecting the best one
In our problem, we have 3 targets where for each we have to
create a separate model and each model is independent of the
other. These targets are:
2.1 Accident type:
This target will show what accident happened. Let’s say it
was ladder falling, scaffold falling, excavation, electrocution, etc. For predicting this output, we are going to create a model. 2.2 Injury type
This target will show how injured the worker is, after the
accident. Only a fracture, broken bone, burn, etc. This model is going to tell the condition of the worker. 2.3 Severity:
This target value shows how severe the accident was. Whether there is a chance for survival or the injured
person may lose his life. We will create models for these target values by using different
machine learning algorithms and we will select the best fit
model among them. 3. Handling skewness/Class imbalance
Now when we have data for all the classes, so can handle the
skewness of data. As we know that handling the skew data is
important for good accuracy. 4. Using Ensemble techniques
After creating different models for each target we are going to
assign weights to these models and merge them, using the
ensemble technique, which will help us in making our model
more accurate. 5. Model Building for every individual category
Until now we build 3 models for 3 target values, where the
project manager has to answer every question related to all
accident types, whether it is needed or not, which may be a
time-consuming process and can be unnecessary. Let’s say
someone is working on a ladder, at that time also the manager
has to give answers for all the questions, which are not
required. . So now we have to build different models for every
accident category, like Ladder, Roof, Scaffold, Crane, Excavation, Electrocution, etc. and every model will have the related
questions to its category. So, in that situation manager can
inspect the particular scenario and get to know about the safety. 6. Suggesting Precautionary steps:
In the end, we will suggest some relevant precautionary steps to
follow on the construction site if it is risky to work there. These
steps are given by OSHA which we are going to suggest to the
end users, to reduce the risk of happening accidents on
construction site
