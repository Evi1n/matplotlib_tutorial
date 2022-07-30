from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

plt.title('My Awesome Pie Chart')

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
# colors = ['#008f5d', '#fc4f30', '#e5ae37', '#6d904f']
explode = [0, 0, 0, 0.1, 0] # grafikte dikkat çekmek istenen bir nokta varsa grafiğin dışına çıkarmak için kullanılır.

plt.pie(slices, labels=labels, explode=explode, shadow=True, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})  # daire dilimi şeklindeki grafikler oluşturur. wedgeprops ile daire çevresini ve çizgileri belirginleştirdik.
# pie grafiği çok kalabalık veriler için pek kullanışlı olmaz çünkü sayısal veriler net bir şekilde ortada değildir.
# autopct verilerin dairesel oranlarını öğrenmemize yardımcı olur.

plt.tight_layout()
plt.show()