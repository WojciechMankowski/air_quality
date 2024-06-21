#!/bin/bash

python3 ./dowland_data_for_city/bydgoszcz.py  &
python3 ./dowland_data_for_city/gdansk.py &
python3 ./dowland_data_for_city/katowice.py &
python3 ./dowland_data_for_city/krakow.py &
python3 ./dowland_data_for_city/lodz.py &
python3 ./dowland_data_for_city/lublin.py &
python3 ./dowland_data_for_city/poznan.py &
python3 ./dowland_data_for_city/szczecin.py &
python3 ./dowland_data_for_city/warsaw.py &
python3 ./dowland_data_for_city/wroclaw.py &
wait