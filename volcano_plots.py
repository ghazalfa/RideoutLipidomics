# using data from p and t tests to make volcano plot
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


pTestEWFneg = {'Cer': 0.048373022135593115, 'CL': 0.03493496867644793, 'DGGA': 0.7344332303261454, 'Dodecylbenzenesulfonic': 0.4713842007439111, 'FA': 0.4552412929967504, 'FAHFA': 0.042562229014611104, 'HexCer': 0.027552752080498438, 'LPC': 0.8816046023839198, 'LPE': 0.8951028905827498, 'LPE O': 0.6568699110640221, 'LPE-N': 0.0447182481076588, 'Norethisterone': 0.5523705590901036, 'PA': 0.025646549086168716, 'PC': 0.5432210055518667, 'PC O': 0.07955008452308072, 'PE': 0.22960731253360614, 'PE O': 0.9734244402536202, 'PE-Cer': 0.7587986709576992, 'PG': 0.6439487888996998, 'PI': 0.05219847906825659, 'PS': 0.00457370543036099, 'SHexCer': 0.602085739700719, 'ST': 0.252388356824729}
pTestEWFpos = {'4-Imidazoleacrylic': 0.5652188236684663, 'CAR': 0.003968641118458284, 'CE': 0.19365087176076057, 'Cer': 0.8923019743171974, 'CL': 0.024490341758862447, 'DG': 0.3427703728706769, 'DG O': 0.42333101604280643, 'Diisodecyl': 0.09235957638161081, 'Dioctyl': 0.41803401095295956, 'LPC': 0.8770993453438901, 'LPE': 0.9698773067220237, 'MG': 0.17167243287767756, 'MGDG': 0.6413326926269822, 'NAE': 0.10013115257492022, 'NAOrn': 0.26841045082917214, 'PC': 0.1441481761457514, 'PC O': 0.8818745678874174, 'PE': 0.40626055954605206, 'PE O': 0.5577511365270305, 'PE P': 0.5928819543827641, 'PG': 0.9223498751391217, 'PI': 0.062223393538774895, 'PS': 0.014190470806744876, 'SE': 0.0021146481329762084, 'SM': 0.809356478265671, 'ST': 0.896217195183729, 'TG': 0.3317680271851504, 'TG O': 0.30253110863525967}
pTestWBFneg = {'Cer': 0.1564654642749912, 'CL': 0.7746050861648025, 'DGGA': 0.39958961944139104, 'Dodecylbenzenesulfonic': 0.6630782768774297, 'FA': 0.9946957546306681, 'FAHFA': 0.23213400959874056, 'HexCer': 0.0021470761793168443, 'LPC': 0.9377742095025774, 'LPE': 0.6769602685474102, 'LPE O': 0.8302205721651883, 'LPE-N': 0.015203285642579422, 'Norethisterone': 0.9660849960075792, 'PA': 0.7856159783804595, 'PC': 0.058291466476381226, 'PC O': 0.5648305346869082, 'PE': 0.1581411196598099, 'PE O': 0.201251876343901, 'PE-Cer': 0.9887762209961619, 'PG': 0.2139623747651512, 'PI': 0.8636141374199066, 'PS': 0.9811464046296909, 'SHexCer': 0.6855061865091019, 'ST': 0.5881876244687109}
pTestWBFpos = {'4-Imidazoleacrylic': 0.5204490293522874, 'CAR': 0.0058305146388349435, 'CE': 0.6700877277209836, 'Cer': 0.0274724635459266, 'CL': 0.7322290173184964, 'DG': 0.8292608214673106, 'DG O': 0.5395113944680108, 'Diisodecyl': 0.7990448941136339, 'Dioctyl': 0.9014160692843975, 'LPC': 0.9821921237571648, 'LPE': 0.6819748066405715, 'MG': 0.36514134623417543, 'MGDG': 0.8320319269453993, 'NAE': 0.2778051846024507, 'NAOrn': 0.2823650053338329, 'PC': 0.9510991013228367, 'PC O': 0.5221786798426624, 'PE': 0.11679914228845521, 'PE O': 0.35679769977104353, 'PE P': 0.16760842473526721, 'PG': 0.17834182912050128, 'PI': 0.7031209520353352, 'PS': 0.47206482004566763, 'SE': 0.4960813390414658, 'SM': 0.451980173659116, 'ST': 0.07641705121887528, 'TG': 0.7070024373830246, 'TG O': 0.38029957279020343}

tTestEWFneg = {'Cer': 2.4712901417251647, 'CL': -2.7136766931746994, 'DGGA': 0.3554239181740577, 'Dodecylbenzenesulfonic': 0.7684304499279877, 'FA': 0.7980812843966884, 'FAHFA': 2.5660221144540767, 'HexCer': 2.8939044847473134, 'LPC': 0.1553968183473346, 'LPE': 0.137540794950044, 'LPE O': 0.46715798060418756, 'LPE-N': -2.5293610450305875, 'Norethisterone': 0.6292569513363078, 'PA': -2.9489901005356316, 'PC': 0.644284110917609, 'PC O': 2.1083859858401675, 'PE': 1.3372372091728157, 'PE O': 0.034726306415924474, 'PE-Cer': 0.3214137110640955, 'PG': 0.4863845661805535, 'PI': -2.415263901172338, 'PS': -4.3989192513883415, 'SHexCer': -0.5501407519255535, 'ST': 1.266172233372222}
tTestEWFpos = {'4-Imidazoleacrylic': 0.6084134758920574, 'CAR': 4.531546829082587, 'CE': 1.4635411742000408, 'Cer': -0.14124153981994858, 'CL': 2.9846059756639134, 'DG': 1.0299053079650906, 'DG O': 0.8589886905527427, 'Diisodecyl': 2.0005212644159305, 'Dioctyl': 0.8694221731999608, 'LPC': 0.16136904711121278, 'LPE': 0.03936397779069302, 'MG': 1.5518950811333523, 'MGDG': 0.4903017542644697, 'NAE': 1.9422349308173938, 'NAOrn': 1.2195094152289323, 'PC': 1.6790448702775231, 'PC O': 0.1550391553637848, 'PE': 0.8929709938318939, 'PE O': 0.6204922134691028, 'PE P': 0.5644877435378955, 'PG': 0.10164542626610822, 'PI': -2.286719724116496, 'PS': -3.4173146661346094, 'SE': 5.150294912915923, 'SM': -0.2521281348623401, 'ST': 0.13606911856273962, 'TG': -1.0556523543948202, 'TG O': 1.127654205960767}
tTestWBFneg = {'Cer': 1.6195068946278908, 'CL': 0.2995790755714338, 'DGGA': -0.9065431572529709, 'Dodecylbenzenesulfonic': 0.4579890953555741, 'FA': -0.00692950183243671, 'FAHFA': 1.3290526897491801, 'HexCer': 5.13471753589864, 'LPC': -0.0813961354970037, 'LPE': -0.4376418449649963, 'LPE O': -0.22395876967518588, 'LPE-N': -3.361399226395872, 'Norethisterone': -0.04432329956010859, 'PA': -0.2844659978673049, 'PC': 2.3343658301264627, 'PC O': -0.6090391075958591, 'PE': -1.6117571695136765, 'PE O': -1.435148300772185, 'PE-Cer': -0.014663296503323842, 'PG': -1.3898013795336615, 'PI': -0.17928626073787315, 'PS': 0.02463313985259748, 'SHexCer': 0.4252175133482255, 'ST': -0.5718550159479082}
tTestWBFpos = {'4-Imidazoleacrylic': -0.6823961323493062, 'CAR': 4.1773710349563995, 'CE': 0.44768897680354536, 'Cer': -2.8961405091211354, 'CL': 0.3585232850828139, 'DG': 0.22524986879294742, 'DG O': -0.6504220859246129, 'Diisodecyl': -0.2661343362513523, 'Dioctyl': -0.1292073659575085, 'LPC': -0.023266560825902914, 'LPE': -0.43034242182823323, 'MG': 0.9795419892426109, 'MGDG': 0.22152322932664403, 'NAE': 1.1932634564537437, 'NAOrn': 1.180799429148723, 'PC': -0.06393463625167803, 'PC O': -0.6794640273963823, 'PE': -1.8311667945662509, 'PE O': -0.99803006878825, 'PE P': -1.5693894750731634, 'PG': -1.5240146442464444, 'PI': -0.39983854014325193, 'PS': -0.7671960910441725, 'SE': -0.724405290694742, 'SM': 0.804161388076018, 'ST': -2.137468391095823, 'TG': 0.3942859196303128, 'TG O': -0.9467891874482574}

avgFoldEWFneg = {'Cer': 1.1452563231063841, 'CL': 0.8814291281208129, 'DGGA': 1.0251382233689643, 'Dodecylbenzenesulfonic': 1.263838977194195, 'FA': 1.1966971205330064, 'FAHFA': 2.234480540366677, 'HexCer': 1.2208760484622554, 'LPC': 1.0304933414043584, 'LPE': 1.0353262445371108, 'LPE O': 1.0586814513915572, 'LPE-N': 0.8867889221556886, 'Norethisterone': 1.205898320240148, 'PA': 0.7651667548967708, 'PC': 1.0211584991862301, 'PC O': 1.0797678414281524, 'PE': 1.0751742487679974, 'PE O': 1.0010950163693857, 'PE-Cer': 1.0211142839749299, 'PG': 1.041754540023465, 'PI': 0.8328761823973974, 'PS': 0.6381092699323812, 'SHexCer': 0.9285100270943732, 'ST': 1.4293605481016272}
avgFoldEWFpos = {'4-Imidazoleacrylic': 1.4692301752760404, 'CAR': 1.2449885604327338, 'CE': 1.4179681210755113, 'Cer': 0.998179625181176, 'CL': 1.1278436817692454, 'DG': 1.116251553955959, 'DG O': 1.5812812399688174, 'Diisodecyl': 1.6322208257692128, 'Dioctyl': 1.3280212302667393, 'LPC': 1.0342514263230376, 'LPE': 1.0097961584579533, 'MG': 1.2197064552031163, 'MGDG': 1.0952380952380953, 'NAE': 1.2793391197566353, 'NAOrn': 1.2034807485993564, 'PC': 1.010817524852193, 'PC O': 1.0053671545638554, 'PE': 1.0192241009494065, 'PE O': 1.019178833576481, 'PE P': 1.030189272794002, 'PG': 1.0075375518129943, 'PI': 0.8697236771228496, 'PS': 0.7008405343747741, 'SE': 1.3088162828066416, 'SM': 0.9778308116188803, 'ST': 1.0059021005850945, 'TG': 0.9132316747104094, 'TG O': 1.2767568712598634}
avgFoldWBFneg = {'Cer': 1.0726038100290975, 'CL': 1.0162119457003913, 'DGGA': 0.931736085514191, 'Dodecylbenzenesulfonic': 1.1284856599861783, 'FA': 0.9985557340551776, 'FAHFA': 1.2640720488903183, 'HexCer': 1.288676607642125, 'LPC': 0.9845641646489104, 'LPE': 0.8979382041130483, 'LPE O': 0.9747214140637865, 'LPE-N': 0.8261601796407185, 'Norethisterone': 0.9881043622660791, 'PA': 0.9625198517734251, 'PC': 1.0391411226643357, 'PC O': 0.978167036835268, 'PE': 0.9499206806347845, 'PE O': 0.9598805060306405, 'PE-Cer': 0.9991564932886143, 'PG': 0.8881423152500162, 'PI': 0.9845050302139093, 'PS': 1.0015625415673615, 'SHexCer': 1.0531985506142478, 'ST': 0.8849842991721382}
avgFoldWBFpos = {'4-Imidazoleacrylic': 0.8048027179368389, 'CAR': 1.2126850406824345, 'CE': 1.0706810497504429, 'Cer': 0.9590831230172003, 'CL': 1.0176029058126315, 'DG': 1.021646715176173, 'DG O': 0.810825270173186, 'Diisodecyl': 0.9586649909230555, 'Dioctyl': 0.9809880239520958, 'LPC': 0.9952734605547905, 'LPE': 0.9020044795366621, 'MG': 1.0912458263772955, 'MGDG': 1.0709547500592276, 'NAE': 1.1247337035900011, 'NAOrn': 1.1608058171414948, 'PC': 0.9991871430168633, 'PC O': 0.9693611332363493, 'PE': 0.9610105624023559, 'PE O': 0.9786614050257305, 'PE P': 0.9224243695276044, 'PG': 0.8852983533861096, 'PI': 0.9682813719351145, 'PS': 0.9423966684075528, 'SE': 0.9446063202999464, 'SM': 1.05643188019119, 'ST': 0.8888128656840489, 'TG': 1.051578316161504, 'TG O': 0.8752316898797861}

df = pd.DataFrame.from_dict(tTestEWFneg, orient='index', columns=['t_statistic'])



# create a pandas DataFrame for pTestEWFneg and add avgFoldEWFneg as a new column
df = pd.DataFrame.from_dict(pTestEWFneg, orient='index', columns=['p_value'])
df['avgFoldChange'] = avgFoldEWFneg.values()

# set significance threshold
alpha = 0.05

# calculate the negative logarithm of the p-values and set as new column
df['-log10(p_value)'] = -np.log10(df['p_value'])

# calculate the  logarithm of the FC and set as new column
df['log2(avgFoldChange)'] = np.log2(df['avgFoldChange'])



# set up plot with Seaborn
sns.set_style("white")
sns.set(font_scale=1.2)
plt.figure(figsize=(8,6))

# create scatter plot of -log10(p-value) against avgFoldChange
sns.scatterplot(x='log2(avgFoldChange)', y='-log10(p_value)', data=df, color='grey')

# highlight significant points
sns.scatterplot(x='log2(avgFoldChange)', y='-log10(p_value)', data=df[df['p_value'] < alpha], color='red')

# add labels for the highlighted points
for i, row in df[df['p_value'] < alpha].iterrows():
    plt.text(np.log2(row['avgFoldChange']), -np.log10(row['p_value']), i, ha='center', va='bottom', fontsize=15)

# add axes labels and title
plt.xlabel('log2(Average Fold Change)')
plt.ylabel('-log10(p-value)')
plt.title('P Test Distribution for Genotype Female EWF Negative')

plt.axvline(0, 0,10)



# show plot
plt.show()



# create a pandas DataFrame for pTestEWFneg and add avgFoldEWFneg as a new column
df = pd.DataFrame.from_dict(pTestEWFpos, orient='index', columns=['p_value'])
df['avgFoldChange'] = avgFoldEWFpos.values()

# set significance threshold
alpha = 0.05

# calculate the negative logarithm of the p-values and set as new column
df['-log10(p_value)'] = -np.log10(df['p_value'])

# calculate the  logarithm of the FC and set as new column
df['log2(avgFoldChange)'] = np.log2(df['avgFoldChange'])



# set up plot with Seaborn
sns.set_style("white")
sns.set(font_scale=1.2)
plt.figure(figsize=(8,6))

# create scatter plot of -log10(p-value) against avgFoldChange
sns.scatterplot(x='log2(avgFoldChange)', y='-log10(p_value)', data=df, color='grey')

# highlight significant points
sns.scatterplot(x='log2(avgFoldChange)', y='-log10(p_value)', data=df[df['p_value'] < alpha], color='red')

# add labels for the highlighted points
for i, row in df[df['p_value'] < alpha].iterrows():
    plt.text(np.log2(row['avgFoldChange']), -np.log10(row['p_value']), i, ha='center', va='bottom', fontsize=15)

# add axes labels and title
plt.xlabel('log2(Average Fold Change)')
plt.ylabel('-log10(p-value)')
plt.title('P Test Distribution for Genotype Female EWF Positive')

plt.axvline(0, 0,10)


# create a pandas DataFrame for pTestEWFneg and add avgFoldEWFneg as a new column
df = pd.DataFrame.from_dict(pTestWBFpos, orient='index', columns=['p_value'])
df['avgFoldChange'] = avgFoldWBFpos.values()

# set significance threshold
alpha = 0.05

# calculate the negative logarithm of the p-values and set as new column
df['-log10(p_value)'] = -np.log10(df['p_value'])

# calculate the  logarithm of the FC and set as new column
df['log2(avgFoldChange)'] = np.log2(df['avgFoldChange'])



# set up plot with Seaborn
sns.set_style("white")
sns.set(font_scale=1.2)
plt.figure(figsize=(8,6))

# create scatter plot of -log10(p-value) against avgFoldChange
sns.scatterplot(x='log2(avgFoldChange)', y='-log10(p_value)', data=df, color='grey')

# highlight significant points
sns.scatterplot(x='log2(avgFoldChange)', y='-log10(p_value)', data=df[df['p_value'] < alpha], color='red')

# add labels for the highlighted points
for i, row in df[df['p_value'] < alpha].iterrows():
    plt.text(np.log2(row['avgFoldChange']), -np.log10(row['p_value']), i, ha='center', va='bottom', fontsize=15)

# add axes labels and title
plt.xlabel('log2(Average Fold Change)')
plt.ylabel('-log10(p-value)')
plt.title('P Test Distribution for Genotype Female WBF Positive')

plt.axvline(0, 0,10)


# create a pandas DataFrame for pTestEWFneg and add avgFoldEWFneg as a new column
df = pd.DataFrame.from_dict(pTestWBFneg, orient='index', columns=['p_value'])
df['avgFoldChange'] = avgFoldWBFneg.values()

# set significance threshold
alpha = 0.05

# calculate the negative logarithm of the p-values and set as new column
df['-log10(p_value)'] = -np.log10(df['p_value'])

# calculate the  logarithm of the FC and set as new column
df['log2(avgFoldChange)'] = np.log2(df['avgFoldChange'])


# set up plot with Seaborn
sns.set_style("white")
sns.set(font_scale=1.2)
plt.figure(figsize=(8,6))

# create scatter plot of -log10(p-value) against avgFoldChange
sns.scatterplot(x='log2(avgFoldChange)', y='-log10(p_value)', data=df, color='grey')

# highlight significant points
sns.scatterplot(x='log2(avgFoldChange)', y='-log10(p_value)', data=df[df['p_value'] < alpha], color='red')

# add labels for the highlighted points
for i, row in df[df['p_value'] < alpha].iterrows():
    plt.text(np.log2(row['avgFoldChange']), -np.log10(row['p_value']), i, ha='center', va='bottom', fontsize=15)

# add axes labels and title
plt.xlabel('log2(Average Fold Change)')
plt.ylabel('-log10(p-value)')
plt.title('P Test Distribution for Genotype Female WBF Negative')

plt.axvline(0, 0,10)


