MEDIAN_NUMBER = 1440

def median_filter(valid_lists):
    n = len(valid_lists)
    #filtered
    for i in range(n):
        Rincon_RSAM = Rincon_de_la_Vieja_df['rsam'][Rincon_de_la_Vieja_df.index.isin(valid_lists[i])]
        print(Rincon_RSAM)
        Rincon_RSAM = Rincon_RSAM.rolling(window=MEDIAN_NUMBER, center=True).median()
        print(f"Group {i+1} median filtered RSAM values:")
        print(Rincon_RSAM)


data = [1, 2, 3,4,5, 10, 20, 22,23,24,25 ]
result = select_valid_lists(data)

print(f"Input: {data}")
print(f"Result: {result}")

median_filter(result)

"""
MEDIAN_NUMBER = int(pd.Timedelta(weeks=1)/pd.Timedelta(minutes=1)) #10080

def median_filter(valid_lists):
    n = len(valid_lists)
    filtered = []
    for i in range(n):
        Rincon_RSAM = Rincon_de_la_Vieja_df['rsam'][Rincon_de_la_Vieja_df.index.isin(valid_lists[i])].copy()
        #print(Rincon_RSAM)
        Rincon_RSAM = Rincon_RSAM.rolling(window=MEDIAN_NUMBER, center=True).median()
        filtered.append(Rincon_RSAM)
    return filtered
    


data = eruptions_windows_indices[100]
result = select_valid_lists(data)
print(result[0])
rsam_filtered = median_filter(result)
n = len(rsam_filtered)
plt.figure(figsize=(15,8))
for i in range(n):
    plt.subplot(n, 1, i+1)
    #plt.plot(range(len(rsam_filtered[i])+1, 1,-1 ), rsam_filtered[i], label='RSAM', color='blue')
    #plt.plot(range(1, len(rsam_filtered[i])+1), rsam_filtered[i], label='RSAM', color='blue')
    dates = get_window_dates(result[i])
    plt.plot(dates, rsam_filtered[i], label='RSAM', color='blue')
    plt.title('Rincon de la Vieja - RSAM filtered')
    plt.xlabel('Time')
    plt.ylabel('RSAM')
    plt.legend()
#plt.tight_layout()
plt.show()


"""