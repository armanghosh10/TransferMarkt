data = pd.read_excel('Final3.xlsx')
data.columns

#Selecting the input features used to make price predictions
selected_columns = ['MV','Nation','Club','Leauge','Age','Starts','Gls90','Ast90','G+A','G/Sh',
                    'Tackle','Succ_x','Blocks','Clr','Passes Completed','Cmp%','Touches']
filtered_data = data[selected_columns]
 
# Creating a instance of label Encoder.
le = LabelEncoder()
 
# Using .fit_transform function to fit label
# encoder and return encoded label
label1 = le.fit_transform(filtered_data['Nation'])
label2 = le.fit_transform(filtered_data['Club'])
label3 = le.fit_transform(filtered_data['Leauge'])

filtered_data.drop("Nation", axis=1, inplace=True)
filtered_data["Nation"] = label1
filtered_data.drop("Club", axis=1, inplace=True)
filtered_data["Club"] = label2
filtered_data.drop("Leauge", axis=1, inplace=True)
filtered_data["Leauge"] = label3
filtered_data

#Splitting the data into training and testing data
y = filtered_data['MV']
x = filtered_data.drop('MV', axis=1)
x_train, x_test, y_train, y_test = train_test_split(
x, y, test_size=0.33, random_state=4)
