import pandas as pd


def load_combined():

    gen_normalised_df = pd.read_csv('model_data/generation_half_hourly.txt', names=['Generation'], header=None)
    #print(gen_normalised_df)

    test_df = pd.read_csv('model_data/generation_half_hourly.txt', names=['Consumption'], header=None)
    #print(test_df)

    combined = pd.concat([gen_normalised_df, test_df], axis=1)
    print(combined)

    return combined


