# Parashikimi i orarit të punës së punonjësve

Ky projekt synon të parashikojë orët e punës të punonjësve bazuar në ditën e tyre të punës, duke përdorur algoritmet e "Machine Learning. Ne kemi përdorur një grup të dhënash të quajtur "employee_working_hours.csv" i cili përmban atributet e mëposhtme: employee_name, working_day, date, hours_of_work, and work_from_home. Ne synojme dy modele, një që parashikon orarin e punës në bazë të ditës specifike dhe nëse punonjësi punon nga shtëpia apo jo, dhe një tjetër që parashikon orarin e punës bazuar në muajin specifik.

## Përpunim paraprak

Ne kemi krijuar një folder "preprocessing" që përmban dy skripta Python për parapërpunimin e të dhënave. Skripta e parë, "preprocess_names.py", modifikon emrat e punonjësve për performancë më të mirë. Skripti i dytë, "preprocess_date_and_days.py", modifikon datën në muaj dhe emrin e ditës në një numër për saktësi më të mirë të parashikimit.

## Grupi i të dhënave

Të dhënat fillestare janë marrë nga "employee_working_hours.csv", i cili përmban atributet e nevojshme për modelet tona të mësimit të makinerive. Të dhënat më pas përpunohen paraprakisht duke përdorur skriptet e përmendura më sipër.

## Modelet në Machine Learning

Ne planifikojmë të përdorim dy modele të "Machine Learning" për të arritur qasjen tonë, Linear Regression dhe K Nearest neighbors (KNN). Këto modele do të trajnohen në bazën e të dhënave të parapërpunuara për të parashikuar orët e punës bazuar në ditë dhe muaj të caktuar.

## Kërkesat
Për të ekzekutuar këtë projekt, do t'ju duhet të instaloni paketat e mëposhtme:
- pandas
- numpy
- scikit-learn


## Rezultatet

User interface qe paraqet 3 mundesite e aplikacionit per predikimin e oreve te punes 
<img src="./results/01.png">