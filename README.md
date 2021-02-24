### Project

# Demographic Data Analyzer

In this project, I created an analyser that reads data using Pandas. A dataset of demographic data was extracted from the 1994 Census database. Here is a preview of what the dataset looks like in Excel format:

|    |   age | workclass        |   fnlwgt | education   |   education-num | marital-status     | occupation        | relationship   | race   | sex    |   capital-gain |   capital-loss |   hours-per-week | native-country   | salary   |
|---:|------:|:-----------------|---------:|:------------|----------------:|:-------------------|:------------------|:---------------|:-------|:-------|---------------:|---------------:|-----------------:|:-----------------|:---------|
|  0 |    39 | State-gov        |    77516 | Bachelors   |              13 | Never-married      | Adm-clerical      | Not-in-family  | White  | Male   |           2174 |              0 |               40 | United-States    | <=50K    |
|  1 |    50 | Self-emp-not-inc |    83311 | Bachelors   |              13 | Married-civ-spouse | Exec-managerial   | Husband        | White  | Male   |              0 |              0 |               13 | United-States    | <=50K    |
|  2 |    38 | Private          |   215646 | HS-grad     |               9 | Divorced           | Handlers-cleaners | Not-in-family  | White  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
|  3 |    53 | Private          |   234721 | 11th        |               7 | Married-civ-spouse | Handlers-cleaners | Husband        | Black  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
|  4 |    28 | Private          |   338409 | Bachelors   |              13 | Married-civ-spouse | Prof-specialty    | Wife           | Black  | Female |              0 |              0 |               40 | Cuba             | <=50K    |


Unit tests are written for the user under `test_module.py`.

### Development

For development,  `main.py` is used to test the functions. Click the "run" button and `main.py` will run.

### Testing 

The tests were imported from `test_module.py` to `main.py` for the user's convenience. The tests will run automatically whenever you hit the "run" button.

### Output 

Preview of the final output:
```python
>>> Number of each race: [27816, 3124, 1039, 311, 271]
>>> Average age of men: 39.4
>>> Percentage with Bachelors degrees: 16.4%
>>> Percentage with higher education that earn >50K: 46.5%
>>> Percentage without higher education that earn >50K: 17.4%
>>> Min work time: 1 hours/week
>>> Percentage of rich among those who work fewest hours: 10.0%
>>> Country with highest percentage of rich: Iran
>>> Highest percentage of rich people in country: 41.9%
>>> Top occupations in India: Prof-specialty
>>> ..........
>>> ----------------------------------------------------------------------
>>> Ran 10 tests in 11.723s
>>> 
>>> OK
```

### Dataset Source

Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.
