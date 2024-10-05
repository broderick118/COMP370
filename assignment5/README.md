for the first problem, running grep -Ec "noise" incidents_2020.csv returns 15 hits
so not many incidents

-> try case-insensitive -> returns 619027 hits

python filter_csv.py -i t1_test.csv -o test.csv

cat t1_data.csv | sort --unique | wc -l
returns 58