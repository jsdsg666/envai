# envai
 
One Paragraph of project description goes here
 
## Getting Started
 
This project is used for modeling and machine learning applications in the environment field.Applicable disciplines of the project:Environmental Science and Engineering, Water Supply and Drainage Science and Engineering, Civil Engineering, Municipal Engineering, Resources and Environment, Environmental Informatics, Machine Learning, Deep Learning
 
### Prerequisites
You need the environment of python3,third party library of pandas,openpyxl


### Installing
You can get it by pip install envai
```
pip install envai
```

 
## Example
```
import pandas as pd
import envai

train=pd.read_excel(../dataset/pre_train.xlsx)
test=pd.read_excel(../dataset/pre_test.xlsx)
'''
difference_sequence is the environmental indicator to be constructed. The second column is the initial value, the third column is the end value, and the first column is the difference value.The second and third columns are names of columns about the environmental data set what you need to optimize,  the first column is that you need to name it yourself
'''
difference_sequence=[('COD', 'WI_COD', 'WO_COD'),(...),('AR_AN', 'WI_AN', 'AR_AN')]
print(train.describe(),test.describe())

after_train,after_test=env_data_opt(train, test, difference_sequence)
print(after_train.describe(),after_test.describe())
```
## Versioning
 0.1.3

 
## Authors
 
* **Wang YuQi** -*Harbin Institute of Technology*- *Main work* 
* **Wang HongCheng** -*Harbin Institute of Technology*- *tutor* 
* **Wang AiJie** -*Harbin Institute of Technology*- *tutor* 
 
 
## License
 
GPL
 
## Acknowledgments
 

