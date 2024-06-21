#!/bin/bash

python3 ./dowland_data_for_city/Cities/bydgoszcz.py  &
python3 ./dowland_data_for_city/Cities/gdansk.py &
python3 ./dowland_data_for_city/Cities/katowice.py &
python3 ./dowland_data_for_city/Cities/krakow.py &
python3 ./dowland_data_for_city/Cities/lodz.py &
python3 ./dowland_data_for_city/Cities/lublin.py &
python3 ./dowland_data_for_city/Cities/poznan.py &
python3 ./dowland_data_for_city/Cities/szczecin.py &
python3 ./dowland_data_for_city/Cities/warsaw.py &
python3 ./dowland_data_for_city/Cities/wroclaw.py &
wait