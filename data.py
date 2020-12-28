import pandas as pd
df = pd.read_excel("data.xlsx")
df.columns = ['Sr_No','FIR_No','IPC','Date_of_offence','Date_of_FIR','Police_station','Day','Time_of_offence','First_vehicle','Fatalities','Serious','Minor','Second_vehicle','Fatalities_1','Serious_1','Minor_1','Type_of_collision','Hit_and_run','Intersection_mid_block','Maneuver_type','Place_of_occurence','Total_Fatalities','Total_serious','Total_minor','Latitude','Longitude','Road_name','Road_number','Rural_urban']
print(df['Date_of_offence'].isnull().sum().sum())
df['Date_of_offence']=pd.to_datetime(df['Date_of_offence'],format='%m-%d-%Y').dt.strftime('%m/%d/%Y')
df['Date_of_FIR'] = pd.to_datetime(df['Date_of_FIR'],format='%m-%d-%Y').dt.strftime('%m/%d/%Y')
print(df['Date_of_offence'])
print(df['Date_of_FIR'])
df['geo']= df["Latitude"].astype(str) +","+ df["Longitude"].astype(str)
print(df['geo'].value_counts())

print(df['Longitude'].isnull().sum().sum());
#df['Time_of_offence'] = pd.to_datetime(df['Time_of_offence'])
s=[]
for i in df.Time_of_offence:
	s.append(i.strftime('%H'))
t=[]

for i in s:
	if i>='00' and i<'12':
		t.append('Morning')
	elif i>='12' and i<'16':
		t.append('Afternoon')
	elif i>='16' and i<'21':
		t.append('Evening')
	else:
		t.append('Night')
df['Time_session'] = t
df['d1'] = pd.to_datetime(df['Date_of_offence'], format='%m/%d/%Y')
df['d2'] = pd.to_datetime(df['Date_of_FIR'], format='%m/%d/%Y')
df['delta'] = df['d2']-df['d1']

df['delta'] = df['delta'].replace('days','',regex=True)

df.to_csv("data.csv")
