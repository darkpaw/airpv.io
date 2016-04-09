import csv


def _load_gen_profile(input_filename, output_code):

    total_panels = 5332.0
    # 'input_data/generation_profile.txt'
    rdr = csv.reader(open('input_data/' + input_filename))
    next(rdr)
    minute = 60*5

    generation_values = [0 for i in range(24*60)]

    for row in rdr:
        minute += 1
        value = float(row[1])
        generation_values[minute] = value

    generation_values_30minute = [0 for j in range(24*2)]
    minute = 0

    for idx, half_hour in enumerate(generation_values_30minute):
        half_hour_gen = 0
        for m in range(30):
            half_hour_gen += generation_values[minute]

            value = half_hour_gen / 30.0 / total_panels
            assert value <= 1.0
            assert value >= 0.0
            generation_values_30minute[idx] = value
            minute += 1

    with open("model_data/gen_profile_" + output_code + ".txt", 'w') as outfile:
        wr = csv.writer(outfile)
        for r in generation_values_30minute:
            value = "%0.2f" % r
            wr.writerow([value])



if __name__ == "__main__":

    for idx, letter in enumerate(['A', 'B', 'C', 'D', 'E', 'F']):
        _load_gen_profile('gen profile' + letter + '.txt', '%d' % idx)





