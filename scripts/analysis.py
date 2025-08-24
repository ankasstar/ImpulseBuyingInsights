import csv
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"data/psych_marketing_data.csv")

df['Gender_num'] = df['Gender'].map({'M':1,'F':2})

user_cluster_name = None
user_cluster_cols = None
user_cluster_res = None

def data_for_cor():
    main_value = df['Impulse_Buying_Score']
    other_columns = [
        'Age', 'Gender_num', 'Big5_Openness', 'Big5_Conscientiousness',
        'Big5_Extraversion', 'Stress_Level', 'Reaction_Discount (%)', 'Reaction_Luxury_Ad (%)'
    ]
    return main_value, other_columns
def find_cor(main_value, other_columns):
    correlationTrue = {}
    correlationWeak = {}
    correlationNo = {}
    for col in other_columns:
        corr_value = main_value.corr(df[col])
        if corr_value >= 0.4:
            correlationTrue[col] = corr_value.item()
        elif (corr_value >= 0.2 and corr_value < 0.4):
            correlationWeak[col] = corr_value.item()
        else:
            correlationNo[col] = corr_value.item()
    return correlationTrue, correlationWeak, correlationNo
def cor_res():
    main_value, other_columns = data_for_cor()
    cortrue, corweak, corno = find_cor(main_value, other_columns)
    print("===== Strong correlations (>= 0.4) with Impulse Buying Score =====")
    if not cortrue:
        print("\tNo data available")
    else:
        for key, value in cortrue.items():
            print(f"\t{key}: {value}")
    print("===== Weak correlations (0.2 <= x <= 0.4) with Impulse Buying Score =====")
    if not corweak:
            print("\tNo data available")
    else:
        for key, value in corweak.items():
            print(f"\t{key}: {value}")
    print("===== No correlations with Impulse Buying Score observed =====")
    if not corno:
        print("\t No data available")
    else:
        for key, value in corno.items():
            print(f"\t{key}: {value}")

def cluster_own():
    global user_cluster_name, user_cluster_cols, user_cluster_res
    clustername = input("Enter the cluster's name: ")
    df[clustername]=0
    print("Choose the columns for clustering.")
    print("1 — Big5_Openness\n2 — Big5_Conscientiousness\n3 — Big5_Extraversion\n4 — Big5_Agreeableness\n5 — Big5_Neuroticism\n6 — Stress_Level\n7 — Impulse_Buying_Score")
    onecolumn, secondcolumn = int(input()), int(input())
    while (onecolumn!=secondcolumn):
        if onecolumn == 1:
            dfonecolumn = "Big5_Openness"
        elif onecolumn == 2:
            dfonecolumn = "Big5_Conscientiousness"
        elif onecolumn == 3:
            dfonecolumn = "Big5_Extraversion"
        elif onecolumn == 4:
            dfonecolumn = "Big5_Agreeableness"
        elif onecolumn == 5:
            dfonecolumn = "Big5_Neuroticism"
        elif onecolumn == 6:
            dfonecolumn = "Stress_Level"
        elif onecolumn == 7:
            dfonecolumn = "Impulse_Buying_Score"

        if secondcolumn == 1:
            dfsecondcolumn = "Big5_Openness"
        elif secondcolumn == 2:
            dfsecondcolumn = "Big5_Conscientiousness"
        elif secondcolumn == 3:
            dfsecondcolumn = "Big5_Extraversion"
        elif secondcolumn == 4:
            dfsecondcolumn = "Big5_Agreeableness"
        elif secondcolumn == 5:
            dfsecondcolumn = "Big5_Neuroticism"
        elif secondcolumn == 6:
            dfsecondcolumn = "Stress_Level"
        elif secondcolumn == 7:
            dfsecondcolumn = "Impulse_Buying_Score"
        break
    else:
        print("Columns cannot be the same. Try again")
    decision_one = int(input(f"For {dfonecolumn} do you want to see values above (1), below (2) or equal (3) to average?\nYour answer: "))
    if decision_one == 1:
        firstcond = df[dfonecolumn]>df[dfonecolumn].mean()
    elif decision_one == 2:
        firstcond = df[dfonecolumn]<df[dfonecolumn].mean()
    elif decision_one == 3:
        firstcond = df[dfonecolumn]==df[dfonecolumn].mean()
    decision_two = int(input(f"For {dfsecondcolumn} do you want to see values above (1), below (2) or equal (3) to average?\nYour answer: "))
    if decision_two == 1:
        seccond = df[dfsecondcolumn]>df[dfsecondcolumn].mean()
    elif decision_two == 2:
        seccond = df[dfsecondcolumn]<df[dfsecondcolumn].mean()
    elif decision_two == 3:
        seccond = df[dfsecondcolumn]==df[dfsecondcolumn].mean()
    user_cluster_cols = (dfonecolumn, dfsecondcolumn)
    df.loc[(firstcond) & (seccond), clustername]=1
    user_cluster_name = clustername
    user_cluster_res = df.groupby(clustername)[['Reaction_Discount (%)','Reaction_Luxury_Ad (%)']].mean()
    return user_cluster_res


def clusters_forming():
    df['cluster1'] = 0
    df.loc[(df["Big5_Conscientiousness"]>0.6) & (df['Impulse_Buying_Score']<80), 'cluster1']=1
    cluster1_res = df.groupby('cluster1')[['Reaction_Discount (%)','Reaction_Luxury_Ad (%)']].mean()

    df['cluster2'] = 0
    df.loc[(df['Big5_Extraversion']>0.5) & (df['Big5_Neuroticism']> 0.5), 'cluster2']=1
    cluster2_res = df.groupby('cluster2')[['Reaction_Discount (%)','Reaction_Luxury_Ad (%)']].mean()

    df['cluster3'] = 0
    df.loc[(df['Gender_num']==1) & (df['Stress_Level']>6), 'cluster3']=1
    cluster3_res = df.groupby('cluster3')[['Reaction_Discount (%)','Reaction_Luxury_Ad (%)']].mean()

    return cluster1_res, cluster2_res, cluster3_res
def clusters_res():
    cluster1_res, cluster2_res, cluster3_res = clusters_forming()
    print('-'*70)
    print('===== Cluster 1: Conscious people with low impulses =====')
    print(cluster1_res)
    print('-'*70)
    print('===== Cluster 2: Introverts with high levels of neuroticism =====')
    print(cluster2_res)
    print('-'*70)
    print('===== Cluster 3: Men with high stress levels =====')
    print(cluster3_res)
    print('-'*70)

def clusters_res_own():
    if user_cluster_res is not None:
        print(user_cluster_res)
        return user_cluster_cols
    else:
        print("You need to create your cluster first.")
        return None

def gender_count():
    male_count = 0
    fem_count = 0
    general_count = 0
    with open(r"D:\visulstc\project_csv\psych_marketing_data.csv") as f:
        file = csv.reader(f)
        headrow = next(file)
        indexd = headrow.index('Gender')
        indexb = headrow.index('Impulse_Buying_Score')
        sumb = 0
        for data in file:
            if (data[indexd] == 'F'):
                fem_count+=1
            if (data[indexd] == 'M'):
                male_count+=1
            general_count +=1
            sumb+=float(data[indexb])
    return sumb, general_count, fem_count, male_count
def gender_count_res():
    sumb, general_count, fem_count, male_count = gender_count()
    print(f"Percentage of females in this research: {round((fem_count/general_count)*100,1)}%")
    print(f"Percentage of males in this research: {round((male_count/general_count)*100,1)}%")
    print(f"Average Impulse Buying Score: {round((sumb/general_count),2)}")
def spec_graphs():
    again = 0
    while True:
        if again == 0:
            yesno = input("Would you like to see any specific graphs? y/n: ")
        elif again == 1:
            yesno = input("Would you like to see any specific graphs again? y/n: ")
        if yesno == 'n':
            print("OK, exiting")
            break
        elif yesno=='y':
            build_graph()
            again = 1
        else:
            print("That's an incorrect answer. Choose 'y' or 'n'")
def build_graph():
    cluster1_res, cluster2_res, cluster3_res = clusters_forming()
    sumb, general_count, fem_count, male_count = gender_count()
    clusters_res_own()

    while True:
        typegr = input("Choose what's the graph you'd like to see? \n\tHistogram of Impulse Buying Score: 0\n\tConscious people with low impulses: 1\n\tIntroverts with high levels of neuroticism: 2\n\tMen with high stress levels: 3\n\tRatio between males and females: 4\n\tResults of your own cluster: 5\n\tYour answer: ")
        cmap = plt.get_cmap('cool')
        color = cmap(0.6)
        if typegr == '0':
            plt.hist(df['Impulse_Buying_Score'], bins=15,color=color,edgecolor='black', alpha=0.7)
            plt.title('Histogram of Impulse Buying Score: ', fontsize=16)
            plt.show()
            break
        elif typegr == '1':
            plt.scatter(df["Big5_Conscientiousness"], df['Impulse_Buying_Score'], c=color, s=10)
            plt.title("Conscious people with low impulses. Scatter plot: ", fontsize=16)
            plt.xlabel("Conscientiousness level")
            plt.ylabel("Impulse buying score")
            plt.show()
            cluster1_res.plot(kind='bar')
            plt.title("Conscious people with low impulses. Bar plot: ", fontsize=16)
            plt.legend(["Reaction to Discount", "Reaction to Luxury Ad"])
            plt.show()
            break
        elif typegr == '2':
            plt.scatter(df["Big5_Extraversion"], df['Big5_Neuroticism'], c=color, s=10)
            plt.title("Introverts with high levels of neuroticism. Scatter plot: ", fontsize=16)
            plt.xlabel("Introversion level")
            plt.ylabel("Neuroticism")
            plt.legend(["Reaction to Discount", "Reaction to Luxury Ad"])
            plt.show()
            cluster2_res.plot(kind='bar')
            plt.title("Introverts with high levels of neuroticism. Bar plot: ", fontsize=16)
            plt.show()
            break
        elif typegr == '3':
            plt.scatter(df["Gender_num"], df['Stress_Level'], c=color, s=10)
            plt.title("Men with high stress levels. Scatter plot: ", fontsize=16)
            plt.xlabel("Gender")
            plt.ylabel("Level of stress")
            plt.legend(["Reaction to Discount", "Reaction to Luxury Ad"])
            plt.show()
            cluster3_res.plot(kind='bar')
            plt.title("Men with high stress levels. Bar plot: ", fontsize=16)
            plt.show()
            break
        elif typegr == '4':
            data = [round((fem_count/general_count)*100,1), round((male_count/general_count)*100,1)]
            labels = ['Males', 'Females']
            fig, ax = plt.subplots()
            ax.pie(data, labels=labels,autopct='%1.1f%%', colors = ['blue', 'deeppink'])
            plt.title("Ratio between males and females: ", fontsize=16)
            plt.show()
            break
        elif typegr == '5':
            if user_cluster_res is not None:
                dfonecolumn, dfsecondcolumn = user_cluster_cols
                plt.scatter(df[dfonecolumn], df[dfsecondcolumn], c=color, s=10)
                plt.legend(["Reaction to Discount", "Reaction to Luxury Ad"])
                plt.title(f"Your own cluster. Relationship {dfonecolumn}, {dfsecondcolumn} to discounts and luxury ads")
                plt.show()
            else:
                print("You need to create your cluster first.")
            break
        else:
            print("That's an incorrect answer.")

def user_interactive():
    while True:
        nextlvl = input("Choose what you'd like to see.\n\tThe correlations: 1\n\tThe formed clusters: 2\n\tMake your own cluster: 3\n\tThe count of genders: 4\n\tQuit: 'q'\n\tYour answer: ")
        if nextlvl == 'q':
            print("OK, exiting")
            break
        elif nextlvl == '1':
            cor_res()
        elif nextlvl == '2':
            clusters_res()
        elif nextlvl == '3':
            cluster_own()
            clusters_res_own()
        elif nextlvl == '4':
            gender_count_res()
        spec_graphs()

print("How would you like to use this data analysis?")
if __name__ == "__main__":
    user_interactive()
