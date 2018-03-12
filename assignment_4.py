def get_list_of_university_towns():
    '''Returns a DataFrame of towns and the states they are in from the
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ],
    columns=["State", "RegionName"]  )

    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. '''

    return "ANSWER"

#algorithm or pesudo not real code
def get_list_of_university_towns():
    with open('university_towns.txt') as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    lst=[]
    state=''
    region=''
    for line in content:
            #if i contains '[ed' then the line has a state
            if '[ed' in line:
                    #state = get the state by removing everything from '[' to end(using split on'[ed' and selecting the first element )
                     state = line.split('[')[0]
            else:

                    #region = get region by removing everything from '(' to end if the line contains ( and removing \n otherwise (using split on' (' and selecting the first element and using strip on the result will cover both cases)
                     region = line.split(' (')[0].strip()
                    #add [state,region] to lst
                     lst.append([state,region])
    df = pd.DataFrame.from_records(lst, columns=['State', 'RegionName'])

    return df

#############################################################################################
def get_recession_start():
    '''Returns the year and quarter of the recession start time as a
    string value in a format such as 2005q3'''

    return "ANSWER"


    def get_recession_start():
    recession = pd.read_excel('gdplev.xls', skiprows = 7, parse_cols = 'E:G')
    recession.rename(columns = {'Unnamed: 0':'Quarter', 'Unnamed: 1':'GDP in Billions', 'Unnamed: 2':'GDP Chained 2009'}, inplace = True)
    recession['Year'] = recession['Quarter'].str[:4].astype(int)
    recession = recession[recession.Year > 2000]
    recession["diff"] = recession['GDP Chained 2009'].diff(1)
    recession['trend'] = np.where(recession['diff'] > 0, 'Increase', 'Decrease')
    for i in range(2,len(recession)):
        if (recession.iloc[i-2][5] == 'Decrease') and (recession.iloc[i-1][5] == 'Decrease'):
            return recession.iloc[i-2][0]

#############################################################################################
def get_recession_end():
    '''Returns the year and quarter of the recession end time as a
    string value in a format such as 2005q3'''

    return "ANSWER"


def get_recession_end():
    recession = pd.read_excel('gdplev.xls', skiprows = 7, parse_cols = 'E:G')
    recession.rename(columns = {'Unnamed: 0':'Quarter', 'Unnamed: 1':'GDP in Billions', 'Unnamed: 2':'GDP Chained 2009'}, inplace = True)
    recession['Year'] = recession['Quarter'].str[:4].astype(int)
    recession = recession[recession.Year > 2000]
    recession["diff"] = recession['GDP Chained 2009'].diff(1)
    recession['trend'] = np.where(recession['diff'] > 0, 'Increase', 'Decrease')
    for i in range(2,len(recession)):
        if (recession.iloc[i-3][5] == 'Decrease') and (recession.iloc[i-2][5] == 'Decrease') and (recession.iloc[i-1][5] == 'Increase'):
            return recession.iloc[i][0]

#############################################################################################
def get_recession_bottom():
    '''Returns the year and quarter of the recession bottom time as a
    string value in a format such as 2005q3'''

    return "ANSWER"

def get_recession_bottom():
    recession = pd.read_excel('gdplev.xls', skiprows = 7, parse_cols = 'E:G')
    recession.rename(columns = {'Unnamed: 0':'Quarter', 'Unnamed: 1':'GDP in Billions', 'Unnamed: 2':'GDP Chained 2009'}, inplace = True)
    recession['Year'] = recession['Quarter'].str[:4].astype(int)
    recession = recession[recession.Year > 2000]
    recession["diff"] = recession['GDP Chained 2009'].diff(1)
    recession['trend'] = np.where(recession['diff'] > 0, 'Increase', 'Decrease')
    recession_start = get_recession_start()
    recession_end = get_recession_end()
    recession.reset_index(inplace=True)
    start_index = recession[recession['Quarter'] == recession_start].index.tolist()[0]
    end_index = recession[recession['Quarter'] == recession_end].index.tolist()[0]
    recession_window=recession.iloc[start_index:end_index+1]
    recession_bottom = recession_window['GDP Chained 2009'].min()
    bottom_index = recession_window[recession_window['GDP Chained 2009'] == recession_bottom].index.tolist()[0]-start_index
    return recession_window.iloc[bottom_index]['Quarter']

#############################################################################################

def convert_housing_data_to_quarters():
    '''Converts the housing data to quarters and returns it as mean
    values in a dataframe. This dataframe should be a dataframe with
    columns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].

    Note: Quarters are defined in the assignment description, they are
    not arbitrary three month periods.

    The resulting dataframe should have 67 columns, and 10,730 rows.
    '''

    return "ANSWER"

# Use this dictionary to map state names to two letter acronyms
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}

def convert_housing_data_to_quarters():
    housing = pd.read_csv('City_Zhvi_AllHomes.csv')
    housing['State'] = housing['State'].map(states)
    housing.set_index(['State','RegionName'], inplace = True)
    housing = housing[housing.columns[6:]].rename(columns=pd.to_datetime)
    housing = housing.resample('Q',axis=1).mean()
    housing = housing.rename(columns=lambda x: str(x.to_period('Q')).lower())
    housing = housing.loc[:,'2000q1':'2016q3']

    return housing

#############################################################################################
    def run_ttest():
    '''First creates new data showing the decline or growth of housing prices
    between the recession start and the recession bottom. Then runs a ttest
    comparing the university town values to the non-university towns values,
    return whether the alternative hypothesis (that the two groups are the same)
    is true or not as well as the p-value of the confidence.

    Return the tuple (different, p, better) where different=True if the t-test is
    True at a p<0.01 (we reject the null hypothesis), or different=False if
    otherwise (we cannot reject the null hypothesis). The variable p should
    be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).'''

    return "ANSWER"

def run_ttest():
    #split the data into University Towns and Non-University towns
    housing = convert_housing_data_to_quarters()
    rec_start = get_recession_start()
    rec_bottom = get_recession_bottom()
    housing['PriceRatio'] = housing['2008q2'].div(housing[rec_bottom])
    df = get_list_of_university_towns()
    subset_list = df.to_records(index=False).tolist()
    #uni_towns = housing.loc[subset_list]
    uni_towns = housing.loc[housing.index.isin(subset_list)]
    non_uni_towns = housing.loc[-housing.index.isin(subset_list)]
    is_uni = uni_towns.loc[:,'PriceRatio'].dropna()
    not_uni  = non_uni_towns.loc[:,'PriceRatio'].dropna()
    p_val = list(ttest_ind(is_uni, not_uni))[1]
    #different = np.where(p_val < 0.01, True, False)
    def different():
        p = p_val
        different = None
        if p_val < 0.01:
            different = True
        else:
            different = False
        return different
    def better():
        if not_uni.mean() < is_uni.mean():
            return 'non-university town'
        else:
            return 'university town'
    #better = np.where(uni_towns['PriceRatio'].mean() < non_uni_towns['PriceRatio'].mean(),"university town","non-university town")
    result = (different(),p_val,better())
    return result
