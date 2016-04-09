import pandas as pd


def load_combined():

    base_df = pd.DataFrame({'Time': range(48)})
    generation = [base_df]

    for i in range(6):
        gen_normalised_df = pd.read_csv('model_data/gen_profile_%d.txt' % i, names=['Gen_%d' % i], header=None)
        generation.append(gen_normalised_df)

    load = []
    for idx, letter in enumerate(['A', 'B', 'C', 'D', 'E', 'F']):
        load_df = pd.read_csv('model_data/Person%s.csv' % letter, names=['Load_%d' % idx], header=None)
        load.append(load_df)

    generation.extend(load)
    combined = pd.concat(generation, axis=1)

    #print(combined)

    return combined


if __name__ == "__main__":
    df = load_combined()
    assert isinstance(df, pd.DataFrame)
    df.to_csv("model_data/generation_and_load_half_hourly.csv")
