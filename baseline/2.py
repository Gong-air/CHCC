import csv
labels = []
with open('../单句分割/prompt_offensive/test.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        labels.append(row[0])
# with open('tarlabels.txt',"w") as f:
#     f.writelines(labels)
# labels = []
# with open('检测/test.csv', newline='', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         labels.append(row[0])
with open('labels.txt',"w") as f:
    f.writelines(labels)
def gettext(split,temp):
    with open(split+'/train.csv', newline='', encoding='utf-8') as trainfile:
        with open(split+'/dev.csv', newline='', encoding='utf-8') as devfile:
            with open(split+'/test.csv', newline='', encoding='utf-8') as testfile:
                with open(temp+"/train.txt", "w",encoding='utf-8') as file:
                    train_reader = csv.reader(trainfile)
                    for row in train_reader:
                        row[1] = row[1].replace('\r', '')
                        row[1] = row[1].replace('\n', '')
                        file.write(row[1])
                        file.write('\t')
                        file.write(row[0])
                        file.write('\n')
                with open(temp + "/dev.txt", "w", encoding='utf-8') as file:
                    dev_reader = csv.reader(devfile)
                    for row in dev_reader:
                        row[1] = row[1].replace('\r', '')
                        row[1] = row[1].replace('\n', '')
                        file.write(row[1])
                        file.write('\t')
                        file.write(row[0])
                        file.write('\n')
                with open(temp + "/test.txt", "w",encoding='utf-8') as file:
                    test_reader = csv.reader(testfile)
                    for row in test_reader:
                        row[1] = row[1].replace('\r', '')
                        row[1] = row[1].replace('\n', '')
                        file.write(row[1])
                        file.write('\t')
                        file.write(row[0])
                        file.write('\n')
gettext("../单句分割/prompt_offensive","单句")

gettext("../分割结果/prompt_offensive","连续")