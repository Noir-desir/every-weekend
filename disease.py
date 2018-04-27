total = 100000

disease = total*0.01
undisease = total - disease

disease_positive = disease * 0.9
undisease_positive= undisease *0.09

total_positive = undisease_positive + disease_positive

print('%s 人中\n检测结果为阳性的人数为 %d\n阳性人群中实际患病人数 %d\n检测为阳性的实际患病率为 %0.4f '
      % (total, total_positive, disease_positive, disease/total_positive))
