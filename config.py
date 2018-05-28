
# set the path-to-files
TRAIN_FILE = "../train_merge.csv"
TEST_FILE = "../test_merge.csv"

SUB_DIR = "output"


NUM_SPLITS = 3
RANDOM_SEED = 2018

# types of columns of the dataset dataframe
CATEGORICAL_COLS = [
    'LBS', 'adCategoryId', 'advertiserId', 'age', 'aid',
     'campaignId', 'carrier',
     'consumptionAbility', 'creativeId', 'creativeSize', 
     'education', 'gender', 'house',
     'productId', 'productType'
    
]
MULTIVALUED_COLS = [
    'ct','os', 'topic1', 'topic2', 'topic3', 'kw1', 'kw2', 'kw3',
    'interest1', 'interest2', 'interest3', 'interest4', 'interest5', 
    'marriageStatus', 'appIdAction', 'appIdInstall'
]
NUMERIC_COLS = [
    # binary
    
    # numeric
#  'age_consumptionAbility',
#  'education_consumptionAbility',
#  'carrier_consumptionAbility',
#  'gender_consumptionAbility',
#  'creativeId_consumptionAbility',
#  'adCategoryId_consumptionAbility',
#  'productId_consumptionAbility',
#  'LBS_consumptionAbility',
#  'advertiserId_consumptionAbility',
#  'aid_consumptionAbility',
#  'campaignId_consumptionAbility',
#  'house_consumptionAbility',
#  'creativeSize_consumptionAbility',
#  'productType_consumptionAbility',
#  'gender_education',
#  'LBS_education',
#  'carrier_education',
#  'consumptionAbility_education',
#  'creativeSize_education',
#  'age_education',
#  'aid_education',
#  'gender_education.1',
#  'LBS_education.1',
#  'carrier_education.1',
#  'consumptionAbility_education.1',
#  'creativeSize_education.1',
#  'age_education.1',
#  'aid_education.1',
#  'aid_age',
#  'LBS_age',
#  'carrier_age',
#  'consumptionAbility_age',
#  'education_age',
#  'gender_age',
#  'house_age',
#  'productType_age',
#  'advertiserId_age',
#  'campaignId_age',
#  'creativeId_age',
#  'creativeSize_age',
#  'adCategoryId_age',
#  'productId_age',

    # feature engineering
    "missing_feat"
]

IGNORE_COLS = [
    "uid", "label"
    ,'ct','os', 'topic1', 'topic2', 'topic3', 'kw1', 'kw2', 'kw3',
    'interest1', 'interest2', 'interest3', 'interest4', 'interest5', 
    'marriageStatus', 'appIdAction', 'appIdInstall'
]
