pip3 install faker

if [ "$CREATE_TABLE" = "true" ]
then
    python3 create_table.py
else
  echo "$CREATE_TABLE"
  echo "$0"
  echo "no try again"
fi

flask run --host=0.0.0.0 --port=5500