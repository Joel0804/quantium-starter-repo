import glob
import pandas as pd

# combine all files in one csv
all_dfs = []
for one_filename in glob.glob('data/*.csv'):
    new_df = pd.read_csv(one_filename, 
                         usecols = ['product','price','quantity','region','date'])
    all_dfs.append(new_df) # put them inside blank list
combined_df = pd.concat(all_dfs) # make them proper in order look clean

#filtered data
combined_df["product"] = combined_df["product"].str.lower() # make all of them small character
combined_df['price'] = combined_df['price'].replace('[\$]', '', regex=True) # remove dollar sign 
combined_df['price'] = combined_df['price'].astype(float)# make them float value
combined_df["sales"] = combined_df["price"] * combined_df["quantity"] # get sales


filtered_data = combined_df[combined_df["product"] == "pink morsel"] # filtered out only pink morsel
final_data = filtered_data[['sales', 'date', 'region']]
print(final_data.head())
final_data.to_csv("formatted_sales_data.csv", index=False)
